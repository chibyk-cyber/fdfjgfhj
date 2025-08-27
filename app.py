import streamlit as st
import pyrebase

# Firebase configuration
firebaseConfig = {
  "apiKey": "YOUR_API_KEY",
  "authDomain": "YOUR_PROJECT.firebaseapp.com",
  "projectId": "YOUR_PROJECT_ID",
  "storageBucket": "YOUR_PROJECT.appspot.com",
  "messagingSenderId": "YOUR_SENDER_ID",
  "appId": "YOUR_APP_ID"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

# Authentication
st.title("🛒 Welcome to My Shop")

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Sign Up":
    st.subheader("Create New Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("✅ Account created successfully! Please log in.")
        except Exception as e:
            st.error(e)

elif choice == "Login":
    st.subheader("Login to Your Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.logged_in = True
            st.session_state.user = user
            st.success("✅ Logged in successfully!")
        except Exception as e:
            st.error("❌ Invalid credentials")

# If logged in, show shop
if st.session_state.logged_in:
    st.success(f"Welcome {st.session_state.user['email']} 👋")
    
    # Example shop content
    st.header("🛍️ Products")
    st.write("Here you will show clothes, generators, etc with Paystack links")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.experimental_rerun()
