
# Voice Cloning Script

This project is a Python script designed for generating text-to-speech (TTS) audio using voice cloning technology. It employs pre-trained models to synthesize speech from text input, allowing for voice cloning from a given reference audio file. The script includes options to output audio in both `.wav` and `.mp3` formats and to extend the audio duration by adding silence at the end.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [License](#license)

## Introduction

The Voice Cloning Script leverages the `TTS` Python library and other audio processing tools to generate high-quality synthetic speech. This script allows you to clone a voice using a reference audio file and generate speech from a given text. Additionally, the script supports outputting the audio in `.wav` and `.mp3` formats and provides an option to extend the audio length by adding silence.

## Installation

To use this script, ensure you have the required Python packages installed. You can install them using `pip`:

```bash
pip install TTS soundfile numpy
```

> **Note**: The script references a local `.wav` file for voice cloning. Ensure this file exists at the specified path or modify the path accordingly.

## Usage

To generate cloned TTS audio, run the script with the desired text input. You can customize the output file paths if needed.

```bash
python voice_cloning.py
```

### Example Command

```bash
python voice_cloning.py "Your text here"
```

This command will generate a TTS audio file with the cloned voice based on the reference audio specified in the script.

## Features

- **Voice Cloning**: Clone a voice using a reference `.wav` file.
- **Text-to-Speech Generation**: Convert text input to synthetic speech.
- **Audio Output**: Save the generated audio in `.wav` format.
- **Audio Prolongation**: Add silence at the end of the audio to extend its duration.

## Dependencies

The following Python libraries are required to run the script:

- `TTS`: A Python library for text-to-speech synthesis.
- `soundfile`: For reading and writing sound files.
- `numpy`: For numerical operations, including handling silence in audio.

## Configuration

- **Text Input**: Modify the `text` variable in the script to change the input text for TTS generation.
- **Reference Audio**: Update the path to the reference `.wav` file for voice cloning in the `generate_cloned_tts` function.

## Examples

Below is an example of generating speech with a cloned voice:

1. Set the `text` variable to your desired input:
    ```python
    text = "It took me a long time to develop a voice, and now that I have it I'm not going to be silent."
    ```

2. Run the script:
    ```bash
    python voice_cloning.py
    ```

3. The generated audio will be saved as `output_audio.wav`, and the prolonged version will be saved as `output_audio_prolonged.mp3`.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software in accordance with the license terms.

---

This README provides a comprehensive overview of the Voice Cloning Script, ensuring you can quickly understand and use the script for your TTS needs. If you encounter any issues or need further customization, feel free to modify the script to suit your requirements.
