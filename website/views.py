
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# define the function home with a "decorator" so home will be called when '/' is used
@views.route('/')
def home():
    return render_template("home.html")



