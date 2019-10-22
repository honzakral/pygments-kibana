# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="pygments-kibana",
    author="Honza Král",
    author_email="honza.kral@gmail.com",
    version="0.0.1",
    license="Apache License, Version 2.0",
    url="https://github.com/honzakral/pygments-kibana",
    packages=["pygments_kibana"],
    install_requires=["Pygments"],
    description="Pygments lexer for Kibana Console input",
    long_description="Pygments lexer for Kibana Console input",
    entry_points={"pygments.lexers": ["release = pygments_kibana.kibana_lexer:KibanaLexer"]},
)
