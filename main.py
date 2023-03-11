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
        
                    At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards) At the moment the model only supports tickers that issue a 10k, so only American publically listed companies. We are in the process of adding a checkpoint
            for training on the 20f annual reports (the international standards)'''
        # Pass in the text as variable var
        return render_template('index.html',text=text)
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