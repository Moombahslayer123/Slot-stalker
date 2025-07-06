import streamlit as st
import pandas as pd
import random
from scraper import get_betway_slots

st.set_page_config(page_title="🎰 Slot Stalker 9000", layout="wide")
st.title("🎰 Slot Stalker 9000")

st.markdown("Real slots, scraped live off Betway. Let’s find out who’s hiding the jackpots...")

# Scrape slot names
with st.spinner("Scraping Betway..."):
    slot_names = get_betway_slots()

if not slot_names:
    st.error("Couldn’t fetch slots. Betway probably saw us coming. Try again later.")
else:
    slots = [{"name": name, "rtp": round(random.uniform(88, 97), 2), "volatility": random.choice(["Low", "Medium", "High"])} for name in slot_names]

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
    st.success(f"💰 Thulz's Slot of the Moment: **{best_slot['Name']}** — RTP: {best_slot['RTP (%)']}%, Risk: {best_slot['💸 Risk Level']}")