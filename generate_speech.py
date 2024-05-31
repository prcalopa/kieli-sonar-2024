import os
from os.path import join, dirname
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings, play, save
import pandas as pd
import glob
from time import sleep


def read_csv_file_and_generate_audio(file_path):
    # Get the file name without the path, neither the extension
    print(os.path.splitext(os.path.basename(file_path))[0])
    folder_name = os.path.splitext(os.path.basename(file_path))[0]

    output_folder = join(generated_assets_path, folder_name)
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path, index_col=0)
    
    # Iterate over rows and columns and generate audio
    for row_index, row in df.iterrows():
        for col_index, value in row.items():
            if row_index != col_index:
                if row_index != "English" and col_index != "English":
                  print(f"{row_index} + {col_index} = {value}")
                  output_file_path = join(output_folder, f"{value}_{row_index}-{col_index}.mp3")
                  generate_audio_from_text_and_save(
                      value,
                      "Sara", 
                      "eleven_multilingual_v2", 
                      output_file_path
                  )
                  sleep(1)

def generate_audio_from_text(text, voice, model):
    audio = client.generate(
        text=text,
        voice=voice,
        model=model,
        voice_settings=VoiceSettings(
            stability=0.4,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        )
    )
    return audio

def generate_audio_from_text_and_save(text, voice, model, file_name):
    audio = generate_audio_from_text(text, voice, model)
    save(audio, file_name)
    


# Load the environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

assets_path = join(dirname(__file__), 'assets')
generated_assets_path = join(assets_path, 'generated')

ELEVEN_LABS_KEY = os.environ.get("ELEVEN_LABS_KEY")

# Create a client object
client = ElevenLabs(
  api_key= ELEVEN_LABS_KEY
)

if __name__ == "__main__":
    # Read all csv files in assets/combined-words directory
    csv_files = glob.glob(join(dirname(__file__), 'assets/combined-words/*.csv'))
    for file_path in csv_files:
        print(file_path)
        read_csv_file_and_generate_audio(file_path)


