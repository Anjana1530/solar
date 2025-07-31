import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Add root folder to import calculator
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from roi.calculator import calculate_roi

def run_dashboard():
    st.title("📊 Solar vs Grid Energy Tracker")

    try:
        df = pd.read_csv('data/mock_readings.csv')
        fig = px.line(df, x='date', y=['solar_kwh', 'consumption_kwh'], markers=True)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error loading data: {e}")

    st.subheader("💹 ROI Calculator")
    capex = st.number_input("Installation Cost (₹)", min_value=0.0)
    ann_gen = st.number_input("Annual Solar Energy (kWh)", min_value=0.0)
    tariff = st.number_input("Electricity Rate (₹/kWh)", min_value=0.0)

    if st.button("Calculate ROI"):
        if capex > 0 and ann_gen > 0 and tariff > 0:
            years, roi = calculate_roi(capex, ann_gen, tariff)
            st.success(f"⏳ Payback Period: {years:.2f} years")
            st.info(f"📈 ROI: {roi:.2f}%")
        else:
            st.warning("Please enter valid values for all fields.")
