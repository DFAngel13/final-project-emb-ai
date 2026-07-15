"""
Módulo encargado de interactuar con la API de Watson NLP
para la detección de emociones en texto.
"""

import requests

def emotion_detector(text_to_analyze):
    """
    Ejecuta la detección de emociones enviando una solicitud POST
    a la biblioteca Watson NLP.

    Args:
        text_to_analyze (str): Texto que se desea analizar.

    Returns:
        str: Respuesta de la API en formato de texto.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Se incluye el parámetro timeout para evitar advertencias de seguridad en PyLint
    response = requests.post(url, headers=headers, json=input_json, timeout=10)

    return response.text