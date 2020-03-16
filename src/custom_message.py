import json
import sys
import os

def main(event, context):
    print(event)
    print(dir(event))
    print(event["triggerSource"])
    print(event["response"])

    username_parameter = event["request"]["usernameParameter"]
    code_parameter = event["request"]["codeParameter"]

    custom_response = {}
    custom_response["emailMessage"] = "salut toi {0}{1}".format(username_parameter, code_parameter)
    custom_response["emailSubject"] = "subject"

    event["response"] = custom_response

    print("===========================>>>")
    print(event)
    print(dir(event))
    print(event["triggerSource"])
    print(event["response"])

    return event

if __name__ == "__main__":
    res = main('', '')
    print(res)