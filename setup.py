from distutils.core import setup, Extension
vrapi = Extension('vrapi', sources=['VrApi.h','VrApi_Config.h','VrApi_Helpers.h','VrApi_Input.h','VrApi_SystemUtils.h','VrApi_Types.h','VrApi_Vulkan.h','VrApi_Version.h'])
setup(name = 'PackageName',
       version = '1.0',
       description = 'A port of the Oculus Quest SDK',
       author = 'zurgeg',
       author_email = 'https://github.com/zurgeg/python-vrapi',
       ext_modules = [vrapi])
