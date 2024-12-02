import streamlit as st

# Set the title
st.title("About Jollie Faith S. Jimenez")

# Add image from GitHub
st.image("https://raw.githubusercontent.com/peytttt/about-me-streamlit-app/images/me.jpg", caption="Jollie Faith S. Jimenez", use_container_width=True)


# Description
st.subheader("Hi there!")
st.write("My name is Jollie Faith S. Jimenez, a 1st-year Computer Engineering student at SNSU.")

# About Me
st.header("About Me")
st.write("""
Hello, I'm Jollie Faith S. Jimenez, 19 years old. I was born in San Fernando, Pampanga, and I'm proud to be a Kapampangan 
even though I don't speak the language. When I was young, we moved to Surigao City, and since then, we’ve been living here. 

I have two siblings, and as the eldest, our family calls us "Tres Marias" since we are all girls. My mother has been raising us 
alone for quite a long time now, as our father left us around 11 years ago. 

In 2019, after the school year 2018-2019 ended, I went to Pampanga to live with my father and continue my junior high there. 
Unfortunately, before the school year 2019-2020 could end, the COVID-19 pandemic hit, and the school year ended early. During 
the 2020-2021 school year, I was in Grade 9, completing modules at home at that time I was still in Pampanga. On June 28, 2020, I managed to return to Surigao. 

Returning to Surigao was challenging due to strict travel requirements before boarding a plane. I completed Grade 10 at the 
same school in Pampanga but via online classes. Unfortunately, I couldn't attend my graduation due to the circumstances.

In 2021, I had a fresh start by enrolling in STI Surigao. Initially, having face-to-face classes was difficult because I 
struggled with anxiety, especially in crowded places. I worried most about reporting tasks, as presenting in front of people 
made me stutter and gave me shaky hands. However, thanks to those experiences, I’ve started to improve, and I continue working 
on it. 

In short, I am a shy person, but I am also independent when it comes to getting things done. I’m determined to grow and improve 
every day.
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
st.markdown("<footer style='text-align:center;'>© 2024 Jollie Faith S. Jimenez</footer>", unsafe_allow_html=True)
