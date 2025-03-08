import streamlit as st

st.title("🌍 Unit Convertor App by Abdul Qayoom")
st.markdown("### Convert Length, Weight, Time, Temperature & Speed instantly")
st.write("Welcom! Select a category, enter a value and get the converted results in realtime")

category = st.selectbox("Choose a Category", ["Length", "Weight", "Time", "Temperature", "Speed"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Centimeters to Inches":
            return value * 0.393701
        elif unit == "Inches to Centimeters":
            return value / 0.393701
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Ounces":
            return value * 0.035274
        elif unit == "Ounces to Grams":
            return value / 0.035274
        elif unit == "Tonnes to Pounds":
            return value * 2204.62
        elif unit == "Pounds to Tonnes":
            return value / 2204.62

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Days to Weeks":
            return value / 7
        elif unit == "Weeks to Days":
            return value * 7
        elif unit == "Months to Years":
            return value / 12
        elif unit == "Years to Months":
            return value * 12
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
    elif category == "Speed":
        if unit == "Kilometers per hour to Miles per hour":
            return value * 0.621371
        elif unit == "Miles per hour to Kilometers per hour":
            return value / 0.621371
        elif unit == "Meters per second to Kilometers per hour":
            return value * 3.6
        elif unit == "Kilometers per hour to Meters per second":
            return value / 3.6

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeters"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams", "Tonnes to Pounds", "Pounds to Tonnes"])
elif category == "Time":
    unit = st.selectbox("⌚ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours", "Days to Weeks", "Weeks to Days", "Months to Years", "Years to Months"])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])
elif category == "Speed":
    unit = st.selectbox("🚗 Select Conversion", ["Kilometers per hour to Miles per hour", "Miles per hour to Kilometers per hour", "Meters per second to Kilometers per hour", "Kilometers per hour to Meters per second"])


value = st.number_input("Enter the value to convert")

if st.button("Convert"):
     result = convert_units(category, value, unit)
     st.success(f"The result is {result:.2f}")
    