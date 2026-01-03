
from gtts import gTTS

# Read text file
with open("input/text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Convert text to audio
tts = gTTS(text=text, lang="en")
tts.save("output/audio.mp3")

print("Audio generated successfully")
