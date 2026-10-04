from flask import Flask, render_template, request, redirect
import math

app = Flask(__name__)

@app.route("/")
def inicio():
    return redirect("/perimetro")

@app.route("/perimetro", methods=["GET", "POST"])
def perimetro():
    resultado = None
    error = None
    if request.method == "POST":
        try:
            radio = float(request.form["radio"])
            if radio < 0:
                error = "El radio no puede ser negativo."
            else:
                resultado = round(2 * math.pi * radio, 2)
        except ValueError:
            error = "Ingresa un número válido."
    return render_template("circulo.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5001)