import os
import random
import sounddevice as sd
import streamlit as st
import sys

from dotenv import load_dotenv
from pathlib import Path
from scipy.io.wavfile import write

import streamlit.components.v1 as components


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/style.css")
# Load Animation
animation_symbol = "❄"

# Animated Background 
# Simple Snowflake animation for Christmas

def styling():   
  return st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>

    <div class='box'>
      <div class='wave -one'></div>
      <div class='wave -two'></div>
      <div class='wave -three'></div>
    </div>

    """,
    unsafe_allow_html=True,
)
styling()


load_dotenv()

# Absolute paths must be used.
backend_path = os.getenv('backend_path')
project_path = os.getenv('project_path')

sys.path.append(backend_path)
# from audio_processing import *

# Prompts to be generated.
prompts = ['Kids are talking by the door', 'Dogs are sitting by the door',
'It\'s eleven o\'clock', 'That is exactly what happened', 'I\'m on my way to the meeting',
'I wonder what this is about', 'The airplane is almost full', 'Maybe tomorrow it will be cold',
'I think I have a doctor\'s appointment', 'Say the word apple']

# Title.
st.write('# Voice Emotion Recognition on Audio')

# Image.
image = 'https://t4.ftcdn.net/jpg/03/27/36/95/360_F_327369570_CAxxxHHLvjk6IJ3wGi1kuW6WTtqjaMpc.jpg'
st.image(image, use_column_width=True)

# Subheader.
subheader = 'We will randomly choose a prompt for you to read:'
st.subheader(subheader)
st.write('"' + random.choice(prompts) + '"')

def record_btn():
  if st.button('Record'): # Record audio 
    fs = 44100  # Sample rate.
    seconds = 3 # Duration of recording.
  
    with st.spinner(f'Recording for {seconds} seconds ....'):
      myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
      sd.wait() # Wait until recording is finished.
    
      write(project_path + 'frontend/soundfiles/recording.wav', fs, myrecording) # Save as .wav file.
      st.success('Recording completed.')
def play_btn():  
 # Play the recorded audio.
  if st.button('Play'):
    try:
    # Load audio file.
      audio_file = open(project_path + 'frontend/soundfiles/recording.wav', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes) 
    except:
      st.write('Please record sound first')

def classify_btn():
# Connection with the model.
  if st.button('Classify'):
    try: 
      audio_features = get_features(project_path + 'frontend/soundfiles/recording.wav')
      audio_features = increase_array_size(audio_features)
      classification = predict(audio_features)
      st.write(classification)
    except:
      st.write('Something went wrong. Please try again')


# UI design.
col1, col2, col3 = st.columns(3)
with col1:
  record_btn()

with col2:
  play_btn()

with col3:
  classify_btn()
  
# Skeleton on Predicted Value of the audio. 
# def state_emotion():
  
#   # In the case of persistent emotion data from a previous session:
#   try:
#     st.write("Are you still", st.session_state.emotion, "?")
  
# # Prompt 'Yes' or 'No' buttons
#   # Then let's you predict again

# # Show the Predict Emotion first.
#   except:
#     play = st.button('Predict Emotion', key='emotion', on_click=state_emotion)

repo = 'Check out our [full repository](https://github.com/Alexoneup/VERA_CTP)'
st.markdown(repo)
