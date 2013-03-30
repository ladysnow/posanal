import os
import sys
from distutils.core import setup 
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

class BuildFailed(Exception):
    pass


def echo(msg=''):
    sys.stdout.write(msg + '\n')


#readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
        name='posanal',
        version='0.1',
        url='http://www.randstrom.com/',
        license='BSD',
        author='Malin Randstrom',
        author_email='malin@randstrom.com',
        description='Position analysis module for libreoffice calc',
        long_description="Position analysis module for libreoffice calc",
        packages=['posanal','posanal/utils','posanal/libre','posanal/examples']
    )


