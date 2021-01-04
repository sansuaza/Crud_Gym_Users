from setuptools import setup


setup(
    name= 'gym',
    version='0.1',
    py_modules=['gym'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gym=gym:cli
    ''',

)