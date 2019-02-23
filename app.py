#!/usr/bin/env python
from flask import Flask, jsonify, request

languages = [{'name':'javascript'},{'name':'ruby'},{'name':'python'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(debug=True)

