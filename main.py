from flask import Flask, Blueprint

# prepare views

# load up databse connection

app = Flask(__name__)

@app.route("/")
def site_map():
    return 'Im working. Sitemap will be here\n'

@app.route("/tags")
def tags():
    return 'Tags will be here\n'

@app.route("/persons")
def persons():
    return 'Persons will be here\n'

@app.route("/logs")
def logs():
    return 'Logs will be here later\n'



if __name__ == '__main__':
    app.run(debug=True)

