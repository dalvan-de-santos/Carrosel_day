from flask import Flask, render_template, url_for, request, redirect, flash
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from segurança import secretkey

app = Flask(__name__)
app.secret_key = secretkey

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', "POST"])
def homepage():
    global carrosel_images
    try:
        upload_images = os.listdir(app.config['UPLOAD_FOLDER'])
    except FileNotFoundError:
        os.makedirs(app.config['UPLOAD_FOLDER'])
        upload_images = []
    
    carrosel_images = [f'{img}' for img in upload_images]


    if request.method == "POST":
        data = request.form.get('hoje')
        if data:
            formato = "%Y-%m-%d"
            hoje = datetime.strptime(data, formato )
            hoje_data = hoje.date()
            return redirect(url_for('mother_day', hoje=hoje_data))

    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'], endpoint='upload')
def upload():
    if request.method == "POST":
        if 'image' not in request.files:
            flash('Nenhum arquivo foi selecionado')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(str(file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('imagem enviada com sucesso')
            return redirect(url_for('homepage'))
        else:
            flash('Tipo de arquivo invalido. Por favor, envie imegen do tipo (png, jpg, jpeg,)')
            return redirect(request.url)
    return render_template('upload.html')



@app.route("/motherday/<hoje>")
def mother_day(hoje):
    print(hoje)

    formato = "%Y-%m-%d"
    str_date = datetime.strptime(hoje, formato )
    hoje_date = str_date.date()
    data = datetime(2025, 5, 11)
    diamaes = data.date()

    str_namorados = datetime(2025, 6, 12)
    diadosnamorados = str_namorados.date()    
    return render_template("mother_day.html", diamaes=diamaes, hoje=hoje_date, diadosnamorados=diadosnamorados, imagens=carrosel_images)



if __name__ == "__main__":
    app.run(debug=True)