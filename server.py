'''This is the main server module 
through which the application is run 
and main routes are defined'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDectection")

@app.route("/emotionDetector")
def emo_detector():
    '''This function brings the text to be analyzed
    and pass it to the emotion_detector function
    and then return back the response in a formated dictionary 
    from which the data could be displayed'''

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid test!. \n Please try again."
    return f'''For the given statement, the system response is "anger":{response["anger"]}
    , "disgust" :{response["disgust"]} , "fear": {response["fear"]} ,"joy": {response["joy"]} 
    , "sadness":{response["sadness"]} , The diominant emotion is {response["dominant_emotion"]}'''

@app.route("/")
def render_index_template():
    ''' renders the index.html to show as the index page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host ="0.0.0.0" ,port=5000)
