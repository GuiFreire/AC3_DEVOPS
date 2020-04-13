import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def func_primos():

    count = 0
    num = 2
    primos = ""
    while (count <= 100):
        normal = False
        for i in range(2, num):
            if (num % i == 0):
                normal = True
                break

        if (not normal):
            count += 1
            primos = primos + (num) + ","

    num += 1
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
