import streamlit as st
import time
st.write("""
# Voice Emotion Recognition on Audio
""")

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