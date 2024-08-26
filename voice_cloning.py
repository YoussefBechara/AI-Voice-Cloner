from TTS.api import TTS
from pydub import AudioSegment

def mp3_to_wav(mp3_path, wav_path):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_path)
    # Export as WAV
    audio.export(wav_path, format="wav")
    print(f"Converted {mp3_path} to {wav_path}")

def wav_to_mp3(wav_path, mp3_path):
    # Load the WAV file
    audio = AudioSegment.from_wav(wav_path)
    # Export as MP3
    audio.export(mp3_path, format="mp3")
    print(f"Converted {wav_path} to {mp3_path}")
    
def generate_cloned_tts(text, audio_reference, output_dir='output_audio.mp3'):
    # Load the XTTS model (without GPU)
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # Generate speech by cloning a voice using a single reference
    wav_path = output_dir
    if '.mp3' in output_dir:
        wav_path = output_dir[:-3] + 'wav'
    if '.mp3' in audio_reference:
        mp3_to_wav(audio_reference, wav_path=audio_reference[:-3]+'wav')
    tts.tts_to_file(text=text, speaker_wav=audio_reference, language="en", file_path=wav_path)
    
    if '.mp3' in output_dir:
        wav_to_mp3(wav_path=wav_path, mp3_path=output_dir)

    print(f"Speech synthesized and saved to '{output_dir}'")


if __name__ == '__main__':
    text = "It took me a long time to develop a voice, and now that I have it I'm not going to be silent."
    generate_cloned_tts(text,"path-to-audio-reference")
