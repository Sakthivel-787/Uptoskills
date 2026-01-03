
import os

print("Step 1: Converting text to speech...")
os.system("python tts.py")

print("Step 2: Generating talking video...")

command = (
    "python Wav2Lip/inference.py "
    "--checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth "
    "--face input/image.jpeg "
    "--audio output/audio.mp3 "
    "--outfile output/result.mp4"
)

os.system(command)

print("Talking image video created successfully!")
