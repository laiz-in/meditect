from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    #home page
    return render_template('home.html')



@app.route('/ReadMoreAboutAI')
def ReadMoreAboutAI():
    #page that deals with AI in healthcares section
    return render_template('ReadMoreAboutAI.html')

@app.route('/bmi')
def bmi():
    #page that expects height and weight and returns the BMI
    return render_template('bmi.html')

@app.route('/heartdisease')
def heartdisease():
    #page that deals with heartrates
    return render_template('heartdisease.html')


@app.route('/pneumonia')
def pneumonia():
    #page that deals with heartrates
    return render_template('pneumonia.html')

@app.route('/skindisease')
def skindisease():
    #page that deals with heartrates
    return render_template('skindisease.html')

@app.route('/diabeticdisease')
def diabeticdisease():
    #page that deals with heartrates
    return render_template('diabeticdisease.html')

@app.route('/diabeticretinopathy')
def diabeticretinopathy():
    #page that deals with heartrates
    return render_template('diabeticretinopathy.html')




if __name__ == '__main__':
     app.run(debug=True)




