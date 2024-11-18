import streamlit as st
import random

# Initialize session state
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if "guess_count" not in st.session_state:
    st.session_state.guess_count = 0
if "message" not in st.session_state:
    st.session_state.message = "Try to guess the number!"

# Function to reset the game
def reset_game():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.message = "Game reset! Try to guess the number!"

# Streamlit interface
st.title("Number Guessing Game")
st.write("Guess a number between 1 and 100.")

# Input field for the user's guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.guess_count += 1
    if guess < st.session_state.target_number:
        st.session_state.message = "Too low! Try again."
    elif guess > st.session_state.target_number:
        st.session_state.message = "Too high! Try again."
    else:
        st.session_state.message = (
            f"Congratulations! You guessed the number in {st.session_state.guess_count} tries!"
        )

st.write(st.session_state.message)

# Button to reset the game
if st.button("Reset Game"):
    reset_game()
