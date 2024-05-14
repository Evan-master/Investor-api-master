from flask import Flask, request, jsonify
import handle.investor
import configs

app = Flask(__name__)


@app.route('/investor', methods=['POST'])
def stock_investor_service():
    data = request.json
    prompt = data.get('query', '')

    response = handle.investor.stock_investor(prompt)
    return jsonify({"response": response})


if __name__ == '__main__':
    investor_port = configs.config.get_port()
    app.run(debug=True, port=investor_port)
