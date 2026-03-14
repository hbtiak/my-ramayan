import streamlit as st
from gtts import gTTS
import os

episodes = {
    "Childhood of Ram": {
        "story": "Ram was born in Ayodhya to King Dasharatha and Queen Kaushalya. His childhood reflected wisdom, discipline, and valor.",
        "image": "images/childhood_ram.png"
    },
    "Sita Swayamvar": {
        "story": "In Mithila, Ram broke Lord Shiva's bow to win Sita's hand in marriage, symbolizing strength and divine destiny.",
        "image": "images/sita_swayamvar.png"
    },
    "Vanvaas": {
        "story": "Ram, Sita, and Lakshman went into exile for 14 years, showing sacrifice and adherence to dharma.",
        "image": "images/vanvaas.png"
    },
    "Battle of Lanka": {
        "story": "Ram fought Ravana with the help of Hanuman and the Vanara army, symbolizing the triumph of good over evil.",
        "image": "images/battle_lanka.png"
    }
}

st.title("AI-Driven Narrative Demo: Ramayan Storytelling with Art & Voice")
st.title("<Arts by - Dr Kedar Dicholkar>")


choice = st.selectbox("Choose a Ramayan episode:", list(episodes.keys()))
story_text = episodes[choice]["story"]
image_path = episodes[choice]["image"]

st.subheader("Narrative")
st.write(story_text)

st.subheader("Illustration")
if os.path.exists(image_path):
    st.image(image_path, use_column_width=True)
else:
    st.warning("Image not found. Please add your artwork in the 'images/' folder.")

if st.button("Play Narration"):
    tts = gTTS(text=story_text, lang='en')
    tts.save("story.mp3")
    audio_file = open("story.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
