from flask import Flask, render_template,url_for,request,redirect
import requests

API_KEY = 'a482ebc1621d4a0199d0228105beacd0'

app = Flask(__name__,
    template_folder='client/templates',
    static_folder='client/static'
    )

def get_rate(cry_to):
    url = 'https://openexchangerates.org/api/latest.json?app_id='+API_KEY
    rate_detail = requests.get(url).json()
    rate=rate_detail['rates'][cry_to]
    return rate
    

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        cry_to = request.form['cry_code_to']
        amount_to = request.form['amount']
        f_amout_to = float(amount_to)
        rate_detail = get_rate(cry_to)*f_amout_to
        return render_template('index.html', rate_value=rate_detail,amount=amount_to,cry=cry_to)

if __name__ == '__main__':
    app.run(debug=True)
