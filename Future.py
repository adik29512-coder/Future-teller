import streamlit as st
import sys
from io import StringIO

# --- 1. THE BACKGROUND & UI SETUP ---
st.set_page_config(page_title="Numerology Destiny", page_icon="✨")

# Custom CSS for a professional dark background
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #e94560;
    }
    .stTextInput>div>div>input {
        background-color: #1a1a2e;
        color: #48dbfb;
        border: 1px solid #e94560;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 Numerology Personality Checker")
st.write("Enter your birth details below to see your profile.")

# We create the input field for the user
user_dob = st.text_input("Enter your Date of Birth (DDMMYYYY):", placeholder="Example: 15081947")

if st.button("Check Personality"):
    if user_dob:
        # This captures your 'print' statements so they show up on the web page
        output_capture = StringIO()
        sys.stdout = output_capture
       
        # We assign your variable 'dob' to the input from the website
        dob = user_dob

        # ==========================================================
        # START OF YOUR UNCHANGED CODE
        # ==========================================================
        def single_digit(n):
            while n > 9:
                total = 0
                for digit in str(n):
                    total += int(digit)
                n = total
            return n
        # Input
        # (Note: 'dob' is already defined above from the text_input)
        # Validation
        if len(dob) != 8 or not dob.isdigit():
            print("Please enter valid DOB in DDMMYYYY format.")
        else:
            # Add digits
            total = 0
            for digit in dob:
                total += int(digit)
            # Final Number
            number = single_digit(total)
            print("\n===================================")
            print(" YOUR BIRTH NUMBER IS:", number)
            print("===================================\n")
            # Full Details
            if number == 1:
                print("Number 1 Personality")
                print("You are a natural leader and independent person.")
                print("You have confidence, courage, and strong willpower.")
                print("You like taking charge and making decisions.")
                print("You do not depend on others easily.")
                print("You want success and respect in life.")
                print("Strengths: Leadership, confidence, originality.")
                print("Weaknesses: Can be stubborn or impatient.")
                print("Best Careers: Business, management, politics, entrepreneurship.")
                print("Lucky Colors: Gold, Yellow, Orange.")
                print("Lucky Days: Sunday, Monday.")
            elif number == 2:
                print("Number 2 Personality")
                print("You are calm, cooperative, and sensitive.")
                print("You understand emotions well.")
                print("You like peace and avoid conflict.")
                print("You work well in teams.")
                print("You care deeply for others.")
                print("Strengths: Patience, kindness, diplomacy.")
                print("Weaknesses: Overthinking, emotional mood changes.")
                print("Best Careers: Counseling, teaching, teamwork jobs.")
                print("Lucky Colors: White, Silver, Light Blue.")
                print("Lucky Days: Monday, Friday.")
            elif number == 3:
                print("Number 3 Personality")
                print("You are creative and expressive.")
                print("You have imagination and many ideas.")
                print("You enjoy talking, writing, art or music.")
                print("You spread joy around others.")
                print("You like social life and fun.")
                print("Strengths: Creativity, communication, charm.")
                print("Weaknesses: Distraction, laziness sometimes.")
                print("Best Careers: Artist, writer, media, acting.")
                print("Lucky Colors: Pink, Purple, Yellow.")
                print("Lucky Days: Thursday, Friday.")
            elif number == 4:
                print("Number 4 Personality")
                print("You are hardworking and practical.")
                print("You believe in discipline and rules.")
                print("You build life step by step.")
                print("You are honest and dependable.")
                print("You like stability and planning.")
                print("Strengths: Discipline, honesty, hard work.")
                print("Weaknesses: Rigid thinking, stress.")
                print("Best Careers: Engineering, banking, administration.")
                print("Lucky Colors: Blue, Grey, Brown.")
                print("Lucky Days: Saturday, Sunday.")
            elif number == 5:
                print("Number 5 Personality")
                print("You love freedom and adventure.")
                print("You enjoy travel and new experiences.")
                print("You dislike boring routines.")
                print("You are energetic and curious.")
                print("You adapt quickly to change.")
                print("Strengths: Smartness, flexibility, courage.")
                print("Weaknesses: Restlessness, impatience.")
                print("Best Careers: Travel, marketing, sales, media.")
                print("Lucky Colors: Green, White.")
                print("Lucky Days: Wednesday, Friday.")
            elif number == 6:
                print("Number 6 Personality")
                print("You are responsible and caring.")
                print("You love family and relationships.")
                print("You help people sincerely.")
                print("You like beauty, comfort, and harmony.")
                print("You are trustworthy and loyal.")
                print("Strengths: Love, care, responsibility.")
                print("Weaknesses: Worrying too much, overprotective.")
                print("Best Careers: Teacher, doctor, designer, counselor.")
                print("Lucky Colors: Pink, Blue, Cream.")
                print("Lucky Days: Friday, Tuesday.")
            elif number == 7:
                print("Number 7 Personality")
                print("You are thoughtful and intelligent.")
                print("You think deeply before acting.")
                print("You enjoy learning and knowledge.")
                print("You may like privacy and peace.")
                print("You are wise and observant.")
                print("Strengths: Intelligence, wisdom, analysis.")
                print("Weaknesses: Isolation, overthinking.")
                print("Best Careers: Scientist, researcher, teacher, analyst.")
                print("Lucky Colors: Violet, Blue, Grey.")
                print("Lucky Days: Monday, Thursday.")
            elif number == 8:
                print("Number 8 Personality")
                print("You are ambitious and goal-oriented.")
                print("You want success, money, and achievement.")
                print("You work hard for your dreams.")
                print("You are disciplined and determined.")
                print("You handle responsibilities well.")
                print("Strengths: Power, ambition, confidence.")
                print("Weaknesses: Stress, work pressure, stubbornness.")
                print("Best Careers: Business, law, finance, leadership.")
                print("Lucky Colors: Black, Dark Blue.")
                print("Lucky Days: Saturday, Wednesday.")
            elif number == 9:
                print("Number 9 Personality")
                print("You are kind and helpful.")
                print("You care about humanity and others.")
                print("You are emotional but generous.")
                print("You like helping people in need.")
                print("You have a warm heart.")
                print("Strengths: Compassion, kindness, generosity.")
                print("Weaknesses: Emotional pain, sacrificing too much.")
                print("Best Careers: Charity, medicine, teaching, arts.")
                print("Lucky Colors: Red, White.")
                print("Lucky Days: Tuesday, Sunday.")
            print("\nThank you for using Birth Number Personality Checker!")
        # ==========================================================
        # END OF YOUR UNCHANGED CODE
        # ==========================================================

        # Reset the print system and display results in the web app
        sys.stdout = sys.__stdout__
        st.code(output_capture.getvalue(), language='text')
    else:
        st.warning("Please enter a DOB first!")
