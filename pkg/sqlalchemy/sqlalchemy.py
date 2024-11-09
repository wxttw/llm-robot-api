"""
@Time     : 2024-11-06 12:53
@Author   : jay
@File     : sqlalchemy.py
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    """重写flask_sqlalchemy的核心类，实现自动提交"""

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
