from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/profile')
def profile():
    return app.send_static_file("/static/profile.html")

if __name__ == '__main__':
    app.run()
