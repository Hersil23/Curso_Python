from flask import Flask


app = Flask(__name__)



if __name__ == '__main__':
    # Ejecutamos nuestra aplicacion
    app.run(debug=True)