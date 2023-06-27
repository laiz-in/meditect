from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    #home page or just landing page
    return render_template('home.html')


@app.route('/about')
def about():
    home_url = url_for('home')

    #contents that contains in about page
    return render_template('about.html',home_url=home_url)


@app.route('/bmi')
def bmi():
    #page that expects height and weight and returns the BMI
    return render_template('bmi.html')

@app.route('/heartrate')
def heartrate():
    #page that deals with heartrates
    return render_template('heartrate.html')


@app.route('/xray')
def xray():
    #page that deals with heartrates
    return render_template('xray.html')



if __name__ == '__main__':
    app.run()




