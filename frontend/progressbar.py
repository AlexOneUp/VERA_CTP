import streamlit as st
import random
import time
import sounddevice as sd
from scipy.io.wavfile import write

# for user readings
prompts = ["Kids are talking by the door", "Dogs are sitting by the door",
"It's eleven o'clock", "That is exactly what happened", "I'm on my way to the meeting",
"I wonder what this is about", "The airplane is almost full", "Maybe tomorrow it will be cold",
"I think I have a doctor's appointment", "Say the word apple"]

st.write("""
# Voice Emotion Recognition on Audio
""")

image = "https://t4.ftcdn.net/jpg/03/27/36/95/360_F_327369570_CAxxxHHLvjk6IJ3wGi1kuW6WTtqjaMpc.jpg"
st.image(image, use_column_width=True)

subheader = "We'll randomly choose a prompt for you to read:"
st.subheader(subheader)
time.sleep(0.5)
st.write('"' + random.choice(prompts) + '"')
# 'Our Current Progress...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   if i == 10: break 
#   bar.progress(i + 1) # Update the progress bar with each iteration.
#   time.sleep(0.05)

# st.write('We\'re ', i,'% done!')

if st.button('Record'): # record audio 
  fs = 44100  # Sample rate
  seconds = 3  # Duration of recording
  
  with st.spinner(f'Recording for {seconds} seconds ....'):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    
    write('frontend/soundfiles/recording.wav', fs, myrecording)  # Save as WAV file 
    st.success("Recording completed")

if st.button('Play'): # play the recorded audio
  try:
    audio_file = open('frontend/soundfiles/recording.wav', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)

  except: st.write("Please record sound first")

repo = 'Check out our full repository [here!](https://github.com/AlexOneUp/VERA_CTP)'
st.markdown(repo)