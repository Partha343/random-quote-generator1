import streamlit as st
import pandas as pd
import random
import time

# Load external CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Load quotes from CSV
quotes_df = pd.read_csv("quotes.csv")
quotes_list = quotes_df['quote'].dropna().tolist()

# Function to get a random quote
def get_new_quote():
    return random.choice(quotes_list)

# Title
st.markdown('<div class="title">🌟 Random Quote Generator 🌟</div>', unsafe_allow_html=True)

# Initialize session state
if "quote" not in st.session_state:
    st.session_state.quote = get_new_quote()

# Display the current quote
st.markdown(f'<div class="quote-box">"{st.session_state.quote}"</div>', unsafe_allow_html=True)

# Countdown timer with animation
countdown = 10  # seconds
progress_bar = st.progress(0)
status = st.empty()

for remaining in range(countdown, 0, -1):
    status.text(f"Next quote in {remaining} seconds...")
    progress_bar.progress((countdown - remaining + 1) / countdown)
    time.sleep(1)

# Update the quote and rerun
st.session_state.quote = get_new_quote()
st.rerun()

