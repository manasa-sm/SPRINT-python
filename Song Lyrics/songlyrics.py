from dotenv import load_dotenv
import os
from lyrics_extractor import SongLyrics
load_dotenv()

GCS_API_KEY = str(os.getenv("GCS_API_KEY"))
GCS_ENGINE_ID = str(os.getenv("GCS_ENGINE_ID"))

extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)

s=input("Enter the name of the Song : ")
data = extract_lyrics.get_lyrics(s)
print(data['lyrics'])
