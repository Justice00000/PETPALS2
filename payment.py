from flask import Flask, render_template, redirect
import stripe

app = Flask(__name__, template_folder='templates')

stripe.api_key = 'sk_test_51P3asWDifqfBQ4vNOQ7XLKTZLViJWv5zCygKTJck0aO8SvMO8aGTrAN5rc0brbuLYhNJdG7iPi8teySJWVfG05By00JNtjyhBl'

YOUR_DOMAIN = 'http://127.0.0.1:5000'
@app.route('/')
def home():
    return render_template('payment.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1P3bESDifqfBQ4vNNHxEBdYK',
                    'quantity': 1,
                }
            ],
            mode="payment",
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html'
        )
           
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)

if __name__ == "__main__":
    app.run(port=5000, debug=True)