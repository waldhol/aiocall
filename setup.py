import os

from setuptools import setup

setup(name='aiocall',
      version='0.1',
      description='The missing call methods for python asyncio',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read().strip(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
      ],
      url='http://github.com/waldhol/aiocall',
      author='Holger Waldmann',
      author_email='holger.waldmann@web.de',
      license='Public Domain',
      packages=['aiocall'],
      zip_safe=False)
