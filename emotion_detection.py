from flask import Flask, render_template, request
emotion_detection = Flask('Emotion detection')

@emotion_detection.route('/templates/')
def index():
    return render_template('index.html')

if name == "main":
    emotion_detection(debug=True)