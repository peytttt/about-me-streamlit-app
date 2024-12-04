import streamlit as st

# Set the title
st.title("MY BLOG")

# Customizing the page's background color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f0f4f8;  # Light background color
    }
    .main {
        background-color: #ffffff;  # White background for content area
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        color: #2c6b5d;  # Sage green color for title
        font-family: 'Arial', sans-serif;
    }
    h2 {
        color: #5a6e49;  # Olive green for headers
    }
    h3, h4 {
        color: #34495e;
    }
    p {
        font-size: 18px;
        color: #2c6b5d;  # Sage green text
        line-height: 1.6;
        font-family: 'Arial', sans-serif;
    }
    footer {
        text-align: center;
        font-size: 14px;
        color: #7f8c8d;
    }
    .stImage {
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add image from GitHub with specified size
st.image("https://raw.githubusercontent.com/peytttt/about-me-streamlit-app/main/images/me.jpg", 
         width=400,  # Adjust the width and height as needed
         use_container_width=True)

# Personal Details text after the photo
st.write("**NAME:** Jollie Faith S. Jimenez")
st.write("**BIRTHDAY:** July 15, 2005")
st.write("**COURSE:** BS Computer Engineering (BSCPE)")
st.write("**SECTION:** 1B")

# Description
st.subheader("Hi there!")
st.write("My name is Jollie Faith S. Jimenez, a 1st-year Computer Engineering student at SNSU.")

# About Me
st.header("About Me")
st.write("""
Hello, I'm Jollie Faith S. Jimenez, 19 years old. I was born in San Fernando, Pampanga, and I'm proud to be a Kapampangan 
even though I don't speak the language. We moved here in Surigao City when I was 2 years old, and since then, we’ve been living here. 

I have 2 cats named Tobby and Ginger. I named my cat Tobby after Dobby, the house-elf from Harry Potter, and I named my other cat Ginger because his color is orange. 

My family is religious, and since I was a little kid, I have been serving the church up to this day. We are Catholics, and it has been a significant part of my life.
""")

# Hobbies and Interests (bulleted list)
st.header("Hobbies and Interests")
st.write("""
- I like watching movies (especially Harry Potter).
- I like cooking foods and exploring different dishes.
- I like listening to music.
- I also like watching documentaries about animals, history, and real-life investigation cases.
""")

# Educational Attainment (bulleted list)
st.header("Educational Attainment")
st.write("""
- **Elementary School:** Surigao West Central Elementary School (2012-2017)
- **Junior High School:** Pampanga High School (2019-2022)
- **Senior High School:** STI College Surigao (2022-2024)
- **Currently pursuing:** BS in Computer Engineering at SNSU (1st year)
""")

# Certificates with Buttons
st.header("Certificates")

# Initialize session state for certificates if not already set
if "certificates" not in st.session_state:
    st.session_state.certificates = [
        "Certificate of Completion - ICT Strand, STI College Surigao",
        "Participation Certificate - Web Development Workshop",
        "Recognition for Outstanding Performance in Programming Logic"
    ]

# Display existing certificates
st.subheader("My Certificates")
if st.session_state.certificates:
    for cert in st.session_state.certificates:
        st.write(f"- {cert}")
else:
    st.write("No certificates available.")

# Add a new certificate
st.subheader("Add a Certificate")
new_certificate = st.text_input("Enter a new certificate:")
if st.button("Save Certificate"):
    if new_certificate:
        st.session_state.certificates.append(new_certificate)
        st.success(f"Certificate '{new_certificate}' added successfully!")
    else:
        st.error("Please enter a certificate name.")

# Delete an existing certificate
st.subheader("Delete a Certificate")
if st.session_state.certificates:
    certificate_to_delete = st.selectbox("Select a certificate to delete:", st.session_state.certificates)
    if st.button("Delete Certificate"):
        st.session_state.certificates.remove(certificate_to_delete)
        st.warning(f"Certificate '{certificate_to_delete}' deleted successfully!")

# Edit an existing certificate
st.subheader("Edit a Certificate")
if st.session_state.certificates:
    certificate_to_edit = st.selectbox("Select a certificate to edit:", st.session_state.certificates)
    updated_certificate = st.text_input("Enter the updated certificate:")
    if st.button("Edit Certificate"):
        if updated_certificate:
            index = st.session_state.certificates.index(certificate_to_edit)
            st.session_state.certificates[index] = updated_certificate
            st.success(f"Certificate updated to '{updated_certificate}'!")
        else:
            st.error("Please enter the updated certificate name.")

# Footer
st.markdown("<footer>© 2024 Jollie Faith S. Jimenez</footer>", unsafe_allow_html=True)
