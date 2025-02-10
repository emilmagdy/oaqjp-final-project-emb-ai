from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
 
app = Flask("EmotionDectection")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    return '''For the given statement, the system response is "anger":{} 
    , "disgust" :{} , "fear": {} ,"joy": {} and "sadness":{}. \n 
    The diominant emotion is {}'''.format(response["anger"],response["disgust"],response["fear"], response["joy"],response["sadness"],response["dominant_emotion"])

@app.route("/")
def render_index_template():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host ="0.0.0.0" ,port=5000)

