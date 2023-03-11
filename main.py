from flask import Flask, request
from flask import render_template
#from model import model

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        ticker = request.form['ticker']
        print(ticker)
        # Do something with the ticker
        text = '''
        sdfsdfsdafffffffffffffffffffffffffffffffffffffffff
                '''
        # Pass in the text as variable var
        return text
    else:
        return render_template('index.html')

'''
@app.route('/', methods=['POST'])
def submit_form():
    email = request.form['email']
    with open('emails.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([email])
    return 'Thanks for submitting your email!'
'''

if __name__ == '__main__':
    app.run()