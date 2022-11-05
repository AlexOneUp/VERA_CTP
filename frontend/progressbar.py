import streamlit as st
import time
import sounddevice as sd
from scipy.io.wavfile import write

st.write("""
# Voice Emotion Recognition on Audio
""")

image = "https://camo.githubusercontent.com/f3446d59b1fb66738011577c47e905d79ab0fc8358399a0f12c35b7bbef76cef/68747470733a2f2f74342e667463646e2e6e65742f6a70672f30332f32372f33362f39352f3336305f465f3332373336393537305f434178787848484c766a6b36494a33774769316b755736575474716a614d70632e6a7067"
st.image(image, use_column_width=True)

'Our Current Progress...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  if i == 10:
    break 
  # Update the progress bar with each iteration.
  bar.progress(i + 1)
  time.sleep(0.05)

st.write('We\'re ', i,'% done!')
# st.latex(''' e^{i\pi} + 1 = 0 ''')

if st.button('Record'):
  fs = 44100  # Sample rate
  seconds = 3  # Duration of recording
  
  with st.spinner(f'Recording for {3} seconds ....'):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('frontend/soundfiles/recording.wav', fs, myrecording)  # Save as WAV file 
    st.success("Recording completed")

if st.button('Play'):
  try:
    audio_file = open('frontend/soundfiles/recording.wav', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)
  
  except: st.write("Please record sound first")