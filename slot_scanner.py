import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

st.set_page_config(page_title="🎰 Slot Stalker 9000", layout="wide")

st.title("🎰 Slot Stalker 9000")
st.markdown("Know which slot is about to pop. Built for degenerates by a slightly smarter degenerate.")

slots = [
    {"name": "Big Bass Bonanza", "rtp": 96.71, "volatility": "High"},
    {"name": "Sweet Bonanza", "rtp": 96.51, "volatility": "Medium-High"},
    {"name": "Gates of Olympus", "rtp": 96.50, "volatility": "High"},
    {"name": "Book of Dead", "rtp": 96.21, "volatility": "High"},
    {"name": "Mega Moolah", "rtp": 88.12, "volatility": "Insane"},
]

def simulate_slot_status(slot):
    heat_score = round(random.uniform(0.1, 1.0), 2)
    return {
        "Name": slot["name"],
        "RTP (%)": slot["rtp"],
        "Volatility": slot["volatility"],
        "🔥 Send It Score": heat_score,
        "💸 Risk Level": "High" if heat_score < 0.3 else "Moderate" if heat_score < 0.7 else "Low",
    }

scanned_slots = [simulate_slot_status(slot) for slot in slots]

df = pd.DataFrame(scanned_slots)
df = df.sort_values("🔥 Send It Score", ascending=False)

st.dataframe(df, use_container_width=True)

best_slot = df.iloc[0]
st.success(f"💰 **Thulz's Slot of the Moment**: {best_slot['Name']} — RTP: {best_slot['RTP (%)']}%, Risk: {best_slot['💸 Risk Level']}")

st.caption("🔍 Real scraping & AI analysis coming in Phase 2. This is just foreplay.")