import os
import uuid
import yt_dlp
import whisper
from transformers import pipeline

# ========== 1. Download Audio from YouTube ==========

def download_audio_from_youtube(url: str, output_path: str = "assets") -> str:
    """
    Downloads the best audio format from YouTube using yt_dlp without conversion.
    Returns the downloaded file path.
    """
    try:
        # Generate a unique filename base
        filename_base = str(uuid.uuid4())
        output_template = os.path.join(output_path, filename_base + ".%(ext)s")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'quiet': True,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            ext = info.get('ext', 'webm')
            final_path = os.path.join(output_path, f"{filename_base}.{ext}")
            return final_path

    except Exception as e:
        raise RuntimeError(f"Failed to download audio: {e}")


# ========== 2. Transcribe using Whisper ==========

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes the given audio file using OpenAI's Whisper.
    Returns the transcribed text.
    """
    try:
        model = whisper.load_model("base")  # You can also use "tiny" or "small"
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {e}")


# ========== 3. Summarize using Transformers ==========

# Load the summarizer once (global)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str, max_chunk_len: int = 1000) -> str:
    """
    Summarizes long text by splitting into manageable chunks and combining results.
    """
    try:
        chunks = [text[i:i + max_chunk_len] for i in range(0, len(text), max_chunk_len)]
        summary = ""

        for chunk in chunks:
            result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summary += result[0]["summary_text"] + " "

        return summary.strip()

    except Exception as e:
        raise RuntimeError(f"Summarization failed: {e}")
