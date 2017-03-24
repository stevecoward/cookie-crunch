from distutils.core import setup

setup(
    name='cookie-crunch',
    version='0.1',
    author='Steve Coward',
    author_email='steve.coward@gmail.com',
    url='https://github.com/stevecoward/cookie-crunch',
    license='LICENSE',
    description='Simple extraction of data from session cookies, including Flask',
    long_description=open('README.txt').read(),
    packages=['cookie_crunch'],
)
