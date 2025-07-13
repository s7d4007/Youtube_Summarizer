# 🎬 YouTube Video Summarizer (AI-Powered)

This is an AI-powered YouTube video summarizer that:
- Downloads a YouTube video
- Transcribes it using OpenAI's Whisper
- Summarizes the content using a Hugging Face transformer model
- Displays the final summary in a simple web interface using Gradio

> ⚠️ This is my first version, so processing may take some time. Still learning and working on improving performance!

---

## 🔧 Tech Stack

- **Python**
- [OpenAI Whisper](https://github.com/openai/whisper) for transcription
- [Hugging Face Transformers](https://huggingface.co/transformers/) for summarization
- [yt_dlp](https://github.com/yt-dlp/yt-dlp) for YouTube audio extraction
- [Gradio](https://gradio.app/) for a simple web UI

---

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/s7d4007/Youtube_Summarizer.git
cd youtube-summarizer
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
(Optional) Install FFmpeg (if needed)
Whisper supports .m4a, .webm, and .mp3, but for some formats FFmpeg may be needed.

Download FFmpeg from https://ffmpeg.org/download.html
Add it to your system PATH.

Run the app

bash
Copy
Edit
python app.py
Gradio will start and provide a local web link.
