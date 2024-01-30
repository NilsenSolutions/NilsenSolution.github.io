from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Handle form submission here
    name = request.form.get('Name')
    email = request.form.get('Email')
    subject = request.form.get('Subject')
    comment = request.form.get('Comment')

    # Do something with the form data (e.g., save to a database)

    return f'Thank you, {name}! Your form has been submitted.'

if __name__ == '__main__':
    app.run(debug=True)
