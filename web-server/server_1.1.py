#! /usr/bin/env python3
#-*- coding:utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    '''
    处理请求并返回页面的1.1版本中我们重新整理了一下代码
    把原来的一个函数分解成3个，让原来的页面按照我们设定的模板来显示
    '''

    #页面模板
    Page = '''\
        <html>
        <body>
        <table>
        <tr>  <td>Header</td>         <td>Value</td>          </tr>
        <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
        <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
        <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
        <tr>  <td>Command</td>        <td>{command}</td>      </tr>
        <tr>  <td>Path</td>           <td>{path}</td>         </tr>
        </table>
        </body>
        </html>'''


    #处理一个GET请求
    def do_GET(self):
        page = self.create_page()
        self.send_content(page)

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


    def send_content(self, page):
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
