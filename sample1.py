from gtts import gTTS
import pygame
import os

def speak_text(text):
    try:
        # Define the directory and filename
        directory = "./temp_audio"
        filename = "output.mp3"
        
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)
        
        # Full path to the output file
        file_path = os.path.join(directory, filename)
        
        # Generate and save the speech
        tts = gTTS(text=text, lang='en')
        tts.save(file_path)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load and play the audio
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Remove the file after playback
        os.remove(file_path)
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
speak_text("Hello, this is a test.")
