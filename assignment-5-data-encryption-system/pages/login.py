import streamlit as st

st.title("🔐 Reauthorization Required")

st.info("You have been locked out after 3 failed decryption attempts.")
st.write("Please confirm to reauthorize and try again.")

username = st.text_input("Username", key="login_username")
password = st.text_input("Password", type="password", key="login_password")

if st.button("login"):
    if username and password:
        #Simple placeholder auth logic (replace with real auth if needed)
        st.session_state.failed_attempts=0
        st.success("Reauthorized successfully! Redirecting to retrieval page...")

        #optional delay before redirect
        st.rerun()
    else:
        st.error("Please enter  both username and password")