from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        curso = request.form.get('curso')
        return f"Inscripción recibida: {nombre} {apellidos}, Curso: {curso}"
    return render_template('inscripcion.html')

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        return f"Usuario registrado: {nombre} {apellidos}, Email: {correo}"
    return render_template('registro_usuario.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form.get('producto')
        categoria = request.form.get('categoria')
        existencia = request.form.get('existencia')
        precio = request.form.get('precio')
        return f"Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}"
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        resumen = request.form.get('resumen')
        medio = request.form.get('medio')
        return f"Libro registrado: {titulo}, Autor: {autor}, Medio: {medio}"
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)
