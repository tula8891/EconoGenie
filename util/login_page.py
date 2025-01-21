# Login page function with a single column layout



def login_page(st, email_user, password_user):
    """Render the login page of the Streamlit application."""

    

    # Center-aligned container
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("Login")
        st.write("Welcome back! Please log in to continue.")

        # Login form
        with st.form("login_form", clear_on_submit=True):
            email = st.text_input("Email", placeholder="user@example.com")
            st.write("Email: user@example.com")
            password = st.text_input(
                "Password", type="password", placeholder="password123"
            )
            st.write("Password: password123")

            # Full-width login button
            if st.form_submit_button("Login", use_container_width=True):
                if email == email_user and password == password_user:
                    st.session_state.logged_in = True
                    st.session_state.username = "Demo User"
                    st.session_state.email = email
                    st.session_state.page = "main"
                    st.success("Your credentials are valid! Please click the login button again to proceed")
                else:
                    st.error("Invalid credentials. Please try again.")

        # Sign up link
        st.write("Don't have an account?")
        
        if st.button("Sign Up", use_container_width=True):
            st.session_state.page = "signup"
        st.markdown(
            """
            <style>
            .custom-text {
                position: absolute;
                top: 10px;
                left: 10px;
                font-size: 14px;
                color: black;
            }
            </style>
            <div class="custom-text">
                <strong>Developed and Designed By:</strong><br>
                Parmanand Sahu - <a href="https://parmanandsahu.com/" target="_blank">https://parmanandsahu.com/</a><br>
                Tula Ram Sahu - <a href="https://in.linkedin.com/in/tula-ram-sahu-003226104" target="_blank">https://in.linkedin.com/in/tula-ram-sahu-003226104</a>
                </div>
                """, unsafe_allow_html=True)
            
            