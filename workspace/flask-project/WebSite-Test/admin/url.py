from flask import Blueprint

from admin.views import admin_index

admin_blueprint = Blueprint('admin', __name__)

admin_blueprint.add_url_rule("/index", view_func=admin_index, methods=["POST"])
