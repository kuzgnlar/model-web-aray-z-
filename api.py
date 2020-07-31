from flask import Flask, jsonify, request, make_response

from ner_lib import Ner
from question_answer_lib import QuentionAnswer
from sentiment_lib import Sentiment

app = Flask(__name__)

@app.route('/qa', methods=["POST", "OPTIONS"])
def questionAnswer():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()

    elif request.method == "POST": # The actual request following the preflight
        context = request.json['context']
        question = request.json['question']

        qa = QuentionAnswer()

        if len(context) > 1000:  # Eger context 1000 karakterden fazla ise contexti cumlelere parcaliyoruz
            # Sonra her 6 cumleyi birlestirip ayri ayri context olarak kullaniyoruz
            # Birden fazla cevap cikarsa A1= A2= ... olarak donuyor
            context_sentences = context.split(".")

            counter = 0
            context_part = ""
            answer_list = []
            
            while counter < len(context_sentences):
                
                try:
                    context_part = context_sentences[counter] + context_sentences[counter+1] + context_sentences[counter+2] + context_sentences[counter+3] + context_sentences[counter+4] + context_sentences[counter+5]
                except Exception:
                    context_part = ""
                    for i in range(counter, len(context_sentences)):
                        context_part += context_sentences[i]

                try:
                    answer_list.append(qa.answer(question, context_part))
                except Exception:
                    pass
                
                counter += 6
                context_part = ""

            best_answer = None
            max_score = -1
            for a in answer_list:
                if a['score'] > max_score:
                    max_score = a['score']
                    best_answer = a

            return _corsify_actual_response(jsonify(best_answer))

        else:
            answer = qa.answer(question, context)
            return _corsify_actual_response(jsonify(answer))


@app.route('/ner', methods=["POST", "OPTIONS"])
def ner():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()

    elif request.method == "POST": # The actual request following the preflight
        context = request.json['context']

        try:
            ner = Ner()
            entities = ner.entities(context)
            return _corsify_actual_response(jsonify(entities))
            
        except Exception as e:
            print(e)
            return _corsify_actual_response(jsonify({"Error": "Failed"}))


@app.route('/sentiment', methods=["POST", "OPTIONS"])
def sentiment():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()

    elif request.method == "POST": # The actual request following the preflight
        context = request.json['context']

        try:
            sentiment = Sentiment()
            result = sentiment.result(context)
            return _corsify_actual_response(jsonify(result))
            
        except Exception as e:
            print(e)
            return _corsify_actual_response(jsonify({"Error": "Failed"}))


# CORS
def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=False)
