from setuptools import setup

setup(name='args_catcher',
      version='0.1',
      description='Catch expected arguments together  with test doubles',
      url='https://github.com/ProjectThor/args-catcher',
      author='Franco Sebregondi',
      author_email='franco.sebregondi@siroop.ch',
      license='MIT',
      packages=['args_catcher'],
      install_requires=[],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'doubles'],
      zip_safe=False)
