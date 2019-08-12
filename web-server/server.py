#! /usr/bin/env python3
#-*- coding:utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer
import sys,os

class ServerException(Exception):
    '''
    服务器内部错误
    由于我们现在的web服务器还不能处理异常的发生，比如找不到文件还是会返回299
    所以这款添加一个类来处理404这样的情况
    '''
    pass

class RequestHandler(BaseHTTPRequestHandler):
    '''
    处理请求并返回页面的1.1版本中我们重新整理了一下代码
    把原来的一个函数分解成3个，让原来的页面按照我们设定的模板来显示
    '''

    #页面模板
    Error_Page = '''\
        <html>
        <body>
        <h1> Error accessing {path} </h1>
        <p>{mag}</p>
        </body>
        </html>
        '''



    #处理一个GET请求
    def do_GET(self):
        '''
        首先看完整路径的代码，os.getcwd()是当前的工作目录，self.path保存了请求的相对路径，这是继承BaseHTTPRequestHandler里面的功能来的
        '''
        try:
            #文件完整的路径
            full_path = os.getcwd() + self.path

            #如果该路径不存在
            if not os.path,exists(full_path):
                #抛出异常：文件未找到
                raise ServerException("'{0}' not found".format(self.path))

                #如果该路径是一个文件
            elif os.path.isfile(full_path):
                #调用handle_file 处理该文件
                self.handle_file(full_path)

            #如果该路径不是一个文件
            else:
                #抛出异常：该路径为不知名对象
                raise ServerException("Unknow object '{0}'".format(self.path))

        #处理异常
        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path = self.path, msg =msg)
        self.send_content(content.encode('utf-8'),404)

    def create_page(self):
        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path
        }
        page = self.Page.format(**values)
        return page


    def send_content(self,content, status = 200):
        '''
        通过确定请求的方法来调用其对应的函数，比如方法是GET那么该类就会调用名为do_GET的方法
        这里是重写了do——GET方法
        content-type告诉了客户端要以处理html文件的方式处理返回的内容
        end_headers方法会插入一个空白行
        page.encode告诉了客户端page的编码方式
        '''
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

if __name__ == '__main__':
    serverAddress = ('',8080)
    server =HTTPServer(serverAddress, RequestHanlder)
    server.serve_forever()
