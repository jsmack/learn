import xmlrpc.client

with xmlrpc.client.ServerProxy('http://127.0.0.1:8000/') as proxy:
    print(proxy.xadd_num(10,20))