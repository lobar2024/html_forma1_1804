from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        n = request.form.get('name')
        e = request.form.get('email')

        return render_template('other.html', n=n, e=e)

    return render_template('result1.html')


if __name__ == '__main__':
    app.run(debug=True)
