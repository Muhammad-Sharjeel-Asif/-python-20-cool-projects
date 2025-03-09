import streamlit as st

def unit_converter(value, from_unit, to_unit):

    conversions = {
        "meter_kilometer":0.001,
        "kilometer_meter":1000,
        
        "gram_kilogram":0.001,
        "kilogram_gram":1000,

        "hour_second":3600,
        "second_hour":1/3600,
        "minute_hour":1/60,
        "hour_minute":60,
        "second_minute":1/60,
        "minute_second":60,
    }

    key = f"{from_unit}_{to_unit}"

    if key in conversions:
        conversion = conversions[key]
        return conversion * value
    else:
        return "Unsupported units"

st.title("Unit Converter App")

value = st.number_input("Enter a value", min_value=1.0, step=1.0)
from_unit = st.selectbox("Select from unit", ["meter", "kilometer", "gram", "kilogram", "hour", "second", "minute"])
to_unit = st.selectbox("Select from unit", ["kilometer", "meter", "kilogram", "gram", "second", "minute", "hour"])

if st.button("Convert"):
    result = unit_converter(value, from_unit, to_unit)
    st.success(f"The value is {result} {to_unit}")