import json
import sys
import os

def main(_event, _context):
    alphabet = ['a', 'b', 'c']

    return {
        "statusCode": 200,
        "body": json.dumps(alphabet)
    }

if __name__ == "__main__":
    res = main('', '')
    print(res)