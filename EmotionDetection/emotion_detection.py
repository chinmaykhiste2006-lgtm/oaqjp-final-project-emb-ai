"""Emotion detection using IBM Watson NLP."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}

EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyse):
    """Analyze text and return emotion scores and dominant emotion."""
    if not text_to_analyse or not text_to_analyse.strip():
        return dict.fromkeys((*EMOTIONS, "dominant_emotion"))

    response = requests.post(
        WATSON_URL,
        headers=HEADERS,
        json={"raw_document": {"text": text_to_analyse}},
        timeout=15,
    )

    if response.status_code == 400:
        return dict.fromkeys((*EMOTIONS, "dominant_emotion"))

    response.raise_for_status()

    data = response.json()
    emotion_scores = data["emotionPredictions"][0]["emotion"]

    result = {
        emotion: emotion_scores[emotion]
        for emotion in EMOTIONS
    }

    result["dominant_emotion"] = max(
        EMOTIONS,
        key=emotion_scores.get
    )

    return result
