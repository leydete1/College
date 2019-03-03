from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
        return "Looks like it works!"

app.run()
