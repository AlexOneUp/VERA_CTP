import streamlit as st
import random
import time
import sounddevice as sd
from scipy.io.wavfile import write
import sys

# NOTE: use absolute paths 
absolute_path = ""
sys.path.insert(0, absolute_path + 'backend')
from audio_processing import *

# for user readings
prompts = ["Kids are talking by the door", "Dogs are sitting by the door",
"It's eleven o'clock", "That is exactly what happened", "I'm on my way to the meeting",
"I wonder what this is about", "The airplane is almost full", "Maybe tomorrow it will be cold",
"I think I have a doctor's appointment", "Say the word apple"]

# title
st.write("# Voice Emotion Recognition on Audio")

image = "https://t4.ftcdn.net/jpg/03/27/36/95/360_F_327369570_CAxxxHHLvjk6IJ3wGi1kuW6WTtqjaMpc.jpg"
st.image(image, use_column_width=True)

subheader = "We'll randomly choose a prompt for you to read:"
st.subheader(subheader)
# time.sleep(0.5)
st.write('"' + random.choice(prompts) + '"')

# UI design
if st.button('Record'): # record audio 
  fs = 44100  # Sample rate
  seconds = 3  # Duration of recording
  
  with st.spinner(f'Recording for {seconds} seconds ....'):
    # Recording with sounddevice lib 
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    
    write(absolute_path + 'frontend/soundfiles/recording.wav', fs, myrecording)  # Save as WAV file 
    st.success("Recording completed")

if st.button('Play'): # play the recorded audio
  try:
    #loads audio file
    audio_file = open(absolute_path + 'frontend/soundfiles/recording.wav', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes) 

  except: st.write("Please record sound first")

if st.button('Classify'): # connection with model
  try: 
    audio_features = get_features(absolute_path + 'frontend/soundfiles/recording.wav')
    
    if audio_features.shape[1] < 2376:
      audio_features = increase_ndarray_size(audio_features)

    predict(audio_features)
  except: st.write("Something went wrong.")

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


repo = 'Check out our [full repository](https://github.com/AlexOneUp/VERA_CTP)'
st.markdown(repo)