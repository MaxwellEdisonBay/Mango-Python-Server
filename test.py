import requests
import sys
import uuid
from cryptography.fernet import Fernet
std_base = "http://www.mango-friends.com//"
std_req = "testapi/dima/21"


def send_request(req=std_req, base=std_base):
    response = requests.get(base + req)
    print(response.json())


def test_api(subdomain, url, req_type):
    request_type = {"Request-Type": req_type}
    request_data = {"uid":str(uuid.uuid4()), "name":"test", "sirname":"test_sirname"}
    response = requests.post("http://" + subdomain + '.' + url, json=request_data, headers=request_type)
    print(response.status_code)
    # print(response.json())


if __name__ == "__main__":
    # test_api("api", "mango.test:5000", "create-user")
    test_api("api", "mango-friends.com", "create-user")

    # test_api("api", "mango.test:5000", "bad-request")
    # test_api("api","mango-friends.com")
    # send_request()
    # args = sys.argv
    # argn = len(args)
    # if argn == 3:
    #     send_request(args[1], args[2])
    # elif argn == 2:
    #     send_request(req=args[1])
    # elif argn == 1:
    #     send_request()
    # else:
    #     print("Bad too many arguments", file=sys.stderr)
