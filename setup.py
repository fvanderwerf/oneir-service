
from setuptools import setup

import subprocess

git_commit_time = subprocess.check_output("git log -1 --format=%ci | awk '{ print $1 $2 }' | tr -cd [0-9]", shell=True) 

setup(
        name='oneir-service',
        version='0.1.dev' + git_commit_time,
        description='oneir-service',
        author='Fabian van der Werf',
        author_email='fvanderwerf@gmail.com',
        py_modules=['oneir'],
        scripts=['bin/oneird'],
        install_requires=[
                "Flask==0.10.1",
                "pika==0.10.0"
            ]
        )
