# Whisper Speech Recognition App

## Overview

A Streamlit-based web application that uses OpenAI's Whisper model to convert speech to text. The application provides a user-friendly interface for uploading audio files and getting accurate transcriptions.

## Features

- Audio file upload support (WAV, MP3, M4A, OGG formats)
- Real-time audio playback
- Text transcription with download option
- Optimized for Apple Silicon (M2) processors
- User-friendly interface with progress indicators
- System information display

## Prerequisites

- Python 3.10
- FFmpeg
- macOS (optimized for M2 chip)

## Installation

### 1. Create and Activate Conda Environment

```bash
# Create new environment
conda create -n whisper_env python=3.10 -y
conda activate whisper_env
```

### 2. Install Dependencies

```bash
# Install PyTorch (for M2 Mac)
conda install pytorch torchvision torchaudio -c pytorch-nightly

# Install FFmpeg
conda install ffmpeg -c conda-forge

# Install other requirements
pip install streamlit
pip install git+https://github.com/openai/whisper.git
```

### 3. Verify Installation

```bash
# Verify whisper installation
python -c "import whisper; print(whisper.__version__)"

# Verify PyTorch installation
python -c "import torch; print(torch.__version__)"
```

## Running the Application

1. Navigate to the project directory

```bash
cd /path/to/project
```

2. Run the Streamlit app

```bash
streamlit run app.py
```

3. Access the application in your web browser (typically at http://localhost:8501)

## Troubleshooting

### Common Issues and Solutions

1. **Whisper Installation Error**

```bash
# Try reinstalling whisper
pip uninstall whisper
pip uninstall openai-whisper
pip install git+https://github.com/openai/whisper.git
```

2. **FFmpeg Missing**

```bash
# Install FFmpeg using Homebrew
brew install ffmpeg

# Or using conda
conda install ffmpeg -c conda-forge
```

3. **PyTorch Compatibility Issues**

```bash
# Reinstall PyTorch for M2
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```

### Testing Installation

Run the test script to verify all dependencies:

```bash
python test_whisper.py
```

## Project Structure

```
whisper-app/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Usage Guide

1. Launch the application using `streamlit run app.py`
2. Click the "Upload your audio file" button to select an audio file
3. Once uploaded, you can play the audio using the built-in audio player
4. Click "Transcribe" to process the audio
5. View the transcription and download it as a text file if needed

## System Requirements

- macOS (optimized for M2 chip)
- Minimum 8GB RAM recommended
- Internet connection for model download
- Sufficient disk space for model storage (~1GB)

## Performance Tips

1. For optimal performance:

   - Use clear audio recordings
   - Avoid files longer than 10 minutes
   - Keep file sizes under 25MB
   - Use supported audio formats

2. Model selection:
   - Default: "base" model
   - Can be modified to use "tiny", "small", "medium", or "large" models

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project uses the OpenAI Whisper model, which is released under the MIT License.
