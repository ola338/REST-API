from flask import Flask
from flask import jsonify, request, abort
import numpy as np

app = Flask(__name__)

words = [
    {
        'id': 1,
        'word': 'drzewo'
    }
]


@app.route('/', methods=['GET'])
def get_words():
    return jsonify({'all words': words})


@app.route('/<int:word_id>', methods=['GET'])
def get_word(word_id):
    word = [word 
            for word in words 
            if word['id'] == word_id]
    if len(word) == 0:
        abort(404)
    return jsonify({'selected word': word[0]})


@app.route('/', methods=['POST'])
def create_word():
    #if not request.json or not 'word' in request.json:
     #   abort(400)
    word = {
        'id': words[-1]['id'] + 1,
        'word': request.json['word']
    }
    words.append(word)
    return jsonify({'appended word': word})


@app.route('/<int:word_id>', methods=['DELETE'])
def delete_word(word_id):
    word = [word 
            for word in words 
            if word['id'] == word_id]
    if len(word) == 0:
        abort(404)
    words.remove(word[0])
    return jsonify({'deleted word': word})


@app.route('/<int:word_id>/amount', methods=['GET'])
def get_amout(word_id):
    search_word = [word['word'] 
                  for word in words 
                  if word['id'] == word_id]    
    sum = 0
    for word in words:
        if word['word'] == search_word[0]:
            sum += 1
    return jsonify({'number of appearances of the word': sum})


@app.route('/unique', methods=['GET'])
def get_unique_words():
    all = []
    for word in words:
        all.append(word['word'])
    all = np.array(all)
    unique = np.unique(all)
    unique = list(unique)
    return jsonify({'unique words': unique})


if __name__ == '__main__':
    app.run(debug=True)