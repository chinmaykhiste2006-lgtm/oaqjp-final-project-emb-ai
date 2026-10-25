"""Unit tests for the IBM Watson emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify all five supported dominant emotions."""

    def check_emotion(self, text, expected):
        """Mock Watson's response and verify the detected emotion."""
        scores = {
            "anger": 0.02,
            "disgust": 0.02,
            "fear": 0.02,
            "joy": 0.02,
            "sadness": 0.02,
        }
        scores[expected] = 0.92

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }

        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=mock_response,
        ):
            result = emotion_detector(text)

        self.assertEqual(result["dominant_emotion"], expected)
        for emotion in scores:
            self.assertEqual(result[emotion], scores[emotion])

    def test_anger(self):
        """Test an angry sentence."""
        self.check_emotion("I am really mad about this", "anger")

    def test_disgust(self):
        """Test a disgusted sentence."""
        self.check_emotion("I feel disgusted", "disgust")

    def test_fear(self):
        """Test a fearful sentence."""
        self.check_emotion("I am afraid", "fear")

    def test_joy(self):
        """Test a happy sentence."""
        self.check_emotion("I am very happy", "joy")

    def test_sadness(self):
        """Test a sad sentence."""
        self.check_emotion("I am feeling sad", "sadness")


if __name__ == "__main__":
    unittest.main()
