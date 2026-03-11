import torch
from transformers import pipeline
import gradio as gr

def transcript_audio(audio_file):
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

    # Perform speech recognition on the specified audio file using the initialized pipeline.
    # The batch_size parameter specifies the number of audio chunks to process in parallel,
    # which can speed up the transcription process for longer audio files.
    # The output of the pipeline is a dictionary containing the transcribed text under the 
    # "text" key.
    prediction = pipe(audio_file, batch_size=8)["text"]

    return prediction

# Create a Gradio interface for the audio transcription function.
interface = gr.Interface(
    fn=transcript_audio,
    inputs=gr.Audio(sources="upload", type="filepath"),
    outputs=gr.Textbox(label="Transcribed Text"),
    title="Audio Transcription with Whisper",
    description="Upload an audio file to transcribe it using the Whisper model.")

# Launch the Gradio interface.
interface.launch(server_name="0.0.0.0", server_port=7860)