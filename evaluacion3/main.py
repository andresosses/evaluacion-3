from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = ""
    estado = ""
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3, 2)
        if promedio >= 4.0 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

    return render_template('ejercicio 1.html', promedio=promedio, estado=estado)


@app.route('/ejercicio2', methods=['get', 'post'])
def ejercicio2():
    nombre_mas_largo = ""
    longitud = 0

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

    return render_template('ejercicio 2.html', nombre=nombre_mas_largo, longitud=longitud)


if __name__ == '__main__':
    app.run(debug=True)
