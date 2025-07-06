# TTS_DEMO - Remote Voice Cloning Web App using Hugging Face API

This is a lightweight Flask-based web application for text-to-speech (TTS) voice cloning. It allows users to upload a reference audio sample and input text, then generates a synthetic voice audio that mimics the reference speaker. The TTS model is powered remotely by Hugging Face Spaces (`mrfakename/E2-F5-TTS`).

## ✨ Features

- Upload a short audio sample(less than 12 seconds) (WAV/MP3)
- Enter custom text to synthesize
- Listen to uploaded reference audio before synthesis
- Preview and download generated voice
- Works without local model installation – uses remote Hugging Face API

## 🖼️ Demo Interface

The app consists of:
- A file upload field for reference audio
- A text box to enter content for speech synthesis
- Audio players for both input preview and generated result
- A "Clear" button to reset input text

## 🚀 Installation

### Prerequisites

- Python 3.9+
- Flask
- gradio_client
- Conda or virtual environment (optional but recommended)

### Setup

```bash
# Clone this repo
git clone https://github.com/yourusername/tts_demo.git
cd tts_demo

# Create & activate virtual environment (optional)
conda create -n tts_env python=3.9
conda activate tts_env

# Install dependencies
pip install -r requirements.txt

# Run the App
python app.py

# License
MIT License - free to use and modify