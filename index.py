import streamlit as st

# Set page configuration at the very top
st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="centered")

# Apply custom styles
st.markdown(
    """
    <style>
        /* Set background color and text color */
        .stApp {
            background-color: black;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: white !important;
        }

        /* Style input fields */
        .stTextInput, .stSelectbox, .stNumberInput {
            background-color: #222 !important;
            color: white !important;
            border-color: white !important;
        }

        /* Style Convert button */
        div.stButton > button {
            background-color: white !important;  /* White button */
            color: black !important;  /* Black text */
            border-radius: 5px;
            border: 2px solid white !important;
            padding: 8px 16px;
            font-weight: bold;
            transition: 0.3s ease-in-out;
        }
        div.stButton > button:hover {
            background-color: #ddd !important; /* Light gray on hover */
        }

        /* Make dropdown arrows show pointer cursor */
        div[data-baseweb="select"] span {
            cursor: pointer !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔢 Multi-Unit Converter")
st.write("Easily convert between different units of measurement.")

# Conversion Factors Dictionary
conversion_factors = {
    "Distance": {"Meters": 1, "Kilometers": 1000, "Feet": 0.3048, "Miles": 1609.34},
    "Weight": {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495},
    "Pressure": {"Pascals": 1, "Hectopascals": 100, "Kilopascals": 1000, "Bar": 100000},
    "Energy": {"Joules": 1, "Kilojoules": 1000, "Calories": 4.184, "Kilocalories": 4184},
    "Time": {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400},
}

# Conversion Function
def convert_units(category, from_unit, to_unit, value):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        return value  # Same unit case

    return value * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure", "Energy", "Time"])

# Get unit options correctly
unit_options = (
    ["Celsius", "Fahrenheit"] 
    if category == "Temperature" 
    else list(conversion_factors[category].keys())
)

with st.form("conversion_form"):
    from_unit = st.selectbox("From", unit_options)
    to_unit = st.selectbox("To", unit_options)
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
    submit = st.form_submit_button("Convert")

if submit and value >= 0:
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
