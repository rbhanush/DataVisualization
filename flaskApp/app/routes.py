import json
import gensim
from app import app
import pickle
from flask import jsonify, render_template, request
from flask_wtf import Form

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
      count = request.form['words']

    else:
      count = request.args.get('words')

    default = 50
    count = int(count) if count else default
    temp = {}
    num_topics = 10

    lda = gensim.models.ldamodel.LdaModel.load('app/lda/florence/model.gensim')

    topic_summaries = []
    for i in range(num_topics):
        for term, frequency in lda.show_topic(i, topn=25):
            if term in temp.keys():
                temp[term] += frequency
            else:
                temp[term] = frequency
    temp = sorted(temp.items(), key=lambda item: item[1], reverse=True)
    result = {}
    res = []
    for i in temp[:count]:

        result['text'] = i[0]
        result['size'] = round(i[1]*500)
        res.append(result)
        result = {}
    res1 = [res, 'Hello']
    return render_template('index.html', result=res1)

@app.route('/selectDate', methods=['GET', 'POST'])
def selectDate():
    print(request.json['response1']['dateSelected'])

    return render_template('index.html', result=[{'text': 'aabcd', 'size': 100}])
