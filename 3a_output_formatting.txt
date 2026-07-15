"""
Módulo encargado de interactuar con la API de Watson NLP
para la detección de emociones y formateo de la salida.
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
        dict: Diccionario con las puntuaciones de cada emoción y la dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Petición a la API
    response = requests.post(url, headers=headers, json=input_json, timeout=10)
    
    # Transformar el texto JSON devuelto en un diccionario de Python
    formatted_response = json.loads(response.text)
    
    # Extraer el conjunto de emociones de la estructura anidada
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Crear un diccionario temporal para encontrar el valor máximo
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Calcular la emoción dominante
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    
    # Retornar el formato exacto requerido por el proyecto
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }