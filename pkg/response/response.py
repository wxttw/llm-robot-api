"""
@Time     : 2024-11-05 14:58
@Author   : jay
@File     : response.py
"""
from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from pkg.response.http_code import HttpCode


@dataclass
class Response:
    """基础HTTP接口相应格式"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Any = None):
    """基础的响应接口"""
    return jsonify(data), 200


def success_json(data: Any = None):
    """成功的响应接口"""
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    """失败的响应接口"""
    return json(Response(code=HttpCode.FAIL, message="", data=data))


def validate_error_json(errors: dict = None):
    """数据验证错误的响应接口"""
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATE_ERROR, message=msg, data=errors))


def message(code: HttpCode = None, msg: str = ""):
    """基础的消息响应，固定返回消息提示， 数据固定为空字典"""
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    """成功的消息响应"""
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """失败的消息响应"""
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    """未找到的消息响应"""
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    """未授权的消息响应"""
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    """无权限的消息响应"""
    return message(code=HttpCode.FORBIDDEN, msg=msg)