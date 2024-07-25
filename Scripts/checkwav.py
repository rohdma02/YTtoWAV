import wave


def is_authentic_wav(file_path):
    try:
        with wave.open(file_path, 'rb') as wav_file:
            # Check if the file is a valid WAV file
            if wav_file.getcomptype() != 'NONE':
                return False

            # Check the bit depth and sampling rate
            bit_depth = wav_file.getsampwidth() * 8
            sample_rate = wav_file.getframerate()

            # Define your criteria for lossless WAV (e.g., 16-bit or 24-bit, 44.1 kHz or 48 kHz)
            if bit_depth not in [16, 24] or sample_rate not in [44100, 48000]:
                return False

            return True
    except (wave.Error, EOFError):
        return False


# Usage
file_path = 'music\Darude - Sandstorm.wav'

# Usage
if is_authentic_wav(file_path):
    print("The file is an authentic lossless WAV.")
else:
    print("The file is not an authentic lossless WAV.")
