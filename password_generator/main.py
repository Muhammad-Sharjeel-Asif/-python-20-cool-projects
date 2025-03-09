import streamlit as st
import string
import secrets

def password_generator(length, digits, special_char):
    characters = string.ascii_letters

    if digits:
        characters += string.digits

    if special_char:
        characters += string.punctuation

    return ''.join(secrets.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select the length of the password", 8, 32, 12)
digits = st.checkbox("Select to include digits")
special_characters = st.checkbox("Select to include special characters")


if st.button("Generate"):
    password = password_generator(length, digits, special_characters)
    st.success(f"Your password is: **{password}**")
