from flask import *

main = Blueprint('main', __name__, template_folder='templates')



@main.route('/')
def main_route():
  options = { "message": "hello world" }
  return render_template("index.html", **options)
