"""Flask application for IBM Watson NLP emotion detection."""

import requests
from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the emotion detection homepage."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Return emotion analysis for the supplied text."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    try:
        response = emotion_detector(text_to_analyze)
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return "Emotion detection service is unavailable.", 502

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
