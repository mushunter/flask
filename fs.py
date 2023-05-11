import random
from flask import Flask, render_template, url_for, request, redirect   


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/main", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        age = request.form.get('age')
        marital_status = request.form.get('marital_status')
        children = request.form.get('children')
        housing_type = request.form.get('housing_type')
        position = request.form.get('position')
        experience = request.form.get('experience')
        income = request.form.get('income')
        loan_amount = request.form.get('loan_amount')
        gender = request.form.get('gender')
    
    results = random.uniform(0, 1)

    if 0.6 < results < 1:
            return redirect(url_for('green'))
    
    if 0.33 < results < 0.6:
            return redirect(url_for('yellow'))
    
    if results < 0.33:
            return redirect(url_for('red'))


        
    return render_template('main.html')


@app.route("/green")
def green():
    return render_template('green.html')


@app.route("/yellow")
def yellow():
    return render_template('yellow.html')


@app.route("/red")
def red():
    return render_template('red.html')



if __name__ == "__main__":
    app.run(debug=True)     