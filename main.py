from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET', "POST"])
def homepage():
    if request.method == "POST":
        data = request.form.get('hoje')
        if data:
            formato = "%Y-%m-%d"
            hoje = datetime.strptime(data, formato )
            hoje_data = hoje.date()
            return redirect(url_for('mother_day', hoje=hoje_data))

    return render_template('index.html')



@app.route("/motherday/<hoje>")
def mother_day(hoje):
    imagens = [
        {"arquivo": "mother_day1.png", "titulo": "Amor incondicional", "descricao": "Mãe, você é e sempre será a minha melhor parte. Nunca vou te esquecer!."},
        {"arquivo": "mother_day2.png", "titulo": "Gratidão", "descricao": "Mãe, no dicionário da minha vida, você é a própria definição do amor.."},
        {"arquivo": "mother_day3.png", "titulo": "Felicidades", "descricao": "Feliz Dia das Mães, que a luz de Cristo brilhe no caminho de cada mãe!."},
    ]

    formato = "%Y-%m-%d"
    str_date = datetime.strptime(hoje, formato )
    hoje_date = str_date.date()
    data = datetime(2025, 5, 11)
    diamaes = data.date()
    print(diamaes)
    print(hoje_date)
    return render_template("mother_day.html", diamaes=diamaes, hoje=hoje_date, imagens=imagens)



if __name__ == "__main__":
    app.run(debug=True)