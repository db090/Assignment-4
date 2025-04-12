import streamlit as st
from crypto.encryptor import encrypt_message
from crypto.hasher import hash_passkey
from storage.memory_store import store_data

st.title("📝 Insert New Encrypted Data")

# Step 1: Get user input
data_key=st.text_input("Enter a unique key for this data (e.g. username or label)")
user_text=st.text_area("Enter the text to encrypt")
passkey=st.text_input("Enter a passkey (will be used to decrypt later)" ,type="password")

# Step 2: On Submit
if  st.button("Encrypt & Save"):
    if not data_key or not user_text or not passkey:
        st.warning("Please Fill out all fields.")
    else:
        encrypted=encrypt_message(user_text,passkey)
        hashed=hash_passkey(passkey)

        store_data(data_key,encrypted,hashed)
        st.success(f"Data encrypted and stored successfully under key: '{data_key}'")