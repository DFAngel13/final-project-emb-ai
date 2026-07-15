"""
Módulo encargado de interactuar con la API de Watson NLP
para la detección de emociones y formateo de la salida.
Incluye manejo de errores para entradas en blanco.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Ejecuta la detección de emociones enviando una solicitud POST
    a la biblioteca Watson NLP y formatea la respuesta.

    Args:
        text_to_analyze (str): Texto que se desea analizar.

    Returns:
        dict: Diccionario con las puntuaciones o valores None en caso de error.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=input_json, timeout=10)
    
    # Manejo del error 400 (entrada en blanco o inválida)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Si la petición fue exitosa (200), procesamos el JSON
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }