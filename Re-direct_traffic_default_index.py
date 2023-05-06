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



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Other way>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    uri = request['uri']
    ends_with_slash = uri.endswith('/')

    if ends_with_slash or not '.' in uri:
        request['uri'] = f"{uri}{'' if ends_with_slash else '/'}index.html"
        return request
    elif uri.rsplit('/', 1)[-1] != 'index.html':
        request['uri'] = f"{uri}/index.html"
        return request
    else:
        return request
