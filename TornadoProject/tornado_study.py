# -*- coding:utf-8 -*-
"""
tornado 学习.
"""
import json

import tornado.web
import tornado.ioloop

from TornadoProject.student import StudentHandler

"""
get请求中write函数和streamlit.write的异同：
    相似点
    输出内容: 两者都用于向用户界面输出内容
    简单易用: 都提供了简单直观的方式来显示文本信息
    自动渲染: 都能自动将内容渲染到前端界面
    不同点
    tornado.web.RequestHandler.write()
    属于 Web 框架 的响应机制
    将内容写入 HTTP 响应体
    需要客户端发起请求才能看到输出
    输出到浏览器页面
    streamlit.write()
    属于 数据应用框架 的 UI 组件
    直接渲染到 Web 应用界面
    支持多种数据类型（DataFrame、图表等）
    更丰富的可视化能力
    总结
    虽然两者都叫 write 并且都用于输出内容，但它们的应用场景和工作机制不同：
    tornado 的 write 是服务器响应的一部分
    streamlit 的 write 是构建用户界面的工具
"""


# 定义处理类型
class IndexHandler(tornado.web.RequestHandler):
    """
    IndexHandler
    """

    # 添加一个处理get请求方式的方法
    def get(self):
        # 向响应中，添加数据
        self.write("好看的皮囊千篇一律，有趣的灵魂万里挑一。")

    def post(self):
        """
        接收json数据
        响应字符串
        """
        # 检查请求内容类型
        content_type = self.request.headers.get("Content-Type", "")

        if "application/json" in content_type:
            # 处理JSON数据
            try:
                data = json.loads(self.request.body.decode('utf-8'))
                message = data.get("data", "No data received")
                self.write(f"Received JSON data: {message}")
            except json.JSONDecodeError:
                self.write("Invalid JSON format")
        else:
            # 处理表单数据
            data = self.get_body_argument("data", default="No data received")
            self.write(f"Received POST data: {data}")


if __name__ == '__main__':
    # 创建一个应用对象

    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/student', StudentHandler)
    ])

    # 绑定一个监听端口
    app.listen(8888)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()
