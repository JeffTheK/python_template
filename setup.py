from setuptools import setup

setup(
    name = "$name",
    version = "0.1.0",
    description = "TODO",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/$name",
    packages = ["$name"],
    entry_points = {
        'console_scripts': [
            '$name = $name.__main__:main'
        ]
    },
    package_data = {
        "$name": [
            "data/*/*"
        ]
    }
)