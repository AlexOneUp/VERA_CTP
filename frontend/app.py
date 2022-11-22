import random
import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write

import os
import sys
from dotenv import load_dotenv
load_dotenv()

# Absolute paths must be used.
backend_path = os.getenv('backend_path')
project_path = os.getenv('project_path')
sys.path.append(backend_path)
from audio_processing import get_features, increase_array_size, predict

def local_css(file_name): # Use local CSS
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("styles/style.css") 

# Prompts used in training data.
prompts = ['Kids are talking by the door', 'Dogs are sitting by the door',
'It\'s eleven o\'clock', 'That is exactly what happened', 'I\'m on my way to the meeting',
'I wonder what this is about', 'The airplane is almost full', 'Maybe tomorrow it will be cold',
'I think I have a doctor\'s appointment', 'Say the word apple']

emotions = ['angry 😡', 'calm 😌', 'disgusted 🤢', 'fearful 😨', 'happy 😆',
          'neutral 🙂', 'sad 😢', 'surprised 😳']

emotion = random.choice(emotions) 
partition = emotion.split(' ')
particle = partition[1]

def styling(): # model for 'snowfall' animation 
  return st.markdown(
    f"""
      <div class="snowflake">{particle}</div>
      <div class="snowflake">{particle}</div>
      <div class="snowflake">{particle}</div>
      <div class="snowflake">{particle}</div>
      <div class="snowflake">{particle}</div>
      <div class="snowflake">{particle}</div>
      <div class="snowflake">{particle}</div>
      <div class="snowflake">{particle}</div>

      <div class='box'>
        <div class='wave -one'></div>
        <div class='wave -two'></div>
        <div class='wave -three'></div>
      </div>
    """, unsafe_allow_html=True,
  )

# def card():
#   return """
#     <div class="card" style="width: 100%;">
#       <div class="card-header">
#       Card Header
#       </div>

#       <img class="card-img-top" src="https://t4.ftcdn.net/jpg/03/27/36/95/360_F_327369570_CAxxxHHLvjk6IJ3wGi1kuW6WTtqjaMpc.jpg" alt="Card image cap">
#       <div class="card-body">
#         <h5 class="card-title">Voice Emotion Recognition on Audio</h5>
#         <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
#         <a href="#" class="btn btn-primary col-md-3">Go somewhere</a>
#         <a href="#" class="btn btn-primary col-md-3">Go somewhere</a>
#         <a href="#" class="btn btn-primary col-md-3">Go somewhere</a>
#         <div class='btn-toolbar'>
#           <div class='btn-group'>
#             <button class="btn-danger signin">Sign In</button>
#             <button class="btn-success signup">Sign Up</button>
#           </div>
#         </div>
#       </div>
#     </div>
#   """
# 
styling()

# Bootstrap cards w/ reference to css
st.markdown("""
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"
  integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  """, unsafe_allow_html=True
)

# st.markdown(card(), unsafe_allow_html=True)

# Title.
st.write('# Voice Emotion Recognition on Audio')

# Image.
image = 'https://t4.ftcdn.net/jpg/03/27/36/95/360_F_327369570_CAxxxHHLvjk6IJ3wGi1kuW6WTtqjaMpc.jpg'
st.image(image, use_column_width=True)

# Header.
header = 'We will randomly choose a prompt for you to read:'
st.header(header)
prompt = '"' + random.choice(prompts) + '"'
st.subheader(prompt)

# prompting emotion to user
emotion_prompt = "Try to sound " + emotion + ":"
st.subheader(emotion_prompt)

def record_btn():
  if st.button('Record'): # Record audio 
    fs = 44100  # Sample rate.
    seconds = 3 # Duration of recording.
  
    with st.spinner(f'Recording for {seconds} seconds ....'):
      myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
      sd.wait() # Wait until recording is finished.
    
      write(project_path + 'frontend/soundfiles/recording.wav', fs, myrecording) # Save as .wav file.
      st.success('Recording completed.')

def play_btn(): # Play the recorded audio.
  if st.button('Play'):
    try: # Load audio file.
      audio_file = open(project_path + 'frontend/soundfiles/recording.wav', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes) 
    
    except: st.write('Please record sound first')

def classify_btn():
  if st.button('Classify'):
    try: 
      audio_features = get_features(project_path + 'frontend/soundfiles/recording.wav')
      audio_features = increase_array_size(audio_features)
      classification = predict(audio_features)
      
      st.write(classification)
    
    except: st.write('Something went wrong. Please try again')

# UI design.
col1, col2, col3 = st.columns(3)
with col1: record_btn()
with col2: play_btn()
with col3: classify_btn()
  
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

repo = """<br>
          <p align="right"> Check out our 
            <a href="https://github.com/Alexoneup/VERA_CTP"> GitHub repository </a>
          </p>
        """
st.write(repo, unsafe_allow_html=True)
