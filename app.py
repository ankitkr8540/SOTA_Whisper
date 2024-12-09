import streamlit as st
import os
import tempfile
# First, verify whisper installation
try:
    import whisper
except ImportError:
    st.error("Whisper not found. Please install it using: pip install git+https://github.com/openai/whisper.git")
    st.stop()

# Configure page
st.set_page_config(
    page_title="Whisper Speech Recognition",
    page_icon="🎙️",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
    }
    .upload-text {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the Whisper model"""
    try:
        return whisper.load_model("base")
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def transcribe_audio(audio_file):
    """Transcribe audio file using Whisper"""
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
        tmp_file.write(audio_file.getvalue())
        tmp_path = tmp_file.name
    
    try:
        # Load model and transcribe
        model = load_model()
        if model is None:
            return "Error: Model failed to load"
        
        result = model.transcribe(tmp_path)
        return result["text"]
    except Exception as e:
        return f"Error during transcription: {str(e)}"
    finally:
        # Clean up temporary file
        os.unlink(tmp_path)

def main():
    st.title("🎙️ Whisper Speech Recognition")
    st.markdown("### Convert Speech to Text")

    # Model loading
    with st.spinner("Initializing Whisper model..."):
        model = load_model()
        if model:
            st.success("Model loaded successfully! ✅")
        else:
            st.error("Failed to load model. Please check your installation.")
            st.stop()

    # File upload section
    st.markdown('<p class="upload-text">Upload your audio file</p>', unsafe_allow_html=True)
    audio_file = st.file_uploader(
        "",  # Empty label as we're using custom text above
        type=['wav', 'mp3', 'm4a', 'ogg'],
        help="Supported formats: WAV, MP3, M4A, OGG"
    )

    if audio_file:
        # Audio player
        st.audio(audio_file)
        
        # Transcribe button
        if st.button("🎯 Transcribe Audio"):
            try:
                with st.spinner("Processing your audio..."):
                    transcription = transcribe_audio(audio_file)
                
                if not transcription.startswith("Error"):
                    # Success case
                    st.markdown("### 📝 Transcription Result:")
                    st.markdown(
                        f'<div style="padding: 20px; background-color: #f0f2f6; color: #333; font-size: 18px;'
                        f'border-radius: 10px;">{transcription}</div>',
                        unsafe_allow_html=True
                    )
                    st.markdown("<br><br>", unsafe_allow_html=True)
                    # Download option
                    st.download_button(
                        "📥 Download Transcription",
                        transcription,
                        file_name="transcription.txt",
                        mime="text/plain"
                    )
                else:
                    # Error case
                    st.error(transcription)
                    st.info("Please try again with a different audio file.")
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please try again with a different audio file.")

    # Information section
    with st.expander("ℹ️ About this app"):
        st.markdown("""
        This application uses OpenAI's Whisper model to convert speech to text. 
        
        **Features:**
        - Supports multiple audio formats (WAV, MP3, M4A, OGG)
        - Provides downloadable transcription
        - Easy-to-use interface
        
        **Tips for best results:**
        - Use clear audio with minimal background noise
        - Keep files under 25MB for best performance
        - Supported languages: Multiple (auto-detected)
        """)

if __name__ == "__main__":
    main()