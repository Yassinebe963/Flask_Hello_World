from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def fibo(n):
    res = ', '.join(str(b := a + b) if i else str(a) for i, (a, b) in enumerate([(0, 1)] * min(n, 50)))
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0')
