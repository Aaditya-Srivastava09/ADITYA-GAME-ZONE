# ADITYA-GAME-ZONE
# 🎮 Aditya's Game Zone

A dynamic, arcade-style mini-game web app built with **Python + Streamlit** — featuring two fully interactive games with real-time animations, score tracking, and a dark neon UI.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

---

## 🕹️ Games Available

### 🎯 Number Quest
Guess the secret number chosen by the computer (between 1–100).
- Live range tracker that narrows after every guess
- Binary Search hints to guide you toward the optimal strategy
- Attempt counter + performance rating (Legendary / Optimal / Good)
- Full guess history log
- Win rate tracker across sessions

### ✂️ Rock · Paper · Scissors
Classic RPS against the computer — with a battle arena twist.
- Animated battle arena showing both choices with a VS banner
- Real-time score tracker — Wins / Draws / Losses / Win Rate %
- Last 8 rounds battle log
- Reset score option

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or above
- pip

### Installation

```bash
# 1. Clone or download this project
git clone https://github.com/yourusername/game-zone.git
cd game-zone

# 2. Install dependencies
pip install streamlit

# 3. Run the app
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
game-zone/
│
├── app.py          # Main Streamlit app (both games)
└── README.md       # Project documentation
```

---

## ✨ Features

| Feature | Details |
|--------|---------|
| 🎨 Dark Neon UI | Space-themed design with electric blue + purple gradients |
| 🔤 Custom Fonts | Orbitron + Rajdhani from Google Fonts |
| 🌌 Animated BG | Floating SVG particle blobs with smooth animations |
| 📊 Score Tracking | Persistent win/loss/draw stats within session |
| 📋 History Log | Last 8 rounds visible at all times |
| 💡 Smart Hints | Binary Search strategy tips in Number Quest |
| 📱 Responsive | Works on desktop and mobile browsers |

---

## 🧠 Tech Stack

| Technology | Usage |
|-----------|-------|
| Python | Core game logic |
| Streamlit | Web app framework |
| HTML/CSS | Custom UI styling |
| SVG | Background particle animations |
| Session State | Score + history persistence |

---

## 📈 Time & Space Complexity

### Number Quest
- **Time:** O(n) worst case — O(log n) if Binary Search strategy is followed
- **Space:** O(n) — stores guess history in session

### Rock Paper Scissors
- **Time:** O(1) per round — constant time logic
- **Space:** O(n) — stores battle history in session

---

## 🙋‍♂️ About the Developer

**Aditya** — First Year B.Tech AI/ML Student  
Interned at **IIHMR, MNNIT Allahabad** (Summer 2026)  
Built ML projects using Python, Scikit-learn, XGBoost, and Streamlit.

> *"First time writing both games from scratch — and this is what happened when Python met Streamlit."*

---

## 📌 Future Improvements

- [ ] Multiplayer mode
- [ ] Leaderboard with localStorage
- [ ] Sound effects
- [ ] Dark / Light theme toggle
- [ ] Difficulty levels for Number Quest (Easy: 1-50, Hard: 1-500)
- [ ] Best score tracking across sessions

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
Made with ❤️ and Python by Aditya
</div>
