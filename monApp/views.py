from .app import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/about')
def about():
    return app.config['ABOUT']

@app.route('/contacts')
def contacts():
    return app.config['CONTACT']
if __name__ == '__main__':
    app.run()