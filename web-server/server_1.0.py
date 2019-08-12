#! /usr/bin/env python3
#-*- coding:utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    '''
    处理请求并返回页面
    这里定义了一个类，继承了BaseHTTPRequestHandler类
    来返回page的内容
    '''

    #页面模板
    Page = '''\
        <html>
        <body>
        <p>Hello, web! </p>
        </body>
        </html>
    '''

    #处理一个GET请求
    def do_GET（self):
        '''
        通过确定请求的方法来调用其对应的函数，比如方法是GET那么该类就会调用名为do_GET的方法
        这里是重写了do——GET方法
        content-type告诉了客户端要以处理html文件的方式处理返回的内容
        end_headers方法会插入一个空白行
        page.encode告诉了客户端page的编码方式
        '''
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))

if __name__ == '__main__':
    serverAddress = ('',8080)
    server =HTTPServer(serverAddress, RequestHanlder)
    server.serve_forever()
