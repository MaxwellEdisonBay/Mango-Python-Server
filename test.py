import requests
import sys

std_base = "https://mango-friends.herokuapp.com/"
std_req = "testapi/ivan/20"


def send_request(req=std_req, base=std_base):
    response = requests.get(base+req)
    print(response.json())


if __name__ == "__main__":
    args = sys.argv
    argn = len(args)
    if argn == 3:
        send_request(args[1], args[2])
    elif argn == 2:
        send_request(req=args[1])
    elif argn == 1:
        send_request()
    else:
        print("Bad too many arguments", file=sys.stderr)
