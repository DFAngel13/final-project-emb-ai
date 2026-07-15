"""
Módulo de pruebas unitarias para el paquete EmotionDetection.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Clase que contiene las pruebas unitarias para la función emotion_detector.
    """

    def test_emotion_predictor(self):
        """
        Prueba las cinco emociones principales para asegurar que
        la emoción dominante devuelta sea la correcta.
        """
        # Prueba 1: Alegría (joy)
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Prueba 2: Enojo (anger)
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Prueba 3: Asco/Disgusto (disgust)
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Prueba 4: Tristeza (sadness)
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Prueba 5: Miedo (fear)
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()