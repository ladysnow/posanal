import os
import sys
from distutils.core import setup 
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError


# fail safe compilation shamelessly stolen from the simplejson
# setup.py file.  Original author: Bob Ippolito



extra = {}
if sys.version_info >= (3, 0):
    extra['use_2to3'] = True


class BuildFailed(Exception):
    pass


def echo(msg=''):
    sys.stdout.write(msg + '\n')


#readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


def run_setup():
    features = {}
    setup(
        name='posanal',
        version='0.1',
        url='http://www.randstrom.com/',
        license='BSD',
        author='Malin Randstrom',
        author_email='malin@randstrom.com',
        description='Position analysis module for libreoffice calc',
        long_description="Position analysis module for libreoffice calc",
        packages=['posanal','posanal/utils','posanal/libre','posanal/examples'],
        #py_modules=[],
        classifiers = [
                           'Intended Audience :: Developers',
                           'Intended Audience :: Information Technology',
                           'License :: OSI Approved :: BSD License',
                           'Programming Language :: Python :: 3.3',
                           'Operating System :: OS Independent',
                           ],
    )

try:
    run_setup()
except BuildFailed:
    echo('Failure information, if any, is above.')
    echo()

