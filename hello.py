from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # вывести сообщение с данным id, id - целое число
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    x = ""
    with app.test_request_context():
        x = url_for('static', filename='style.css')
    return x


if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0', debug=True)
    app.run()

    # with app.test_request_context():
    #     print(url_for('index'))
    #     print(url_for('login'))
    #     print(url_for('login', next='/'))
    #     print(url_for('profile', username='John Doe'))