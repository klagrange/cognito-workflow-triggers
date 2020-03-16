import json
from functools import wraps
import jsonschema
import boto3
from lambda_decorators import LambdaDecorator

CLIENT_DYNAMODB = boto3.client('dynamodb')

ERRORS = {
    # CLIENT_COGNITO_IDP.exceptions.UsernameExistsException: {
    #     "statusCode": 400,
    #     "type": "UsernameExistsException",
    # },
    # CLIENT_COGNITO_IDP.exceptions.InvalidParameterException: {
    #     "statusCode": 400,
    #     "type": "InvalidParameterException",
    # },
    # CLIENT_COGNITO_IDP.exceptions.ExpiredCodeException: {
    #     "statusCode": 400,
    #     "type": "ExpiredCodeException",
    # },
    # CLIENT_COGNITO_IDP.exceptions.NotAuthorizedException: {
    #     "statusCode": 401,
    #     "type": "NotAuthorizedException",
    # },
    # CLIENT_GATEWAY.exceptions.NotFoundException: {
    #     "statusCode": 400,
    #     "type": "NotFoundException",
    # }
}

class GatewayHandler(LambdaDecorator):
    @staticmethod
    def errors(exception):
        exception_type = type(exception)
        if exception_type in ERRORS.keys():
            error = ERRORS[exception_type]
            return {
                "statusCode": error["statusCode"],
                "body": json.dumps({
                    "type": error["type"],
                    "message": str(exception)
                })
            }

        custom_args = exception.args
        if len(custom_args) == 1 and isinstance(custom_args[0], dict):
            args = custom_args[0]
            status_code = args["statusCode"] if "statusCode" in args.keys() else 400
            return {
                "statusCode": status_code,
                "body": json.dumps({
                    "type": args["type"],
                    "message": args["message"]
                })
            }

        return {
            "statusCode": 500,
            "body": json.dumps({
                "type": "NotCaptured",
                "message": str(exception)
            })
        }

    @staticmethod
    def on_exception(exception):
        return GatewayHandler.errors(exception)


def jsonschema_validate(instance, schema):
    try:
        jsonschema.validate(instance=instance, schema=schema)
    except jsonschema.ValidationError as exception:
        raise Exception({
            "type": "RequestValidationError",
            "message": exception.message
    })

def json_schema_validator(request_schema_body=None, request_schema_path_params=None):
    def wrapper_wrapper(handler):
        @wraps(handler)
        def wrapper(event, context):
            print(event)
            print(request_schema_path_params)
            if request_schema_body is not None:
                jsonschema_validate(event["body"], request_schema_body)
            if request_schema_path_params is not None:
                jsonschema_validate(event["pathParameters"], request_schema_path_params)  
            response = handler(event, context)
            return response
        return wrapper
    return wrapper_wrapper
