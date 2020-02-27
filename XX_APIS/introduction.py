from flask import Flask #Flask es una clase

app= Flask(__name__)#Se crea en lugar único

#Decorator
@app.route('/') #http://www.google.com/
def home():
    return "Hola Mundo!"

app.run(port = 5000)