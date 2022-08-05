from setuptools import setup, find_packages

setup(
    name="todo",
    version="1.0.0",
    description="Simple todo list manager",
    author="samfelt",
    url="https://github.com/samfelt/todo",
    packages=find_packages(exclude=("tests*",)),
    entry_points={
        "console_scripts": [
            "todo = todo.main:main",
            "t = todo.main:main",
        ]
    }
)

