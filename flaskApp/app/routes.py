import json
import gensim
from app import app
import pickle
from flask import jsonify, render_template, request, redirect
from flask_wtf import Form

def ldaEvent(year, event):
    default = 50
    count = default
    temp = {}
    num_topics = 10
    newPath = 'app/data/' + year + '/' + event + '/model.gensim'
    lda = gensim.models.ldamodel.LdaModel.load(newPath)

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
    return res

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/selectDate', methods=['GET', 'POST'])
def selectDate():
    final = {}
    year = request.json['yearSelected']
    event = request.json['eventSelected']

    if event == 'Cyclone Pam':
        event = 'CyclonePam'
    elif event == 'Germanwings Crash':
        event = 'Germanwings'
    elif event == 'Paris Attacks':
        event = 'ParisAttacks'
    elif event == 'Brexit':
        event = 'Brexit'
    elif event == 'Irish General Election':
        event = 'IrishGE'
    elif event == 'Lahore Blast':
        event = 'LahoreBlast'
    elif event == 'California Wildfire':
        event = 'CaliforniaWildfire'
    elif event == 'Hurricane Harvey':
        event = 'HurricaneHarvey'
    elif event == 'Iraq Earthquake':
        event = 'IraqEarthquake'
    elif event == 'Hurricane Florence':
        event ='HurricaneFlorence'

    res = ldaEvent(year, event)
    final['ldaData'] = res

    final['mapData1'] = '/static/data/' + year + '/' + event + '/forMap1.csv'
    return jsonify(final)
