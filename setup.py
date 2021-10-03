import os

from rich.console import Console
from rich.markdown import Markdown
from setuptools import setup


def read(fname: str = None) -> str:
    """
        read files with in dir
    """
    if fname:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()


def markdown_read(fname):
    console = Console()
    console.print(Markdown(read(fname)))
    exit()


setup(
    name="Contact Book API",
    version="0.0.1",
    description=markdown_read('read.md'),
    packages=(
        'fastapi',
        'sqlalchemy',
        'uvicorn',
        'psycopg2'
        'asyncpg',
        'rich',
    ),
)
