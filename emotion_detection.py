import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json = input_json, headers = headers)
    formated_response = json.loads(response.text)

    return formated_response

def get_raw_emotions_w_dominant(formated_response):
    if formated_response['emotionPredictions'] is not None:
        emotions_dict = formated_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotions_dict, key=emotions_dict.get)
        return {
            **emotions_dict,
            'dominant_emotion': max_emotion
        }
