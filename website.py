from flask import Flask,render_template
import virtualenv

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/code')
def projectscode():
    return render_template('projectscode.html')
@app.route('/school')
def projectsschool():
    return render_template('projectsschool.html')
@app.route('/research')
def projectsresearch():
    return render_template('projectsresearch.html')
@app.route('/fun')
def projectsfun():
    return render_template('projectsfun.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug = True)