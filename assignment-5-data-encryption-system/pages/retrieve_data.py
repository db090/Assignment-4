import streamlit as st
from storage.memory_store import get_all_keys,retrieve_data
from crypto.hasher import verfiy_passkey
from  crypto.encryptor import decrypt_message

st.title("🔓 Retrieve Encrypted Data")

# Initialize failed attempts

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts=0

if st.session_state.failed_attempts >= 3:
    st.warning("Too many failed attempts. Please reauthorize")
    st.switch_page("pages/login.py")
    st.stop()

# Step 1: Choose a key
available_keys=get_all_keys()
selected_key=st.selectbox("Select a key",available_keys)

# Step 2: Ask for passkey
passkey=st.text_input("Enter passkey to decrypt", type="password")

if st.button("Decrypt"):
    record=retrieve_data(selected_key)

    if not record:
        st.error("No Data Found for this key.")
    else:
        stored_hash=record["passkey"]
        if verfiy_passkey(passkey,stored_hash):
            decrypted=decrypt_message(record["encrypted_text"],passkey)
            if decrypted:
                st.success("✅ Decrypted Message")
                st.code(decrypted,language="text")
                st.session_state.failed_attempts = 0 #reset
            else:
                st.error("Decryption Failed.")
        else:
            st.session_state.failed_attempts += 1
            remaining=3-st.session_state.failed_attempts
            st.error(f"Incorrect passkey. Attempts remaining: {remaining}")