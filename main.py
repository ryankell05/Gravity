from flask import *
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def main_route():
  options = { "message": "hello world" }
  return render_template("index.html", **options)

@app.route('/services')
def services_route():
	options = { "messages": "Hello services" }
	return render_template("services.html", **options)