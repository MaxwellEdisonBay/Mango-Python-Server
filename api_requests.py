import json

from consts import ErrorCode


def respond (request, db):
    respond_json = {}

    method = request.headers['Request-Type']
    data = request.get_json()

    if method == 'api-test':
        print(data)
        respond_json['test'] = 'ok'
        return respond_json, ErrorCode.OK
    elif method == 'create-user':
        print(data)
        db.createUser(data["uid"], data)
        return respond_json, ErrorCode.OK

