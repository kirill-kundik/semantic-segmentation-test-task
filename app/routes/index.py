from flask import Blueprint, render_template

# Blueprint configuration
index_bp = Blueprint(
    'index_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@index_bp.route('/')
def main_page():
    return render_template('index.html')
