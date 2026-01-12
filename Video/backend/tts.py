from gtts import gTTS

def text_to_speech(text: str, output_file: str):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"Audio saved to {output_file}")
