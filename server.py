"""
Emotion Detection Server
Flask-based server for performing emotion detection on user-provided text.
Author: [divinemuffin]
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, get_raw_emotions_w_dominant

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def run_detection():
    """
    User input analysis
    """
    text_to_detect = request.args.get('textToAnalyze')
    formated_response = get_raw_emotions_w_dominant(emotion_detector(text_to_detect))
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route('/')
def index():
    """
    Render main page
    """
    return render_template('index.html')

app.run(host="0.0.0.0", port=5000)
