from TTS.api import TTS

text = "My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment."
ex_output_file = 'output_audio.wav'

def generate_cloned_tts(text=text, output_dir=ex_output_file, output_mp3_file=ex_output_mp3_file, prolonged_path=ex_prolonged_path):
    # Load the XTTS model (without GPU)
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # Generate speech by cloning a voice using a single reference
    tts.tts_to_file(text=text,
                    speaker_wav=r"C:\Users\user\Downloads\combined.wav",
                    language="en",
                    file_path=output_dir)
    print(f"Speech synthesized and saved to '{output_dir}'")


if __name__ == '__main__':
    generate_cloned_tts("It took me a long time to develop a voice, and now that I have it I'm not going to be silent.")
