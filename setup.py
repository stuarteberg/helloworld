from setuptools import setup

## HINT: py2app is smart enough to recognize that some packages, like numpy,
##       should not be zipped up.  That is, they should *not* be forced into 
##       helloworld.app/Contents/Resources/lib/python2.7/site-packages.zip
## 
##       However, py2app doesn't know about your own packages.  If you have 
##       a package that fails to import correctly in the final app, try forcing
##       py2app to leave it alone (not zipped) by using the following py2app 
##       'recipe' code.
##
# class exclude_from_zipped_packages(object):
#     def __init__(self, module):
#         self.module = module
# 
#     def check(self, dist, mf):
#         m = mf.findNode(self.module)
#         if m is None:
#             return None
# 
#         # Don't put the module in the site-packages.zip file
#         return dict(
#             packages=[self.module]
#         )
# 
# import py2app.recipes
# py2app.recipes.some_package_that_cant_be_zipped = exclude_from_zipped_packages('some_package_that_cant_be_zipped')

OPTIONS = { 'dist_dir' : 'dist',
            'site_packages' : False,
            'argv_emulation': False, # argv_emulation interferes with gui apps
            'iconfile' : 'resources/Tsukasa-Tux-Daft-Punks-Thomas-Hello.icns', # http://www.iconarchive.com/tag/hello-world
            'alias': False }

setup(name='helloworld',
      app=['helloworld/main.py'],
      options={'py2app': OPTIONS},
      version='0.1',
      description='A simple greeting using pyqt',
      author='Stuart Berg',
      author_email='stuarteberg@gmail.com',
      url='github.com/stuarteberg/helloworld',
      packages=['helloworld']
     )
