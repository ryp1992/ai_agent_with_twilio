import sounddevice as sd
import scipy.io.wavfile
import time


def record_audio(duration, filename, samplerate=44100):
    """Records audio and saves it as a WAV file."""

    print(f"Recording audio for {duration} seconds...")
    recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1,
                       dtype='int16')  # channels=1 for mono, dtype='int16' is a common format
    sd.wait()  # Wait until recording is finished
    print(f"Audio recording finished. Saving to {filename}...")
    scipy.io.wavfile.write(filename, samplerate, recording)
    print(f"Audio saved to {filename}")


if __name__ == "__main__":
    duration = 30  # Duration of recording in seconds
    filename = "recorded_audio.wav"  # Name of the output WAV file
    record_audio(duration, filename)
