import torch
from transformers import pipeline

# Initialize the speech-to-text pipeline using the Hugging Face Transformers library.
# Load the Whisper model for automatic speech recognition
# The "openai/whisper-tiny.en" model is a smaller version of the Whisper model, 
# optimized for English speech recognition.
# The chunk_length_s parameter specifies the length of audio chunks (in seconds) 
# that the model will process at a time.
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30)

# Define the path to the audio file that you want to transcribe.
audio_file = "audio_file.mp3"

# Perform speech recognition on the specified audio file using the initialized pipeline.
# The batch_size parameter specifies the number of audio chunks to process in parallel,
# which can speed up the transcription process for longer audio files.
# The output of the pipeline is a dictionary containing the transcribed text under the 
# "text" key.
prediction = pipe(audio_file, batch_size=8)["text"]

# Print the transcribed text to the console.
print(prediction)
