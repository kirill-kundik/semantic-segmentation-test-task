from flask import Blueprint, render_template

# Blueprint configuration
api_bp = Blueprint(
    'api_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@api_bp.route('/semantic_segmentation')
def main_page():
    return {'success': True}
