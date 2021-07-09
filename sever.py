# Import Flask to allow us to create our app
from flask import Flask
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
# The "@" decorator associates this route with the function immediately following
# Return the string 'Hello World!' as a response
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "dojo"

@app.route('/say/<string:name>')
def whats_suh_dude(name):
    print(name)
    return "Hello, " + str(name)

@app.route('/repeat/<int:somenumber>/<string:someword>')
def repeating(somenumber, someword):
    return f"{somenumber * someword}"

@app.errorhandler(404)
def notfoundbrother(e):
    return "Sorry! No response. Try again"

# Ensure this file is being run directly and not from a different module
# Run the app in debug mode.
if __name__=="__main__":
    app.run(debug=True)