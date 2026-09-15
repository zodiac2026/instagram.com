from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Test</title>
    </head>
    <body style="background:white;">
        <h1 style="color:black;">FLASK TEST</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
