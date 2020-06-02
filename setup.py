from distutils.core import setup, Extension
vrapi = Extension('vrapi', sources=['bridge.c'])
setup(name = 'oqvr',
      packages = ['oqvr'],
       version = '1.0',
       description = 'A port of the Oculus Quest SDK',
       author = 'zurgeg',
       author_email = 'https://github.com/zurgeg/python-vrapi',
       ext_modules = [vrapi])
