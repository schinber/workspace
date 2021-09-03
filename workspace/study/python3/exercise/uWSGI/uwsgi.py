# coding:utf-8


def application(environ, start_response):
    status = "200 OK"
    output = "Hello World!"

    response_headers = [("Content-type", "text/plain"),
                        ("Content-Length", str(len(output)))]
    return [output]
