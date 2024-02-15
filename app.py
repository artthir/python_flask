from flask import Flask, redirect, url_for, request
import html_generator as h

app = Flask(__name__)

@app.route('/')
def get_root():
    return h.make_body('Etusivu', h.form())

@app.route('/user', methods = ['POST'])
def post_test():
    value = request.form['username']
    #print(value)
    return h.redirect(url_for('/'))