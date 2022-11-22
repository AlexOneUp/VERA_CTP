<div>
    <h1  align="center" >Voice Emotion Recognition of Audio 🔊</h1>
</div>

## INTRODUCTION

<p align="center">
   <a
      href="https://stock.adobe.com/search?k=waveform&asset_id=327369570">
      <img src="/frontend/styles/Waveform.jpg"
      alt="Waveform illustration" width="600" height="300"/>
   </a>
</p>

An audio classification project which takes audio files recorded from human speech, primarily in .wav format, and predicts the emotion conveyed from the voice.

## DATASETS USED

1. [RAVDESS Emotional Speech Dataset on Kaggle](https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio)
   <br />
   <p>This portion of the RAVDESS contains 1440 files: 60 trials per actor x 24 actors = 1440. The RAVDESS contains 24 professional actors (12 female, 12 male), vocalizing two lexically-matched statements in a neutral North American accent. Speech emotions includes calm, happy, sad, angry, fearful, surprise, and disgust expressions. Each expression is produced at two levels of emotional intensity (normal, strong), with an additional neutral expression.</p>

2. [CREMA-D: Crowd Sourced Emotional Multimodal Actors Dataset](https://www.kaggle.com/datasets/ejlok1/cremad)
   <br>
   <p>CREMA-D is a data set of 7,442 original clips from 91 actors. These clips were from 48 male and 43 female actors between the ages of 20 and 74 coming from a variety of races and ethnicities (African America, Asian, Caucasian, Hispanic, and Unspecified). Actors spoke from a selection of 12 sentences. The sentences were presented using one of six different emotions (Anger, Disgust, Fear, Happy, Neutral, and Sad) and four different emotion levels (Low, Medium, High, and Unspecified).</p>

3. [SAVEE: Surrey Audio-Visual Expressed Emotion](https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee)
   <br>
   <p>The SAVEE database was recorded from four native English male speakers (identified as DC, JE, JK, KL), postgraduate students and researchers at the University of Surrey aged from 27 to 31 years. Emotion has been described psychologically in discrete categories: anger, disgust, fear, happiness, sadness and surprise. A neutral category is also added to provide recordings of 7 emotion categories.<br>

   The text material consisted of 15 TIMIT sentences per emotion: 3 common, 2 emotion-specific and 10 generic sentences that were different for each emotion and phonetically-balanced. The 3 common and 2 × 6 = 12 emotion-specific sentences were recorded as neutral to give 30 neutral sentences. This resulted in a total of 120 utterances per speaker.</p>

4. [TESS: Toronto Emotional Speech Set](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess)
   <br>
   <p>There are a set of 200 target words were spoken in the carrier phrase "Say the word _' by two actresses (aged 26 and 64 years) and recordings were made of the set portraying each of seven emotions (anger, disgust, fear, happiness, pleasant surprise, sadness, and neutral). There are 2800 data points (audio files) in total.<br>

   The dataset is organized such that each of the two female actor and their emotions are contain within its own folder. And within that, all 200 target words audio file can be found. The format of the audio file is a WAV format</p>

## TECHNOLOGIES

1. [Librosa](https://librosa.org)
2. [Numpy](https://numpy.org/)
3. [Pandas](https://pandas.pydata.org/)
4. [Seaborn](https://seaborn.pydata.org/)
5. [Plotly](https://plotly.com/)
6. [Tensorflow/Keras](https://www.tensorflow.org/)
7. [Scikit-Learn](https://scikit-learn.org/stable/)
8. [Kaggle](https://www.kaggle.com/)
9. [Streamlit](https://streamlit.io/)

## UI
<p align="center">
   <img src="/frontend/styles/UI.png"
      alt="User Interface Design illustration" width="1721" height="500"/>
</p>   

## NOTEBOOK VIEWER LINK

You can check the Jupyter notebook for [model creation](https://nbviewer.org/github/AlexOneUp/VERA_CTP/blob/main/backend/vera-ctp.ipynb) here.

## SPECIAL MENTIONS

1. [Vijay Anandan](https://www.linkedin.com/in/vijay-anadan) who helped coordinate with the ideation and guidance in the project.

## CONTRIBUTION AND FEEDBACK

If you would like to contribute or have any feedback for this project please feel free to contact one of the three members of the group.

## CODE LICENSE

MIT License

Copyright (c) 2022 Georgios Ioannou, Hussam Marzooq, Alex Ruan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
