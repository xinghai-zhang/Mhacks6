from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == '__main__':
    app.run()