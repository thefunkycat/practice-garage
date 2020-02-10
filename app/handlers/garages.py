from flask import Blueprint, abort, jsonify, request
from shared.model.garage import Garage

bp = Blueprint(name='garages', import_name=__name__, url_prefix='/garages')

# @garages.route('/', defaults={'page': 'index'})
@bp.route('/', methods=["GET"])
def garage_list():
    print(request.args)
    if request.args and 'garage' in request.args:
        garage = Garage.get(key=request.args.get('garage'))
        return jsonify({
            'id': garage.id,
            'name': garage.name,
            'brand': garage.brand,
            'postal_country': garage.postal_country
        })
    return jsonify(
        [
            {
                'id': g.id,
                'name': g.name,
                'brand': g.brand,
                'postal_country': g.postal_country
            } for g in Garage.list()
        ]
    )


@bp.route('/', methods=["POST"])
def garage_add():
    garage = Garage.add(props=request.json)
    return garage_list()

@bp.route('/', methods=["PUT"])
def garage_update():
    props = request.json
    garage = Garage.get(key=props.pop('id'))
    # print(garage)
    garage.update(props=props)
    return garage_list()

@bp.route('/', methods=["DELETE"])
def garage_delete():
    garage = Garage.get(key=request.json.pop('garage'))
    garage.delete()
    return garage_list()
