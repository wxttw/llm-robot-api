"""
@Time     : 2024-11-05 21:27
@Author   : jay
@File     : module.py
"""

from flask_migrate import Migrate
from injector import Module, Binder

from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
