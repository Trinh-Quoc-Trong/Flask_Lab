from flask import Flask

app = Flask(__name__)

@app.route('/index')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>User is {name}</h1>'

@app.route('/blog/<int:blog_int>')
def blog(blog_int):
    return f'<h1>Blog number {blog_int}</h1>'



if __name__ == '__main__':
    app.run(debug=True)
    
