import streamlit as st
import sqlite3 
import hashlib
import main  # Import the main module

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

def main():
    st.title("Sign in")
    menu = ["Login","SignUp"]
    choice = st.selectbox("Menu", menu)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    if choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        
        if st.button("Login"):
            c.execute('SELECT * FROM userstable WHERE username = ?', (username,))
            data = c.fetchone()
            if data:
                if check_hashes(password, data[1]):
                    st.success("Logged In as {}".format(username))
                    st.write("Redirecting to the main page...")
                    # Run the main Streamlit application directly
                    main.main()
                else:
                    st.warning("Incorrect Password")
            else:
                st.warning("Username not found")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        
        if st.button("Signup"):
            hashed_pswd = make_hashes(new_password)
            c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (new_user, hashed_pswd))
            conn.commit()
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")

    conn.close()

if __name__ == '__main__':
    main()
