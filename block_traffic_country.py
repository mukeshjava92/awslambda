import json

def lambda_handler(event, context):
    # Replace "XX" with the two-letter country code that you want to block traffic from
    blocked_country = "IN"

    # Check if the request is coming from the blocked country
    if "headers" in event and "CloudFront-Viewer-Country" in event["headers"]:
        country_code = event["headers"]["CloudFront-Viewer-Country"]
        if country_code == blocked_country:
            # Return a 403 HTTP status code to block the request
            return {
                "statusCode": 403,
                "body": "Access denied"
            }

    # Return a 200 HTTP status code to allow the request
    return {
        "statusCode": 200,
        "body": "Hello, world!"
    }
