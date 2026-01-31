# 🚀 MockVerse Pro: AI-Powered Exam Platform

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Gradio](https://img.shields.io/badge/Gradio-Web%20UI-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Analytics-11557c)
![Exam](https://img.shields.io/badge/Exam-JEE%20%7C%20NEET-green)

> **"Master your preparation with AI-driven analytics, real-time scoring, and smart explanations."**

**MockVerse Pro** is an advanced mock test generator built with **Python & Gradio**. Unlike simple quiz apps, it simulates real competitive exam logic (JEE/NEET), including negative marking, difficulty levels, and visual performance analysis using data visualization.


---

## ✨ Key Features

### 🧠 Smart Exam Engine
* **Real Exam Logic:** Implements the official marking scheme: **+4** for Correct, **-1** for Wrong, **0** for Skipped.
* **Difficulty Toggling:** Choose between **Easy**, **Medium**, or **Hard** levels to tailor your practice session.
* **Subject-Wise Filtering:** Select specific subjects (Physics, Chemistry, Maths) to focus your revision.

### 📊 Advanced Analytics
* **Visual Reports:** Automatically generates a **Pie Chart** using `Matplotlib` to visualize your accuracy vs. mistakes.
* **Time Tracking:** Tracks exactly how many seconds you took to complete the test to help improve speed.

### 💡 AI Explanations
* **Instant Feedback:** Doesn't just say "Wrong Answer" — it explains **WHY** the correct answer is right.
* **Detailed Solutions:** Provides step-by-step reasoning for every question attempted.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend UI** | Gradio (`gr.Blocks`) | Creating the Tabbed Interface & Interactive Elements |
| **Logic Core** | Python | Marking algorithms, Question filtering, State management |
| **Data Visualization** | Matplotlib | Generating performance pie charts |
| **Backend Data** | JSON / Dictionary | Structured Question Bank storage |

---

## ⚙️ Installation & Usage

Run this project locally or on Google Colab in minutes.

### 1. Install Dependencies
You need Python installed. Run the following command:
```bash
pip install gradio matplotlib
