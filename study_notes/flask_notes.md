## How to use Flask

### 1. First settings

```bash
# install Flask
pyenv activate my-env
pip install flask

# Flask project structure
project_folder/
  app.py
  templates/
    home.html
    about.html
  statics/
    js/
      main.js
    css/
      main.css

# create flask app
mkdir flaskblog
cd flaskblog
# create app.py
vi app.py
# input below

  from flask import Flask, render_template
  app = Flask(__name__)

  posts = [
    dict(author='Phan Hoang Phuong',
         title='My Blog',
         content='Introduction',
         date_posted='Jan 25 2021')
  ]

  @app.route('/')
  @app.route('/home')
  def home():
      return render_template('home.html', posts=posts)
      # return '<h1>Hello, world!</h1>'

  if __name__=='__main__':
    app.run(debug=True)

# then save the file
ESC :wq!

# create home.html file
mkdir statics
mkdir templates
cd templates
vi home.html
# input below
  <!DOCTYPE html>
  <html>
  <head>
    {% if title %}
      <title>{{ title }}</title>
    {% else %}
      <title>my home</title>
    {% endif %}
  </head>
  <body>
    {% for post in posts %}
      <h1>{{ post.title }}</h1>
      <p>By {{ post.author }} on {{ post.date_posted }}</p>
      <p>{{ post.content }}</p>
    {% endfor %}
  </body>
  </html>

# then save the file
ESC :wq!

# set app path
export FLASK_APP=app.py
# to stop fask
Control C
# to activate debug mode
export FLASK_DEBUG=1
# run Flask
flask run    # or python app.py
# then check localhost:5000/
```



