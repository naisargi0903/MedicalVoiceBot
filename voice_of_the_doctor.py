#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
import pygame
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


#input_text="Hi this is Ai with Hassan!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

#Step2: Use Model for Text output to Voice
def text_to_speech_with_gtts(input_text, output_filepath):
    # Create gTTS object
    tts = gTTS(text=input_text, lang='en', slow=False)
    
    # Save the audio file
    tts.save(output_filepath)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the audio
    pygame.mixer.music.load(output_filepath)
    pygame.mixer.music.play()
    
    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
input_text = "Hi this is Naisargi!autoplay"
#text_to_speech_with_gtts(input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the audio
    pygame.mixer.music.load(output_filepath)
    pygame.mixer.music.play()
    
    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
input_text = "Hi this is Naisargi!autoplay"
#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")

#C:\Users\Admin\.virtualenvs\MedicalVoiceBot-2oRxba7r\Scripts\activate to activate virtual env
