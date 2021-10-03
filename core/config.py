import os

from pydantic import BaseSettings


class Config(BaseSettings):
    service_name: str = os.environ.get('secret_key')
    secret_key: str = os.environ.get('secret_key')


config = Config()
