from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        feet = float(request.form['feet'])
        inches = float(request.form['inches'])
        height = (feet * 12 + inches) * 0.0254  # Convert height to meters
        bmi = calculate_bmi_value(weight, height)
        weight_difference = calculate_weight_difference(weight, height)
        return render_template('result.html', bmi=bmi, weight_difference=weight_difference)
    return render_template('index.html')

def calculate_bmi_value(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_weight_difference(weight, height):
    # Calculate ideal weight range based on a healthy BMI (18.5 - 24.9)
    ideal_weight_min = 18.5 * (height ** 2)
    ideal_weight_max = 24.9 * (height ** 2)
    
    if weight < ideal_weight_min:
        weight_difference = ideal_weight_min - weight
        return f"You need to gain {round(weight_difference, 2)} kg to reach a healthy weight."
    elif weight > ideal_weight_max:
        weight_difference = weight - ideal_weight_max
        return f"You need to lose {round(weight_difference, 2)} kg to reach a healthy weight."
    else:
        return "You are already within a healthy weight range."

if __name__ == '__main__':
    app.run()
