from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__ , template_folder='template')

model = pickle.load(open('student_dropout1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('result.html' , output = 'something')

if __name__ == '__main__' :
    app.run(debug = True)