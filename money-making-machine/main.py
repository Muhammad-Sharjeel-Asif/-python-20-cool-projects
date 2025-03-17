import streamlit as st
import random
import time
import requests

def money_generator():
    return random.randint(1, 1000)

st.title("Money Making Machine")

st.subheader("Instant Cash Generator")

if st.button("Generate Money"):
    st.write("Generating money...")
    amount = money_generator()
    time.sleep(2)
    st.success(f"You have generated ${amount}!")

def get_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?apikey=123456789")
        if response.status_code == 200:
            side_hustle = response.json()
            return side_hustle["side_hustles"]
        else:
            return ("Freelancing")
        
    except:
        return ("Something went wrong")
    
if st.button("Generate Side Hustle"):
    idea = get_side_hustles()
    st.write("Generating side hustle idea...")
    time.sleep(2)
    st.success(idea)

def get_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?apikey=123456789")
        if response.status_code == 200:
            money_quotes = response.json()
            return money_quotes["money_quotes"]
        else:
            return ("Money is evil...")
    except:
        return ("No money quotes available")

if st.button("Generate money making motivations"):
    st.write("Generating money making motivations...")
    time.sleep(2)
    quotes = get_money_quotes()
    st.success(quotes)