/* Page switch */
function showPage(pageNumber) {
    document.querySelectorAll(".page").forEach(p => p.classList.remove("active"));
    document.getElementById(`page${pageNumber}`).classList.add("active");
    // hide results when entering page 3 until prediction
    if (pageNumber === 3) {
        const res = document.getElementById("resultsContainer");
        if (res) res.classList.add("hidden");
    }
}

/* Page 2 grid generation */
const behaviours = { 
    "Stress Level":["Low","Medium","Extreme"], 
    "Burnout Level":["Low","Medium","Extreme"], 
    "Sleep Quality":["Poor","Average","Excellent"], 
    "Productivity":["Low","Medium","High"], 
    "Focus Hours":["Low","Medium","High"], 
    "Screen Time":["Low","Medium","High"], 
    "Study Hours":["Low","Medium","High"], 
    "Physical Activity":["Low","Medium","High"], 
    "Social Media":["Low","Medium","High"] 
};

const colourMap = {
    "Low":"#b6e3b6",
    "Medium":"#f5f0e1",
    "High":"#f9c0c0",
    "Extreme":"#f9c0c0",
    "Poor":"#f9c0c0",
    "Average":"#f5f0e1",
    "Excellent":"#b6e3b6"
};

const gridContainer = document.querySelector(".grid-container");

for (const [name, levels] of Object.entries(behaviours)) {
    const box = document.createElement("div");
    box.className = "grid-box";

    const title = document.createElement("h3");
    title.innerText = name;

    const tooltip = document.createElement("span");
    tooltip.className = "tooltip";
    tooltip.setAttribute("data-tip", `This is your ${name} rating`);
    tooltip.innerText = " ℹ";

    title.appendChild(tooltip);
    box.appendChild(title);

    const levelsDiv = document.createElement("div");
    levelsDiv.className = "levels";

    levels.forEach(level => {
        const span = document.createElement("span");
        span.innerText = level;
        span.style.background = colourMap[level] || "#eee";
        span.style.padding = "5px 8px";
        span.style.borderRadius = "6px";
        levelsDiv.appendChild(span);
    });

    box.appendChild(levelsDiv);

    const numbersDiv = document.createElement("div");
    numbersDiv.className = "numbers";
    numbersDiv.innerHTML = "<span>1–3</span><span>4–6</span><span>7–9</span>";

    box.appendChild(numbersDiv);
    gridContainer.appendChild(box);
}

/* Page 3 prediction */
async function predictProductivity() {
    const inputData = {
        screen_time: parseFloat(document.getElementById("screen_time").value) || 0,
        study_hours: parseFloat(document.getElementById("study_hours").value) || 0,
        sleep_hours: parseFloat(document.getElementById("sleep_hours").value) || 0,
        social_media_hours: parseFloat(document.getElementById("social_media_hours").value) || 0,
        physical_activity: parseFloat(document.getElementById("physical_activity").value) || 0,
        breaks: parseFloat(document.getElementById("breaks").value) || 0,
        unlock_count: parseFloat(document.getElementById("unlock_count").value) || 0,
        focus_hours: parseFloat(document.getElementById("focus_hours").value) || 0,
        stress_index: parseFloat(document.getElementById("stress_index").value) || 0,
        burnout_level: parseFloat(document.getElementById("burnout_level").value) || 0
    };

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(inputData)
        });

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        const data = await response.json();

        const resultsContainer = document.getElementById("resultsContainer");
        resultsContainer.innerHTML = "";

        // Ensure we display score rounded to two decimals (backend already rounds but format again for safety)
        const displayScore = (typeof data.score === "number") ? data.score.toFixed(2) : parseFloat(data.score).toFixed(2);

        const scoreCard = document.createElement("div");
        scoreCard.className = "result-card";
        scoreCard.innerHTML = `<h2>Predicted Productivity Score</h2><p style="font-size:28px;font-weight:800;color:#333;margin-top:6px">${displayScore}</p>`;
        resultsContainer.appendChild(scoreCard);

        const alertsCard = document.createElement("div");
        alertsCard.className = "result-card";
        alertsCard.innerHTML = `<h3>Alerts:</h3><p>${(data.alerts && data.alerts.length) ? data.alerts.join("<br>") : "No alerts."}</p>`;
        resultsContainer.appendChild(alertsCard);

        const recCard = document.createElement("div");
        recCard.className = "result-card";
        recCard.innerHTML = `<h3>Recommendations:</h3><p>${(data.recommendations && data.recommendations.length) ? data.recommendations.join("<br>") : "No recommendations."}</p>`;
        resultsContainer.appendChild(recCard);

        const planCard = document.createElement("div");
        planCard.className = "result-card";
        planCard.innerHTML = `<h3>Daily Plan:</h3><p>${(data.daily_plan && data.daily_plan.length) ? data.daily_plan.join("<br>") : ""}</p>`;
        resultsContainer.appendChild(planCard);

        const rewardCard = document.createElement("div");
        rewardCard.className = "result-card";
        rewardCard.innerHTML = `
            <h3>Rewards & Badges:</h3>
            <p>Points: ${data.points ?? 0}</p>
            <p>Badges: ${(data.badges && data.badges.length) ? data.badges.join(", ") : "—"}</p>
        `;
        resultsContainer.appendChild(rewardCard);

        // show results pane
        resultsContainer.classList.remove("hidden");
    } catch (error) {
        alert("Error connecting to backend. Make sure your Flask server is running.");
        console.error(error);
    }
}
