def lambda_handler(event, context):
    request = event['request']
    headers = request['headers']
    host = 'dewsk8drll354.cloudfront.net'  # Replace with your CloudFront domain name
    countryUrls = {
        'IN': f"https://{host}/IN/index.html",
        'FR': f"https://{host}/fr/index.html",
        'ES': f"https://{host}/es/index.html",
        # Add more country codes and URLs here
    }
    defaultUrl = f"https://{host}/default/index.html" # Change this to your default URL

    if 'cloudfront-viewer-country' in headers:
        countryCode = headers['cloudfront-viewer-country']['value']
        if countryCode in countryUrls:
            response = {
                'statusCode': '302',
                'statusDescription': 'Found',
                'headers': {
                    'location': {
                        'value': countryUrls[countryCode]
                    }
                }
            }

            return response

    # Redirect to default URL if viewer's country is not in dictionary
    response = {
        'statusCode': '302',
        'statusDescription': 'Found',
        'headers': {
            'location': {
                'value': defaultUrl
            }
        }
    }

    return response
