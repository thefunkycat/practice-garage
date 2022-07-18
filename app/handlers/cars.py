# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint(name='cars', import_name=__name__, url_prefix='/cars')


@bp.route('/', methods=["GET"])
def cars_get():
    pass
