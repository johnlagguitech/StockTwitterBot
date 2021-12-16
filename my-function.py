import json

def lambda_handler(event, context):
    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps({
            "abc": ip.status_code,
            "message": os.environ.get('MyParam')
        }),
    }
