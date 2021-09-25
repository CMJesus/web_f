from flask import Flask

app = Flask(__name__)
# desde el Objeto Flask creamos una instancia, a la que tenemos
# que pasarle un parámetro para saber su nombre (__name__).

# Ahora, usaremos decoradores, que envuelven nuestras funciones
# añadiendo nuevas funcionalidades. 
# Nuestras funciones serán las que hagan los requerimientos:
# rutas > endpoints.

@app.route('/')
# Decorador debe de ir acompañado de una función
def webbApp_inicio():
    return 'Hola, mundo'#.upper()

# Otra vista.
@app.route('/bye')
def webbApp_fin():
    return 'Adiós, mundo'#.lower()