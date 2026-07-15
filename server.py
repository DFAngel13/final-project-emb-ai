"""
Servidor Flask para el despliegue de la aplicación de detección de emociones.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Inicializar la aplicación Flask
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
    y devuelve una cadena de texto formateada para el usuario.
    """
    # Extraer el texto de los parámetros GET (request.args)
    text_to_analyze = request.args.get('textToAnalyze')

    # Ejecutar la función de detección importada
    response = emotion_detector(text_to_analyze)

    # Construir y retornar el string exacto que pide la evaluación
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    # Ejecutar el servidor en el puerto 5000
    app.run(host="0.0.0.0", port=5000)