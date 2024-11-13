from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route('/test')
def about():
    return render_template('index_snow_test_3.html')
    # return render_template('index_1.html')


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    return f'<h1>User is {name}</h1>'

@app.route('/blog/<int:blog_int>')
def blog(blog_int):
    return f'<h1>Blog number {blog_int}</h1>'

# cccc

@app.route('/admin')
def admin():
    return '<h1>Admin Page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
    
