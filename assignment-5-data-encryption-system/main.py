# main.py

import streamlit as st

st.set_page_config(page_title="Secure Data App", page_icon="🛡️")

st.title("🛡️ Secure Data Encryption System")
st.write("""
Welcome to your in-browser encryption system built with **Streamlit**!  
Here, you can safely store sensitive data using encryption and retrieve it securely using a passkey.
""")

# Show failed attempt status
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

st.info(f"Failed Decryption Attempts: {st.session_state.failed_attempts}/3")

st.subheader("🔗 Navigate")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Insert Data"):
        st.switch_page("pages/insert_data.py")

with col2:
    if st.button("🔓 Retrieve Data"):
        st.switch_page("pages/retrieve_data.py")

with col3:
    if st.button("🔐 Login Page"):
        st.switch_page("pages/login.py")

