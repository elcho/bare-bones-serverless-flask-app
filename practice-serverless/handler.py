def hello(event, context):
    try:
        return dict(
            statusCode=200,
            body='HELLO FROM MY SERVERLESS HANDLER!!'
        )
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )

