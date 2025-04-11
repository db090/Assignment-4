import streamlit as st

st.title("🏋️‍♂️ BMI Calculator")

# User inputs
height = st.number_input("Enter your height (in meters):", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0, format="%.2f")


if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader(f"📊 Your BMI is: {bmi:.2f}")


    if bmi < 18.5:
        st.info("🔎 You are underweight.")
    elif 18.5 <= bmi < 25:
        st.success("✅ You have a normal weight.")
    elif 25 <= bmi < 30:
        st.warning("⚠️ You are overweight.")
    else:
        st.error("🚨 You are obese.")
