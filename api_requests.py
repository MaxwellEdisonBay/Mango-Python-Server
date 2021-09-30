from consts import ErrorCode


def respond (request, db):
    respond_json = {}

    method = request.headers['Request-Type']
    data = request.get_json()

    if method == 'api-test':
        respond_json['test'] = 'ok'
        return respond_json, ErrorCode.OK
    elif method == 'create-user':
        db.createUser(data["uid"], data)
        print(data)
        return respond_json, ErrorCode.OK

