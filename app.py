from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = 0
    resultado = ""

    if request.method == 'POST':
        try:
            notas = [int(request.form['nota1']), int(request.form['nota2']), int(request.form['nota3'])]
            asistencia = int(request.form['asistencia'])

            if all(10 <= nota <= 70 for nota in notas) and 0 <= asistencia <= 100:
                promedio = sum(notas) / len(notas)

                if promedio >= 40 and asistencia >= 75:
                    resultado = "Aprobado"
                else:
                    resultado = "Reprobado"
            else:
                resultado = "Error: Las notas y la asistencia deben estar en los rangos especificados."

        except ValueError as e:
            resultado = f"Error: {str(e)}"

    return render_template('ejercicio1.html', promedio=promedio, resultado=resultado)

@app.route('/resultado_ejercicio1')
def resultado_ejercicio1():
    resultado = request.args.get('resultado', '')
    return render_template('resultado_ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mas_largo = ""
    cantidad_caracteres = ""
    resultado = ""

    if request.method == 'POST':
        try:
            nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]

            nombre_mas_largo = max(nombres, key=len)
            cantidad_caracteres = len(nombre_mas_largo)
            resultado = f"Nombre con más caracteres: {nombre_mas_largo}, Cantidad de caracteres: {cantidad_caracteres}"

        except ValueError as e:
            nombre_mas_largo = "Error"
            cantidad_caracteres = str(e)

    return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
