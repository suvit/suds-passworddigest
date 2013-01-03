# -*- coding: utf-8 -
#
# This file is part of suds-passworddigest released under the MIT license. 
# See the NOTICE for more information.

import os
import sys
from setuptools import setup, find_packages

from suds_passworddigest import VERSION


setup(
    name='suds_passworddigest',
    version=VERSION,
    description='adds Web Services Security'
                ' PasswordDigest authentication to SUDS',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='Victor Safronovich',
    author_email='vsafronovich@gmail.com',
    license='MIT',
    url='http://github.com/suvit/suds-passworddigest',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=['suds'],
    include_package_data=True,
)
