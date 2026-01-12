import shutil
import os

def generate_video(image_file: str, audio_file: str, output_file: str):
    """
    Stub version for testing.
    Copies a placeholder video to output location.
    """
    placeholder_video = "assets/celebrities/sample_video.mp4"
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    if os.path.exists(placeholder_video):
        shutil.copy(placeholder_video, output_file)
        print(f"[Wave2Lip Stub] Video saved to {output_file}")
    else:
        print(f"[Wave2Lip Stub] Placeholder video not found: {placeholder_video}")
