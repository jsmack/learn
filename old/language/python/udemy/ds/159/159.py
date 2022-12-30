from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:

    def add_num(x ,y):
        print( x + y)
        return x + y

    server.register_function(add_num, "xadd_num")
    server.serve_forever()