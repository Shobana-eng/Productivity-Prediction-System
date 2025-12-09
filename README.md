# 📊 Productivity Prediction System  
### *By Shobana T*

A machine-learning based web application that analyzes daily habits and predicts a user's productivity score.  
The system provides smart alerts, personalized recommendations, daily plans, and badges to improve overall performance.

---

## 🚀 Project Overview

The **Productivity Prediction System** helps users understand how their daily behaviors — such as sleep, screen time, study hours, stress, and focus levels — affect their productivity.  
Using ML predictions and intelligent recommendations, the system guides users to build healthier and more efficient routines.

---

## 🎯 Main Goal of the Project

To **predict productivity** using machine learning and  
to **improve users’ routines** through smart alerts, recommendations, and personalized daily plans.

---

## 🧠 Features

### ✔ Productivity Prediction  
Predicts user productivity score based on 10 daily behavior inputs.

### ✔ Behavior Awareness  
Simple awareness page explaining factors affecting productivity.

### ✔ Behavior Classification Chart  
Visual grid explaining ranges from *Low → Medium → High*.

### ✔ Alerts  
Smart warnings for:  
- High stress  
- Burnout risk  
- Sleep shortage  
- High screen time  
- Excessive phone unlocks  

### ✔ Recommendations  
Personalized suggestions such as:  
- Sleep routine improvements  
- Study optimization  
- Screen time control  
- Stress reduction techniques  

### ✔ Daily Plan  
Automatically generated schedule for the day.

### ✔ Reward System  
Earn points and badges like  
🏅 Gold Achiever  
🥈 Silver Performer  
💪 Keep Improving  

---

## 🏗 System Architecture
       ┌─────────────────────────┐
       │       Frontend UI       │
       │ (HTML, CSS, JavaScript) │
       └───────────┬────────────┘
                   ↓
       ┌────────────────────────┐
       │       Flask API        │
       │  (Receives user input) │
       └───────────┬────────────┘
                   ↓
       ┌────────────────────────┐
       │    ML Model (pkl)      │
       │ Predict productivity   │
       └───────────┬────────────┘
                   ↓
   ┌──────────────────────────────────┐
   │ Alerts | Recommendations | Plan  │
   └──────────────────────────────────┘
                   ↓
       ┌─────────────────────────┐
       │     UI Results Page     │
       └─────────────────────────┘

## 🔄 Flowchart (ASCII)

┌────────────────────┐
│ User Enters Inputs │
└──────────┬─────────┘
           ↓
┌────────────────────┐
│ Data Sent to Flask │
└──────────┬─────────┘
           ↓
┌────────────────────┐
│ ML Model Predicts  │
│ Productivity Score │
└──────────┬─────────┘
           ↓
┌────────────────────┐
│ Alerts Generated   │
│ Recommendations    │
│ Daily Plan         │
└──────────┬─────────┘
           ↓
┌────────────────────┐
│ Results Displayed  │
└────────────────────┘

---

## 🛠 Technologies Used

### **Frontend**
- HTML  
- CSS  
- JavaScript  

### **Backend**
- Python  
- Flask  

### **Machine Learning**
- Scikit-learn  
- Regression model (`model.pkl`)  

---

## 📁 Project Structure


---

## ▶ How to Run the Project

### 1️⃣ Install Dependencies


### 2️⃣ Run the Flask Server

http://127.0.0.1:5000/

---

## 🧪 Input Parameters Used

| Parameter              | Description |
|-----------------------|-------------|
| screen_time           | Hours of screen usage |
| study_hours           | Productive learning hours |
| sleep_hours           | Total sleep duration |
| social_media_hours    | Hours spent on social media |
| physical_activity     | Daily physical movement |
| breaks                | Number of breaks taken |
| unlock_count          | Phone unlocks |
| focus_hours           | Deep work duration |
| stress_index          | Stress rating |
| burnout_level         | Burnout rating |

---

## 🏁 Results

The system outputs:

- **Predicted Productivity Score**  
- **Alerts**  
- **Recommendations**  
- **Daily Plan**  
- **Points Awarded**  
- **Badges Earned**  

---

## 📌 Conclusion

The **Productivity Prediction System** acts as a personal productivity coach.  
By analyzing daily habits and providing actionable insights, it helps users develop a healthier lifestyle, reduce stress, and improve focus and overall performance.

---

## 👩‍💻 Developer  
**Shobana T**

---

## ⭐ If you like this project  
Please Star ⭐ the repository on GitHub!

       └─────────────────────────┘


### 🖼 Architecture Diagram (ASCII)

