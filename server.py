"""
Servidor Flask para el despliegue de la aplicación de detección de emociones.
Incluye validación de errores en la interfaz web.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint de la API que recibe el texto, ejecuta el análisis de emociones
    y maneja los errores si el texto es inválido.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Validar si la emoción dominante es None (Error 400)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Respuesta exitosa
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)