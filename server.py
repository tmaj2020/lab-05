import flask 

app = flask.Flask(__name__)

# TODO: create a route for the delay endpoint.
#      The route should accept POST requests and return the same message that was sent to it.

@app.route('/delay', methods=['POST'])
def delay():
    x = flask.request.data
    return x

if __name__ == "__main__":
    app.run()