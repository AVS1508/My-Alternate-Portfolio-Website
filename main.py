from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
'''
@app.route('/submit-form', methods=['POST'])
def submit_form():
    email = request.form['email']
    with open('emails.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([email])
    return 'Thanks for submitting your email!'
'''
if __name__ == '__main__':
    app.run()