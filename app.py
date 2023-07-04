from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi_value(weight, height)
        return render_template('result.html', bmi=bmi)
    return render_template('index.html')

def calculate_bmi_value(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

if __name__ == '__main__':
    app.run()
