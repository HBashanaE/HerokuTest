from flask import Blueprint, jsonify, request


SUB_BLUEPRINT = Blueprint('SB', __name__)

@SUB_BLUEPRINT.route('/test', methods=['GET'])
def Test():
    """
    Test
    """

    result = "\
        <html>\
            <head><title>Hello World</title></head>\
                <body>\
                    <h1>Hi there</h1></body>\
                        </html>"

    resp = {'result': result}
    return result