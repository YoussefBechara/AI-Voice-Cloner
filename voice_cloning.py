from TTS.api import TTS
#from pydub import AudioSegment
import numpy as np
import soundfile as sf

tts_model_path = "tts_models/en/ljspeech/fast_pitch"
vocoder_model_path = "vocoder_models/en/ljspeech/hifigan_v2"
text = "My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment."
ex_output_file = 'output_audio.wav'
ex_output_mp3_file = 'output_audio.mp3'  # Output file in .mp3 format
ex_prolonged_path = 'output_audio_prolonged.mp3'
model_path = "tts_models/multilingual/multi-dataset/xtts_v2"

def generate_cloned_tts(text=text, output_dir=ex_output_file, output_mp3_file=ex_output_mp3_file, prolonged_path=ex_prolonged_path):
    # Load the XTTS model (without GPU)
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # Generate speech by cloning a voice using a single reference
    tts.tts_to_file(text=text,
                    speaker_wav=r"C:\Users\user\Downloads\combined.wav",
                    language="en",
                    file_path=output_dir)
    print(f"Speech synthesized and saved to '{output_dir}'")

    # Convert .wav to .mp3
    # audio = AudioSegment.from_wav(output_dir)
    # audio.export(output_mp3_file, format="mp3")
    # print(f"Audio converted and saved to '{output_mp3_file}'")

    # Load your TTS audio
    data, samplerate = sf.read(output_dir)

    # Calculate the duration of the silence needed
    duration_of_silence = max(0, 62 - len(data) / samplerate)

    # Calculate the number of samples of silence needed
    silence = np.zeros(int(duration_of_silence * samplerate))

    # Append the silence to the end of the audio
    prolonged_data = np.concatenate([data, silence])

    # Save the prolonged audio
    sf.write(prolonged_path, prolonged_data, samplerate)

if __name__ == '__main__':
    generate_cloned_tts("It took me a long time to develop a voice, and now that I have it I'm not going to be silent.")
