from flask import Flask, jsonify
# create a flask app
app = Flask(__name__)
# define an endpoint
# / is a home page of the app
@app.route('/') #http://mywebsite.com/
# func what runs whenever a client enters the endpoint
def home():
    # flask cant return dictionaries, only strings, so jsonify(dict->str)
    return jsonify({'message': 'hello world'})


if __name__ == '__main__':
    app.run()
    
    
