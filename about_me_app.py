import streamlit as st

# Set the title
st.title("About Jollie Faith S. Jimenez")

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
        color: #2c3e50;  # Dark text for title
        font-family: 'Arial', sans-serif;
    }
    h2 {
        color: #2980b9;  # Blue color for headers
    }
    h3, h4 {
        color: #34495e;
    }
    p {
        font-size: 18px;
        color: #2c3e50;
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
         caption="Jollie Faith S. Jimenez", 
         width=400,  # Adjust the width and height as needed
         use_container_width=True)

# Description
st.subheader("Hi there!")
st.write("My name is Jollie Faith S. Jimenez, a 1st-year Computer Engineering student at SNSU.")

# About Me
st.header("About Me")
st.write("""
Hello, I'm Jollie Faith S. Jimenez, 19 years old. I was born in San Fernando, Pampanga, and I'm proud to be a Kapampangan 
even though I don't speak the language. We moved here in Surigao City when I was 2 years old, and since then, we’ve been living here. 

I have 2 cats named Tobby and Ginger. I named my cat Tobby after Dobby, the house-elf from Harry Potter, and I named my other cat Ginger because his color is orange. 

My family is religious, so since I was a little kid, I have been serving the church. We are Catholics, and it has been a big part of my life.
""")

# Hobbies
st.header("Hobbies and Interests")
hobbies = [
    "I like watching movies (especially Harry Potter).",
    "I like cooking foods and exploring different dishes.",
    "I like listening to music.",
    "I also like watching documentaries about animals, history, and real-life investigation cases."
]
st.write(hobbies)

# Educational Attainment
st.header("Educational Attainment")
educational_attainment = [
    "Junior High School: Completed at Pampanga (2019-2020, partially online)",
    "Senior High School: STI College Surigao, ICT Strand (Graduated in 2024)",
    "Currently pursuing: BS in Computer Engineering at SNSU (1st year)"
]
st.write(educational_attainment)

# Certificates
st.header("Certificates")
certificates = [
    "Certificate of Completion - ICT Strand, STI College Surigao",
    "Participation Certificate - Web Development Workshop",
    "Recognition for Outstanding Performance in Programming Logic"
]
st.write(certificates)

# Footer
st.markdown("<footer>© 2024 Jollie Faith S. Jimenez</footer>", unsafe_allow_html=True)
