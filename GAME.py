import streamlit as st
import random
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ADITYA'S GAME ZONE",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #020814 !important;
    color: #e0e8ff;
    font-family: 'Rajdhani', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at 20% 20%, #0d1b4b 0%, #020814 50%, #0d0b1e 100%) !important;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #020814; }
::-webkit-scrollbar-thumb { background: #3a6fff; border-radius: 2px; }

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    position: relative;
}
.hero-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2rem, 6vw, 4.5rem);
    font-weight: 900;
    letter-spacing: 0.12em;
    background: linear-gradient(135deg, #3a6fff 0%, #a78bfa 50%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: none;
    animation: pulse-glow 3s ease-in-out infinite;
}
@keyframes pulse-glow {
    0%, 100% { filter: drop-shadow(0 0 8px #3a6fff88); }
    50%       { filter: drop-shadow(0 0 24px #a78bfa88); }
}
.hero-sub {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.1rem;
    color: #64748b;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}

/* ── GAME SELECTOR CARDS ── */
.selector-grid {
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    flex-wrap: wrap;
    padding: 1rem 0 2rem;
}
.game-card {
    background: linear-gradient(145deg, #0d1b4b22, #1e1b4b33);
    border: 1px solid #3a6fff44;
    border-radius: 20px;
    padding: 2rem 2.5rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    min-width: 220px;
    position: relative;
    overflow: hidden;
}
.game-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, #3a6fff11, #a78bfa11);
    opacity: 0;
    transition: opacity 0.3s;
}
.game-card:hover::before { opacity: 1; }
.game-card:hover {
    border-color: #3a6fff;
    transform: translateY(-4px);
    box-shadow: 0 12px 40px #3a6fff33;
}
.game-card.active {
    border-color: #a78bfa;
    background: linear-gradient(145deg, #1e1b4b55, #0d1b4b55);
    box-shadow: 0 0 30px #a78bfa44;
}
.card-icon { font-size: 3rem; margin-bottom: 0.75rem; }
.card-title {
    font-family: 'Orbitron', monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #c4b5fd;
    letter-spacing: 0.1em;
}
.card-desc { font-size: 0.85rem; color: #64748b; margin-top: 0.4rem; }

/* ── DIVIDER ── */
.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #3a6fff, #a78bfa, #38bdf8, transparent);
    margin: 0.5rem auto 2rem;
    max-width: 600px;
    animation: shimmer 3s linear infinite;
}
@keyframes shimmer {
    0%   { background-position: -600px; }
    100% { background-position: 600px; }
}

/* ── GAME CONTAINER ── */
.game-container {
    background: linear-gradient(145deg, #0a0f2e, #0d0b1e);
    border: 1px solid #3a6fff33;
    border-radius: 24px;
    padding: 2rem;
    max-width: 820px;
    margin: 0 auto;
    box-shadow: 0 0 60px #3a6fff1a, inset 0 0 60px #a78bfa08;
}

/* ── SCORE BAR ── */
.score-bar {
    display: flex;
    justify-content: space-around;
    align-items: center;
    background: #ffffff08;
    border: 1px solid #3a6fff22;
    border-radius: 16px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.5rem;
}
.score-item { text-align: center; }
.score-label {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #64748b;
    text-transform: uppercase;
}
.score-value {
    font-family: 'Orbitron', monospace;
    font-size: 2rem;
    font-weight: 900;
}
.score-wins  { color: #34d399; }
.score-draws { color: #fbbf24; }
.score-loss  { color: #f87171; }
.score-divider { width: 1px; height: 40px; background: #3a6fff33; }

/* ── NUMBER GAME SPECIFIC ── */
.range-bar-container {
    background: #ffffff08;
    border: 1px solid #3a6fff22;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.5rem;
    text-align: center;
}
.range-label {
    font-size: 0.75rem;
    color: #64748b;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.range-track {
    height: 6px;
    background: #ffffff11;
    border-radius: 99px;
    position: relative;
    overflow: visible;
}
.range-fill {
    height: 100%;
    background: linear-gradient(90deg, #3a6fff, #a78bfa);
    border-radius: 99px;
    transition: all 0.5s ease;
}
.range-marker {
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 14px;
    height: 14px;
    background: #fff;
    border: 2px solid #a78bfa;
    border-radius: 50%;
    box-shadow: 0 0 10px #a78bfa;
}

.attempt-badge {
    display: inline-block;
    background: linear-gradient(135deg, #3a6fff22, #a78bfa22);
    border: 1px solid #a78bfa44;
    border-radius: 99px;
    padding: 0.3rem 1rem;
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    color: #c4b5fd;
    margin-bottom: 1.5rem;
}

/* ── RPS CHOICE BUTTONS ── */
.rps-grid {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin: 1.5rem 0;
}
.rps-btn {
    background: linear-gradient(145deg, #0d1b4b33, #1e1b4b33);
    border: 2px solid #3a6fff44;
    border-radius: 20px;
    padding: 1.5rem 2rem;
    cursor: pointer;
    text-align: center;
    transition: all 0.25s ease;
    min-width: 140px;
}
.rps-btn:hover {
    border-color: #a78bfa;
    transform: translateY(-6px) scale(1.05);
    box-shadow: 0 16px 40px #a78bfa33;
    background: linear-gradient(145deg, #1e1b4b55, #0d1b4b55);
}
.rps-icon   { font-size: 3.5rem; }
.rps-label  {
    font-family: 'Orbitron', monospace;
    font-size: 0.8rem;
    color: #94a3b8;
    margin-top: 0.5rem;
    letter-spacing: 0.1em;
}

/* ── BATTLE ARENA ── */
.battle-arena {
    display: flex;
    align-items: center;
    justify-content: space-around;
    background: #ffffff05;
    border: 1px solid #3a6fff22;
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    flex-wrap: wrap;
    gap: 1rem;
}
.fighter {
    text-align: center;
}
.fighter-label {
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: #64748b;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.fighter-icon { font-size: 4.5rem; }
.vs-badge {
    font-family: 'Orbitron', monospace;
    font-size: 1.5rem;
    font-weight: 900;
    color: #a78bfa;
    text-shadow: 0 0 20px #a78bfa;
}

/* ── RESULT BANNER ── */
.result-banner {
    text-align: center;
    padding: 1.2rem;
    border-radius: 16px;
    font-family: 'Orbitron', monospace;
    font-size: 1.3rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    animation: banner-pop 0.4s cubic-bezier(.34,1.56,.64,1);
}
@keyframes banner-pop {
    0%   { transform: scale(0.7); opacity: 0; }
    100% { transform: scale(1);   opacity: 1; }
}
.result-win  { background: linear-gradient(135deg,#05401c,#064e3b); border:1px solid #34d399; color:#34d399; text-shadow:0 0 20px #34d39988; }
.result-lose { background: linear-gradient(135deg,#450a0a,#4c0519); border:1px solid #f87171; color:#f87171; text-shadow:0 0 20px #f8717188; }
.result-draw { background: linear-gradient(135deg,#451a03,#4a2308); border:1px solid #fbbf24; color:#fbbf24; text-shadow:0 0 20px #fbbf2488; }

/* ── HISTORY TABLE ── */
.history-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 1rem;
    border-bottom: 1px solid #3a6fff11;
    font-size: 0.85rem;
    color: #94a3b8;
}
.history-item:last-child { border-bottom: none; }
.hist-result-win  { color: #34d399; font-weight: 700; }
.hist-result-lose { color: #f87171; font-weight: 700; }
.hist-result-draw { color: #fbbf24; font-weight: 700; }

/* ── HINT BOX ── */
.hint-box {
    background: #ffffff06;
    border-left: 3px solid #3a6fff;
    border-radius: 0 12px 12px 0;
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    color: #94a3b8;
    margin: 1rem 0;
}

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg, #3a6fff, #6d28d9) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    padding: 0.65rem 1.5rem !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 15px #3a6fff44 !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px #3a6fff66 !important;
    background: linear-gradient(135deg, #5580ff, #7c3aed) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── INPUT ── */
.stNumberInput > div > div > input,
.stTextInput > div > div > input {
    background: #0d1b4b33 !important;
    border: 1px solid #3a6fff44 !important;
    border-radius: 12px !important;
    color: #e0e8ff !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 1.1rem !important;
    text-align: center !important;
    padding: 0.5rem !important;
}
.stNumberInput > div > div > input:focus,
.stTextInput > div > div > input:focus {
    border-color: #a78bfa !important;
    box-shadow: 0 0 0 2px #a78bfa33 !important;
}

/* ── SECTION HEADERS ── */
.section-header {
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    color: #3a6fff;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}

/* ── PARTICLE BG ── */
.particles {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
</style>

<div class="particles">
  <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <radialGradient id="g1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#3a6fff" stop-opacity="0.15"/>
        <stop offset="100%" stop-color="#3a6fff" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <circle cx="10%" cy="20%" r="180" fill="url(#g1)" opacity="0.4">
      <animate attributeName="cy" values="20%;25%;20%" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="85%" cy="70%" r="220" fill="url(#g1)" opacity="0.3">
      <animate attributeName="cy" values="70%;65%;70%" dur="10s" repeatCount="indefinite"/>
    </circle>
    <circle cx="50%" cy="90%" r="150" fill="url(#g1)" opacity="0.2">
      <animate attributeName="cy" values="90%;85%;90%" dur="12s" repeatCount="indefinite"/>
    </circle>
  </svg>
</div>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "game": None,
        # Number game
        "ng_target": random.randint(1, 100),
        "ng_attempts": 0,
        "ng_low": 1,
        "ng_high": 100,
        "ng_history": [],
        "ng_won": False,
        "ng_wins": 0,
        "ng_total": 0,
        # RPS game
        "rps_wins": 0,
        "rps_losses": 0,
        "rps_draws": 0,
        "rps_history": [],
        "rps_last": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-title">🎮 ADITYA'S GAME ZONE</div>
  <div class="hero-sub">Choose your battlefield · Play · Conquer</div>
</div>
<div class="neon-divider"></div>
""", unsafe_allow_html=True)

# ── GAME SELECTOR ─────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    g1, g2 = st.columns(2)
    with g1:
        if st.button("🎯  NUMBER QUEST", use_container_width=True):
            st.session_state.game = "number"
    with g2:
        if st.button("✂️  ROCK · PAPER · SCISSORS", use_container_width=True):
            st.session_state.game = "rps"

st.markdown("<div style='margin-bottom:1.5rem'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# NUMBER GUESSING GAME
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.game == "number":

    st.markdown('<div class="game-container">', unsafe_allow_html=True)

    # Score bar
    total = st.session_state.ng_total or 1
    st.markdown(f"""
    <div class="score-bar">
      <div class="score-item">
        <div class="score-label">Games Won</div>
        <div class="score-value score-wins">{st.session_state.ng_wins}</div>
      </div>
      <div class="score-divider"></div>
      <div class="score-item">
        <div class="score-label">Games Played</div>
        <div class="score-value" style="color:#c4b5fd">{st.session_state.ng_total}</div>
      </div>
      <div class="score-divider"></div>
      <div class="score-item">
        <div class="score-label">Win Rate</div>
        <div class="score-value score-wins">{int(st.session_state.ng_wins/total*100)}%</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.ng_won:
        # Range visual
        lo = st.session_state.ng_low
        hi = st.session_state.ng_high
        fill_pct  = ((lo - 1) / 99) * 100
        width_pct = ((hi - lo) / 99) * 100
        marker_pct = ((lo + hi) / 2 - 1) / 99 * 100

        st.markdown(f"""
        <div class="range-bar-container">
          <div class="range-label">Search Range: {lo} — {hi}  ({hi-lo+1} possibilities)</div>
          <div class="range-track">
            <div class="range-fill" style="margin-left:{fill_pct}%;width:{width_pct}%"></div>
            <div class="range-marker" style="left:{marker_pct}%"></div>
          </div>
        </div>
        <div style="text-align:center">
          <span class="attempt-badge">⚡ ATTEMPT #{st.session_state.ng_attempts + 1}</span>
        </div>
        """, unsafe_allow_html=True)

        # Hint
        if st.session_state.ng_attempts > 0:
            optimal = 7
            remaining = max(0, optimal - st.session_state.ng_attempts)
            tip = f"🔥 Optimal: guess the middle — {(lo+hi)//2}" if remaining > 0 else "💡 Try Binary Search: always guess the middle of the range!"
            st.markdown(f'<div class="hint-box">{tip}</div>', unsafe_allow_html=True)

        # Input
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            guess = st.number_input("Your Guess", min_value=1, max_value=100, step=1, value=(lo+hi)//2, key="ng_input", label_visibility="collapsed")
            if st.button("⚡  SUBMIT GUESS", use_container_width=True):
                g = int(guess)
                st.session_state.ng_attempts += 1

                if g < 1 or g > 100:
                    st.error("Out of range! Enter between 1 and 100.")
                elif g > st.session_state.ng_target:
                    st.session_state.ng_history.append(("📉", f"Guessed {g}", "Too High"))
                    st.session_state.ng_high = min(st.session_state.ng_high, g - 1)
                    st.toast("📉 Too High! Go lower.", icon="📉")
                elif g < st.session_state.ng_target:
                    st.session_state.ng_history.append(("📈", f"Guessed {g}", "Too Low"))
                    st.session_state.ng_low = max(st.session_state.ng_low, g + 1)
                    st.toast("📈 Too Low! Go higher.", icon="📈")
                else:
                    st.session_state.ng_won = True
                    st.session_state.ng_wins += 1
                    st.session_state.ng_total += 1
                    st.session_state.ng_history.append(("🎯", f"Guessed {g}", "CORRECT!"))
                st.rerun()

    else:
        # Win screen
        a = st.session_state.ng_attempts
        rating = "🏆 LEGENDARY" if a <= 5 else "🔥 OPTIMAL" if a <= 7 else "⚡ GOOD" if a <= 12 else "💪 KEEP PRACTICING"
        st.markdown(f"""
        <div class="result-banner result-win" style="margin-bottom:1.5rem">
          🎉 YOU CRACKED IT IN {a} ATTEMPTS! &nbsp;·&nbsp; {rating}
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔄  PLAY AGAIN", use_container_width=True):
                st.session_state.ng_target   = random.randint(1, 100)
                st.session_state.ng_attempts = 0
                st.session_state.ng_low      = 1
                st.session_state.ng_high     = 100
                st.session_state.ng_history  = []
                st.session_state.ng_won      = False
                st.rerun()
        with c2:
            if st.button("🏠  MAIN MENU", use_container_width=True):
                st.session_state.game = None
                st.rerun()

    # History
    if st.session_state.ng_history:
        st.markdown("<div class='section-header' style='margin-top:1.5rem'>📋 Guess History</div>", unsafe_allow_html=True)
        st.markdown("<div style='background:#ffffff05;border:1px solid #3a6fff22;border-radius:12px;padding:0.5rem'>", unsafe_allow_html=True)
        for icon, guess_txt, result in reversed(st.session_state.ng_history[-8:]):
            color = "#34d399" if result == "CORRECT!" else "#f87171" if result == "Too High" else "#fbbf24"
            st.markdown(f"""
            <div class="history-item">
              <span>{icon} {guess_txt}</span>
              <span style="color:{color};font-weight:700">{result}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ROCK PAPER SCISSORS GAME
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.game == "rps":

    RPS_ICONS  = {"ROCK": "🪨", "PAPER": "📄", "SCISSORS": "✂️"}
    RPS_BEATS  = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
    COMP_EMOJIS = {"ROCK": "🤖🪨", "PAPER": "🤖📄", "SCISSORS": "🤖✂️"}

    st.markdown('<div class="game-container">', unsafe_allow_html=True)

    # Score bar
    w = st.session_state.rps_wins
    l = st.session_state.rps_losses
    d = st.session_state.rps_draws
    total = w + l + d or 1
    st.markdown(f"""
    <div class="score-bar">
      <div class="score-item">
        <div class="score-label">Wins</div>
        <div class="score-value score-wins">{w}</div>
      </div>
      <div class="score-divider"></div>
      <div class="score-item">
        <div class="score-label">Draws</div>
        <div class="score-value score-draws">{d}</div>
      </div>
      <div class="score-divider"></div>
      <div class="score-item">
        <div class="score-label">Losses</div>
        <div class="score-value score-loss">{l}</div>
      </div>
      <div class="score-divider"></div>
      <div class="score-item">
        <div class="score-label">Win Rate</div>
        <div class="score-value score-wins">{int(w/total*100)}%</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>⚔️ Choose Your Weapon</div>", unsafe_allow_html=True)

    # Choice buttons
    c1, c2, c3 = st.columns(3)
    chosen = None
    with c1:
        if st.button("🪨\n\nROCK", use_container_width=True):
            chosen = "ROCK"
    with c2:
        if st.button("📄\n\nPAPER", use_container_width=True):
            chosen = "PAPER"
    with c3:
        if st.button("✂️\n\nSCISSORS", use_container_width=True):
            chosen = "SCISSORS"

    if chosen:
        comp = random.choice(["ROCK", "PAPER", "SCISSORS"])
        if chosen == comp:
            result, css = "IT'S A DRAW! 🤝", "result-draw"
            st.session_state.rps_draws += 1
        elif RPS_BEATS[chosen] == comp:
            result, css = "🏆 YOU WIN!", "result-win"
            st.session_state.rps_wins += 1
        else:
            result, css = "💀 COMPUTER WINS!", "result-lose"
            st.session_state.rps_losses += 1

        st.session_state.rps_last = (chosen, comp, result, css)
        st.session_state.rps_history.append((chosen, comp, result))
        st.rerun()

    # Battle arena — last result
    if st.session_state.rps_last:
        p, c, result, css = st.session_state.rps_last
        st.markdown(f"""
        <div class="battle-arena">
          <div class="fighter">
            <div class="fighter-label">You</div>
            <div class="fighter-icon">{RPS_ICONS[p]}</div>
          </div>
          <div class="vs-badge">VS</div>
          <div class="fighter">
            <div class="fighter-label">Computer</div>
            <div class="fighter-icon">{RPS_ICONS[c]}</div>
          </div>
        </div>
        <div class="result-banner {css}">{result}</div>
        """, unsafe_allow_html=True)

    # History
    if st.session_state.rps_history:
        st.markdown("<div class='section-header' style='margin-top:1.5rem'>📋 Battle Log</div>", unsafe_allow_html=True)
        st.markdown("<div style='background:#ffffff05;border:1px solid #3a6fff22;border-radius:12px;padding:0.5rem'>", unsafe_allow_html=True)
        for ph, ch, res in reversed(st.session_state.rps_history[-8:]):
            if "WIN" in res and "COMPUTER" not in res:
                color, icon = "#34d399", "🏆"
            elif "DRAW" in res:
                color, icon = "#fbbf24", "🤝"
            else:
                color, icon = "#f87171", "💀"
            st.markdown(f"""
            <div class="history-item">
              <span>{RPS_ICONS[ph]} vs {RPS_ICONS[ch]}</span>
              <span style="color:{color};font-weight:700">{icon} {res.replace('!','').strip()}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Reset + Menu
    st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    with r1:
        if st.button("🔄  RESET SCORE", use_container_width=True):
            st.session_state.rps_wins = 0
            st.session_state.rps_losses = 0
            st.session_state.rps_draws = 0
            st.session_state.rps_history = []
            st.session_state.rps_last = None
            st.rerun()
    with r2:
        if st.button("🏠  MAIN MENU", use_container_width=True):
            st.session_state.game = None
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ── No game selected ──────────────────────────────────────────────────────────
else:
    st.markdown("""
    <div style="text-align:center;padding:3rem 1rem;color:#334155">
      <div style="font-size:3rem;margin-bottom:1rem">🎮</div>
      <div style="font-family:'Orbitron',monospace;font-size:1rem;letter-spacing:0.2em">
        SELECT A GAME ABOVE TO BEGIN
      </div>
    </div>
    """, unsafe_allow_html=True)