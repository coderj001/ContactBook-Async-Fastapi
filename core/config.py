import os
from distutils.util import strtobool

from pydantic import BaseSettings


class Config(BaseSettings):
    service_name: str = os.environ.get('service_name')
    secret_key: str = os.environ.get('secret_key')
    db_url: str = os.environ.get('db_url')
    debug: bool = strtobool(os.environ.get('debug'))


config = Config()
