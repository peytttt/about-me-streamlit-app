import streamlit as st

st.title("MY BLOG")

st.markdown(
    """
    <style>
    body {
        background-color: #f0f4f8;  /* Light background color */
        color: #2c6b5d;  /* Sage green text */
        font-family: 'Times New Roman', Times, serif;
    }
    .main {
        background-color: #ffffff;  /* White background for content area */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3, h4 {
        color: #2c6b5d;  /* Sage green for headers */
        font-family: 'Times New Roman', Times, serif;
    }
    p, li {
        font-family: 'Times New Roman', Times, serif;
        font-size: 18px;
        line-height: 1.6;
    }
    footer {
        text-align: center;
        font-size: 14px;
        color: #7f8c8d;
        margin-top: 50px;
        font-family: 'Times New Roman', Times, serif;
    }
    .stImage {
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image(
    "https://raw.githubusercontent.com/peytttt/about-me-streamlit-app/main/images/me.jpg", 
    use_container_width=True
)

st.write("**NAME:** Jollie Faith S. Jimenez")
st.write("**BIRTHDAY:** July 15, 2005")
st.write("**COURSE:** Bachelor of Science in Computer Engineering (BSCPE)")
st.write("**SECTION:** 1B")

st.subheader("Hi there!")
st.write("My name is Jollie Faith S. Jimenez, a 1st-year Computer Engineering student at SNSU.")

st.header("About Me")
st.write("""
Hello, I'm Jollie Faith S. Jimenez, 19 years old. I was born in San Fernando, Pampanga, and I'm proud to be a Kapampangan, 
even though I don't speak the language. We moved to Surigao City when I was 2 years old, and I’ve lived here since. 

I have 2 cats named Tobby and Ginger. Tobby is inspired by Dobby, the house-elf from Harry Potter, while Ginger got his name 
because of his orange fur. My family is religious, and I’ve served the Catholic Church since I was a little kid. 

I also adore stuffed toys and can’t sleep without them. I’ve had one since childhood, which still brings comfort and assurance.
""")

st.header("Hobbies and Interests")
st.write("""
- Watching movies (especially Harry Potter).
- Cooking and exploring different dishes.
- Listening to music.
- Watching documentaries about animals, history, and real-life investigation cases.
""")

st.header("Certificates")

st.subheader("My Certificates")
certificates = [
    "Participation Certificate - SHS Expo 2023-2024"
]

if certificates:
    for cert in certificates:
        st.write(f"- {cert}")
else:
    st.write("No certificates available.")

st.markdown("<footer>© 2024 Jollie Faith S. Jimenez</footer>", unsafe_allow_html=True)
