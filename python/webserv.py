#!/usr/bin/env python3

"""
simple cgi server
Usage: ./cgiserver.py
"""

import http.server
import logging
import sys


class httpserv:
    def __init__(self):
        print("init")
    def run(self):

        IPADDRESS = ""
        PORT = 8000
        SERV_ADDRESS = (IPADDRESS, PORT)

        logging.basicConfig(level=logging.INFO,
                            filename="/home/ec2-user/testapp/info.log")

        handler = http.server.CGIHTTPRequestHandler
        serv = http.server.HTTPServer(SERV_ADDRESS, handler)

        logging.info('start http...')

        try:
            serv.serve_forever()
        except KeyboardInterrupt:
            pass
        except:
            logging.info(sys.exc_info())

        serv.server_close()
        logging.info('stoped httpd...orz')

if __name__ == '__main__':
    httpserv().run()
