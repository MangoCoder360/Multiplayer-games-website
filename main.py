from flask import Flask

app = Flask('app')


@app.route('/')
def index():
    htmlFile = open("index.html", "r")
    html = htmlFile.read()
    htmlFile.close()
    return html


@app.route('/gameChooser')
def gameChooser():
    htmlFile = open("gameChooser.html", "r")
    html = htmlFile.read()
    htmlFile.close()
    return html


@app.route('/poker')
def poker():
    htmlFile = open("games/poker.html", "r")
    html = htmlFile.read()
    htmlFile.close()
    return html


@app.route("/style.css")
def stylesheet():
    css = open('style.css', 'r')
    style = css.read()
    css.close()
    return style


app.run(host='0.0.0.0', port=8080)
