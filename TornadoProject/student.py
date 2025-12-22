import json

import tornado


class StudentHandler(tornado.web.RequestHandler):
    """
    学生处理类
    """
    def post(self):
        # 可以获取请求数据并返回响应
        content_type = self.request.headers.get("Content-Type", "")
        if "application/json" in content_type:
            try:
                payload = json.loads(self.request.body.decode('utf-8'))
                student_name = payload.get("name", "")
                student_age = payload.get("age", "")
                response = {
                    "status": "success",
                    "message": f"Student {student_name} added successfully",
                    "data": {
                        "name": student_name,
                        "age": student_age
                    }
                }
                self.write(response)
            except json.JSONDecodeError:
                self.set_status(400)
                self.write({"status": "error", "message": "Invalid JSON format"})

