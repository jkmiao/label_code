#!/usr/bin/env python
# encoding: utf-8

import tornado.httpserver
import tornado.options
import tornado.web
from tornado.options import define,options
import os
from apicode import Apicode

define("port", default=8088, help="run on the given port", type=int)

class VcodeLabelHandler(tornado.web.RequestHandler):
    def get(self):

        labelMsg = vcode.get_labelmsg()

        self.render('label_code.html', **labelMsg)

    def post(self):

        result = self.get_argument('result', '')
        fname = self.get_argument('fname', '')

        # 验证输入
        if fname and len(result)>1:
            print 'fname',fname
            labelMsg = vcode.get_labelmsg(fname, result)
            self.render('label_code.html', **labelMsg)
        else:
            print '更新失败', result, fname
            self.write('<h1>error: 验证码输入必须大于1位!</h1>')


if __name__ == "__main__":

    vcode = Apicode() 

    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [(r'/', VcodeLabelHandler),],
        template_path = os.path.join(os.path.dirname(__file__),"templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
        autoescape=None,
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print "starting tornado at port http://127.0.0.1:%d" % options.port
    tornado.ioloop.IOLoop.instance().start()


