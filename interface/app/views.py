from flask import send_from_directory
import io
import os
from flask import Blueprint, render_template, request, send_file

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


@main.route('/', methods=['GET', 'POST'])
def index():
    download_url = None

    if request.method == 'POST':
        url = request.form['url']
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            wav_file = os.path.splitext(filename)[0] + '.wav'

            # Open the WAV file in binary mode
            with open(wav_file, 'rb') as file:
                # Create a file object from the binary data
                file_object = io.BytesIO(file.read())

            # Send the file object to the user's browser for download
            return send_file(file_object, mimetype='audio/wav', as_attachment=True, download_name=os.path.basename(wav_file))

    # Clear the form and input if it's a GET request or after form submission
    return render_template('index.html', download_url=download_url)


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


@main.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(main.static_folder, filename)
