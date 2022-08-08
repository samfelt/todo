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
            "todo = todo.__main__:main",
            "t = todo.__main__:main",
        ]
    },
)
