# Async is a non-blocking call and it will not block the execution of the program
#Non-blocking Waiting for the task to complete

# scope  HTTP, WebSocket, path, headers, query_string, client, server, extensions
# receive 
# send


# Sync is a blocking call and it will block the execution of the program
# Waiting for the task to complete


# Async is a non-blocking call and it will not block the execution of the program
#Non-blocking Waiting for the task to complete

# scope  HTTP, WebSocket, path, headers, query_string, client, server, extensions
# receive 
# send

async def app(scope, receive, send): # scope means request information 
    assert scope['type'] == 'http'

    try:
        await send({
            'type': 'http.response.start', # send response start
            'status': 200,
            'headers': [
                (b'content-type', b'text/plain'),
            ],
        })

        await send({
            'type': 'http.response.body', # send response body
            'body': b'Hello, ASGI World! and Python FastApi World!',
        })
    except Exception as e: # run  uvicorn file_name:function_name
        # run  uvicorn async:app --reload
        print(e)
