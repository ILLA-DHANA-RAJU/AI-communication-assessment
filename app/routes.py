from flask import Blueprint, render_template, request, redirect, flash, current_app as app
from werkzeug.utils import secure_filename
import os
from app.utils.audio_analysis import analyze_audio

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/interview', methods=['GET', 'POST'])
def interview():
    if request.method == 'POST':
        if 'audio' not in request.files:
            flash('No file uploaded.')
            return redirect(request.url)

        file = request.files['audio']
        if file.filename == '':
            flash('No file selected.')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        result = analyze_audio(filepath)
        return render_template('interview.html', result=result)

    return render_template('interview.html', result=None)
