import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata"
    ]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Time Zone", TIME_ZONES, default=["UTC", "Asia/Karachi"])

for tz in selected_timezone:
    current_timezone = datetime.now(ZoneInfo(tz)).strftime(("%Y-%m-%d %I %H:%M:%S %p"))
    st.write(f"The current time in **{tz}** is: {current_timezone}")

st.divider()

st.subheader("Convert Time Zone")
current_time = st.time_input("Current Time", value=datetime.now().time())
from_time_zone = st.selectbox("Select Time Zone", TIME_ZONES, index=0)
to_time_zone = st.selectbox("Select Time Zone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(to_time_zone))
    converted_time = dt.astimezone(ZoneInfo(to_time_zone)).strftime(("%Y-%m-%d %I %H:%M:%S %p"))

    st.success(f"The time in **{to_time_zone}** is: {converted_time}")