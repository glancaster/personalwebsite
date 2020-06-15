from flask import Flask,render_template
import virtualenv

app = Flask(__name__)

@app.route('/Home')
def home():
    return render_template('index.html')
@app.route('/About')
def about():
    return render_template('about.html')
@app.route('/Projects')
def projects():
    return render_template('projects.html')
@app.route('/Contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug = True)