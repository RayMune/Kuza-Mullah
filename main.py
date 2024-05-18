from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route("/ussd", methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        # Main Menu
        response = "CON Welcome to Financial Literacy Tips:\n"
        response += "1. What is a money market fund?\n"
        response += "2. What are bonds and bills?\n"
        response += "3. Saving and investing?\n"
        response += "4. Emergency funds\n"
        response += "5. Exit"
    elif text == '1':
        # Explain what a money market fund is
        response = "CON A money market fund is a type of mutual fund that invests in short-term, low-risk securities such as\n"
        response += "Treasury bills, certificates of deposit, and commercial paper. It's considered relatively safe and offers\n"
        response += "higher interest rates than a regular savings account."
    elif text == '2':
        # Explain what bonds and bills are
        response = "CON Bonds and bills are debt instruments issued by governments or corporations to raise funds:\n"
        response += "- Bonds are long-term debt securities with a maturity of usually more than one year.\n"
        response += "- Treasury bills (T-bills) are short-term debt securities with maturities ranging from a few days to one year.\n"
        response += "- Treasury bonds are long-term debt securities with maturities ranging from 10 to 30 years."
    elif text == '3':
        # Explain the difference between saving and investing
        response = "CON Saving and investing are both ways to grow your wealth, but they are different:\n"
        response += "- Saving is putting money aside for short-term goals or emergencies.\n"
        response += "- Investing is putting money into assets with the expectation of earning a return, usually over the long term."
    elif text == '4':
        # Explain how to create an emergency fund
        response = "CON An emergency fund is money set aside to cover unexpected expenses.\n"
        response += "To create one:\n"
        response += "- Set a savings goal (e.g., 3-6 months' worth of expenses).\n"
        response += "- Start small and save regularly.\n"
        response += "- Keep the money in a separate account, easily accessible but separate from your regular spending."
    elif text == '5':
        # Exit the USSD session
        response = "END Thank you for using Financial Literacy Tips. Goodbye!"
    else:
        response = "CON Invalid input. Please select a valid option."

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)