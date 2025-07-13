import gradio as gr
from utils import download_audio_from_youtube, transcribe_audio, summarize_text

def process_video(url):
    try:
        audio_path = download_audio_from_youtube(url)
        transcript = transcribe_audio(audio_path)
        summary = summarize_text(transcript)
        return summary
    except Exception as e:
        return f"Error: {e}"

# Gradio UI
title = "🎬 YouTube Video Summarizer"
description = "Paste a YouTube video link. This app will extract the audio, transcribe it using Whisper, and summarize the content using a Transformer model."

demo = gr.Interface(
    fn=process_video,
    inputs=gr.Textbox(label="YouTube Video URL"),
    outputs=gr.Textbox(label="Summary"),
    title=title,
    description=description
)

if __name__ == "__main__":
    demo.launch()
