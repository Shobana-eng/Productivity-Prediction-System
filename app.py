from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import os
import json
import pandas as pd

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

# ---------------- COLAB LOGIC RECREATED EXACTLY ---------------- #

def predict_score(user_input):
    row = pd.DataFrame([user_input])
    return float(model.predict(row)[0])


def stress_burnout_alerts(user_input):
    alerts = []

    if user_input['stress_index'] >= 7:
        alerts.append("⚠️ High Stress: You should take relaxation breaks today.")

    if user_input['burnout_level'] >= 6:
        alerts.append("🔥 Burnout Risk: Reduce workload and rest properly.")

    if user_input['sleep_hours'] < 7:
        alerts.append("😴 Low Sleep: Aim for 7–8 hours tonight.")

    if user_input['screen_time'] >= 6:
        alerts.append("📱 High Screen Time: Reduce mobile usage during work hours.")

    if user_input['unlock_count'] >= 50:
        alerts.append("🔓 Too Many Phone Unlocks: Enable focus mode for 1–2 hours.")

    if len(alerts) == 0:
        alerts.append("👍 No alerts today! You're doing great.")

    return alerts


def generate_recommendations(user_input):
    recs = []

    if user_input['sleep_hours'] < 7:
        recs.append("Sleep 7–8 hours tonight for better clarity.")

    if user_input['study_hours'] < 3:
        recs.append("Increase focused work/study by 1 hour.")

    if user_input['screen_time'] > 5:
        recs.append("Reduce screen time by at least 1–2 hours.")

    if user_input['physical_activity'] < 1:
        recs.append("Do a 20-minute walk or light exercise today.")

    if user_input['breaks'] < 3:
        recs.append("Take 3–4 mindful breaks during the day.")

    if user_input['unlock_count'] > 50:
        recs.append("Reduce phone checks using DND or focus mode.")

    if user_input['social_media_hours'] > 1:
        recs.append("Limit social media to under 1 hour.")

    if user_input['stress_index'] > 5:
        recs.append("Do a 3-minute breathing exercise to reduce stress.")

    if user_input['burnout_level'] > 5:
        recs.append("Take a lighter schedule today to prevent burnout.")

    if len(recs) == 0:
        recs.append("Great job! Maintain your healthy routine.")

    return recs


def generate_daily_plan(user_input):
    plan = []

    if user_input['sleep_hours'] < 7:
        plan.append("Sleep early today and target 7–8 hours.")

    plan.append("Do one 45-minute deep work session in the morning.")
    plan.append("Take a 10-minute mindful break every 90 minutes.")

    if user_input['physical_activity'] < 1:
        plan.append("Do a 20-minute walk or light exercise.")

    if user_input['screen_time'] > 5:
        plan.append("Keep your phone away during work periods.")

    if user_input['unlock_count'] > 50:
        plan.append("Turn on Do Not Disturb for 2 hours.")

    if user_input['social_media_hours'] > 1:
        plan.append("Use social media only during breaks.")

    plan.append("Review your tasks in the evening for 5 minutes.")

    return plan


def award_badges_and_rewards(user_input, score,
                             storage_path=os.path.join(os.path.dirname(__file__), "user_rewards.json")):

    s = float(score)
    pts = 0
    badges = []

    # Score-based rewards
    if s >= 80:
        pts = 50; badges.append("🏅 Gold Achiever")
    elif s >= 60:
        pts = 30; badges.append("🥈 Silver Performer")
    else:
        pts = 10; badges.append("💪 Keep Improving")

    # Additional conditional badges
    if user_input.get('focus_hours', 0) >= 6:
        badges.append("🎯 Focus Master"); pts += 5

    if user_input.get('sleep_hours', 0) >= 7:
        badges.append("😴 Sleep Hero"); pts += 5

    if user_input.get('screen_time', 0) <= 2:
        badges.append("📵 Low Screen Champ"); pts += 3

    # Load previous state
    if os.path.exists(storage_path):
        try:
            with open(storage_path, "r") as f:
                state = json.load(f)
        except:
            state = {"points": 0, "badges": []}
    else:
        state = {"points": 0, "badges": []}

    # Update points
    state["points"] = int(state.get("points", 0) + pts)

    # Update badges
    for b in badges:
        if b not in state["badges"]:
            state["badges"].append(b)

    # Save back
    with open(storage_path, "w") as f:
        json.dump(state, f)

    if len(badges) == 0:
        badges.append("✨ Starter Reward")

    return pts, badges, state


# ------------------- MAIN PREDICT ROUTE ------------------- #

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json or {}

    # Convert to float safely
    def to_float(key):
        try:
            return float(data.get(key, 0))
        except:
            return 0.0

    user_input = {
        "screen_time": to_float("screen_time"),
        "study_hours": to_float("study_hours"),
        "sleep_hours": to_float("sleep_hours"),
        "social_media_hours": to_float("social_media_hours"),
        "physical_activity": to_float("physical_activity"),
        "breaks": to_float("breaks"),
        "unlock_count": to_float("unlock_count"),
        "focus_hours": to_float("focus_hours"),
        "stress_index": to_float("stress_index"),
        "burnout_level": to_float("burnout_level")
    }

    score = predict_score(user_input)
    alerts = stress_burnout_alerts(user_input)
    recs = generate_recommendations(user_input)
    plan = generate_daily_plan(user_input)
    pts, badges, state = award_badges_and_rewards(user_input, score)

    return jsonify({
        "score": round(score, 2),
        "alerts": alerts,
        "recommendations": recs,
        "daily_plan": plan,
        "points": pts,
        "badges": badges,
        "state": state
    })


# ---------------- SERVE FRONTEND ---------------- #

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    full_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
