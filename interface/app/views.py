import io
import os
import wave
from flask import Blueprint, render_template, request, send_file, url_for

import yt_dlp

main = Blueprint('main', __name__)

output_dir = os.path.join(os.path.dirname(__file__), 'music')
os.makedirs(output_dir, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}


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


def get_wav_specs(file_path):
    try:
        with wave.open(file_path, 'rb') as wav_file:
            num_channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            sample_rate = wav_file.getframerate()
            num_frames = wav_file.getnframes()
            duration = num_frames / float(sample_rate)

            return {
                'num_channels': num_channels,
                'sample_width': sample_width,
                'sample_rate': sample_rate,
                'num_frames': num_frames,
                'duration': duration
            }
    except (wave.Error, EOFError):
        return None


@main.route('/', methods=['GET', 'POST'])
def index():
    download_url = None
    is_authentic = None
    wav_specs = None

    if request.method == 'POST':
        url = request.form['url']
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            wav_file = os.path.splitext(filename)[0] + '.wav'
            is_authentic = is_authentic_wav(wav_file)
            wav_specs = get_wav_specs(wav_file)

            # Open the WAV file in binary mode
            with open(wav_file, 'rb') as file:
                # Create a file object from the binary data
                file_object = io.BytesIO(file.read())

            # Send the file object to the user's browser for download
            return send_file(file_object, mimetype='audio/wav', as_attachment=True, download_name=os.path.basename(wav_file))

    # Clear the form and input if it's a GET request or after form submission
    return render_template('index.html', download_url=download_url, is_authentic=is_authentic, wav_specs=wav_specs)


@main.route('/download/<filename>')
def download_file(filename):
    wav_file_path = os.path.join(output_dir, filename)

    # Open the WAV file in binary mode
    with open(wav_file_path, 'rb') as file:
        # Create a file object from the binary data
        file_object = io.BytesIO(file.read())

    # Send the file object to the user's browser for download
    return send_file(file_object, mimetype='audio/wav', as_attachment=True, download_name=filename)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/tracks')
def tracks():
    return render_template('tracks.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/logout')
def logout():
    return render_template('logout.html')


@main.route('/register')
def register():
    return render_template('register.html')
