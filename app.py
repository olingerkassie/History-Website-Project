from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorite', methods=['GET','POST'])
def favorite():
    name = None
    if request.method == 'POST':
        name = request.form['figure']
    return render_template('favorite.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)