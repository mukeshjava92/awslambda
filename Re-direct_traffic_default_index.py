def lambda_handler(event, context):
    # Extract the request from the CloudFront event that is sent to Lambda@Edge
    request = event['Records'][0]['cf']['request']

    # Extract the URI from the request
    old_uri = request['uri']

    # Match any '/' that occurs at the end of a URI. Replace it with a default index
    new_uri = old_uri.rstrip('/') + '/index.html' if old_uri.endswith('/') else old_uri
    
    # Log the URI as received by CloudFront and the new URI to be used to fetch from origin
    print("Old URI: " + old_uri)
    print("New URI: " + new_uri)

    # Replace the received URI with the URI that includes the index page
    request['uri'] = new_uri

    # Return to CloudFront
    return request
