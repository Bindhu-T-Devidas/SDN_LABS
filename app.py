import os
from datetime import datetime
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DevOps Lab: Streamlit", page_icon="✅", layout="centered")

st.title("👋 Hello from Streamlit")
st.write("Tiny app for learning Git → Docker → Kubernetes.")

env = os.getenv("APP_ENV", "local")
st.info(f"Environment: **{env}**")

if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2 = st.columns(2)
if col1.button("➕ Increment"):
    st.session_state.count += 1
if col2.button("🔁 Reset"):
    st.session_state.count = 0

st.metric("Click Counter", st.session_state.count)

st.subheader("Sample Data")
df = pd.DataFrame({"item": ["A", "B", "C"], "value": [1, 2, 3]})
st.dataframe(df, use_container_width=True)

st.caption(f"Time now: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")