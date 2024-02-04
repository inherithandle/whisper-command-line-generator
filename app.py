import streamlit as st
import os
import sys

def generate_whisper_command(audio_path, output_dir, model, language_code, output_format):
    command = f"whisper {audio_path} --output_dir {output_dir} --model {model} --language {language_code} --output_format {output_format}"
    return command

# Title
st.title("Whisper Command Line Generator")

# UI element to select an audio file
audio_filename = st.text_input("Specify path to audio input")

# UI element to select output directory
output_dir = st.text_input("Specify path to output directory", value="/home/gyutae/")

# Select box for model selection
model = st.selectbox("Select model",
                     ["medium", "large", "large-v2", "large-v3"],
                     index=2)  # Default value is 'large-v2'

# Select box for language selection
language = st.selectbox("Select language",
                        ["English", "Korean"],
                        index=0)  # Default value is 'English'

# Select box for output format
output_format = st.selectbox("Select output format",
                             ["all", "txt", "vtt", "srt", "tsv", "json"],
                             index=0)  # Default value is 'all'

# Submit button
if st.button("Generate Command"):
    command = generate_whisper_command(audio_filename, output_dir, model, language, output_format)
    # UI element to show the constructed command line
    st.text_area("Generated Whisper Command Line", command, height=100)