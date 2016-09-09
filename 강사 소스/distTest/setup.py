from distutils.core import setup, Extension

setup( name="myxml", version='1.0', py_modules=['myxml',] ,
       install_requires=['beautifulsoup4', ] )



# setup(name='mycextest',version='2.0', ext_package="myc",
#       ext_modules=[ Extension('extest',['extest.c'] )    ] )
# from setuptools import setup
# setup( name="myeasy", version='1.0', 
#        py_modules=['easy1','easy2'])
# setup( name="mywin", version='1.0', py_modules=['win1','win2'] )
# setup(name='lgpack',version='1.0', packages=['lg','lg.com', 'lg.ui'] )
# setup( name="my", version='1.0', py_modules=['my1','my2'] )