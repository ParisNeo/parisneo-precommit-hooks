from setuptools import setup, find_packages

setup(
    name='parisneo-precommit-hooks',
    version='0.1.0',
    packages=find_packages(),
    author='ParisNeo',
    author_email='parisneo@gmail.com',
    description='ParisNeo\'s Custom Pre-commit Hooks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ParisNeo/parisneo-precommit-hooks',
    install_requires=[
        'black',
        'flake8',
        'isort',
        'pylint',
        'eslint',
        'prettier'
    ],
    entry_points={
        'console_scripts': [
            'parisneo-python-check=parisneo_hooks.python_hooks:python_style_check',
            'parisneo-js-check=parisneo_hooks.js_hooks:js_style_check',
        ],
    },
)
