## BMI Meter

This is a simple web application built with Flask that calculates the Body Mass Index (BMI) and provides information about weight difference based on the calculated BMI. The application allows users to input their weight, height in feet and inches, and displays the BMI value along with the weight difference needed to reach a healthy weight range.

### Prerequisites

To run this application, ensure you have the following installed:

- Python (version 3.6 or higher)
- Flask (version 2.0.1 or higher)

### Installation

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Change to the project directory:

   ```bash
   cd your-repository
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Start the Flask server by running the following command:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the application.

3. Enter your weight, height in feet and inches, and click the "Calculate" button.

4. The application will display the calculated BMI and provide information about the weight difference needed to reach a healthy weight range.

### Code Explanation

The code is organized as follows:

- Import the required modules: `Flask`, `render_template`, and `request` from `flask` package.

- Create a Flask application instance:

  ```python
  app = Flask(__name__)
  ```

- Define a route for the root URL ("/") that supports both GET and POST requests:

  ```python
  @app.route('/', methods=['GET', 'POST'])
  def calculate_bmi():
  ```

  - If a POST request is received, extract the weight, feet, and inches from the submitted form data, convert the height to meters, calculate the BMI using the `calculate_bmi_value` function, and calculate the weight difference using the `calculate_weight_difference` function. Render the "result.html" template with the calculated BMI and weight difference as variables.

  - If a GET request is received, render the "index.html" template.

- Define the `calculate_bmi_value` function:

  ```python
  def calculate_bmi_value(weight, height):
  ```

  - Calculate the BMI by dividing the weight by the square of the height.

- Define the `calculate_weight_difference` function:

  ```python
  def calculate_weight_difference(weight, height):
  ```

  - Calculate the ideal weight range based on a healthy BMI (18.5 - 24.9).
  
  - If the weight is below the ideal range, calculate the weight difference needed to reach a healthy weight and return a message indicating the required weight gain.
  
  - If the weight is above the ideal range, calculate the weight difference needed to reach a healthy weight and return a message indicating the required weight loss.
  
  - If the weight is within the ideal range, return a message indicating that the weight is already within a healthy range.

- Start the Flask application:

  ```python
  if __name__ == '__main__':
      app.run()
  ```

### Customization

You can customize the application according to your needs:

- Modify the HTML templates: `index.html` and `result.html` in the `templates` directory.

- Change the styling by modifying the CSS file: `style.css` in the `static` directory.

- Add additional functionality or validation to the form submission.

### Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
