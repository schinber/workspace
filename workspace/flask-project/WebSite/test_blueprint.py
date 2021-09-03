# -*- coding: utf-8 -*-
from flask import Blueprint

test_blueprint = Blueprint('fir_blueprint', __name__)


@test_blueprint.route('/test', methods=['POST'])
def test():
    return "test success"
