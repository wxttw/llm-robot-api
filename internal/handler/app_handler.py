"""
@Time     : 2024-11-03 11:55
@Author   : jay
@File     : app_handler.py
"""
import os
import uuid
from dataclasses import dataclass

from injector import inject
from openai import OpenAI

from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字为{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功更新，名字为{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，名字为{app.name}")

    def completion(self):
        """聊天窗口"""
        # 1.提取从接口中获取的输入，POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2.构建OpenAI客户端，并发起请求
        client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"))

        # 3.得到请求响应，然后将OpenAI的响应传递给前端
        # open ai: gpt-3.5-turbo-16k
        # moon shot: moonshot-v1-32k
        completion = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {"role": "system", "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的消息"},
                {"role": "user", "content": req.query.data}
            ]
        )
        content = completion.choices[0].message.content

        return success_json({"content": content})

    def ping(self):
        # raise FailException("数据未找到")
        return {"ping": "pong"}
