import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url , json = json_input , headers = header)
    my_emo_dict = json.loads(response.text)
    anger_score = my_emo_dict["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = my_emo_dict["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = my_emo_dict["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = my_emo_dict["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = my_emo_dict["emotionPredictions"][0]["emotion"]["sadness"]
    output_dict ={"anger":anger_score,"disgust" : disgust_score,"fear": fear_score,"joy": joy_score , "sadness": sadness_score}
    dominant_emotion = max (output_dict , key=output_dict.get)
    output_dict["dominant_emotion"]=dominant_emotion
    return output_dict

