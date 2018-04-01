from setuptools import setup, find_packages

from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='tensortweeter',

    version='3.0',

    description='TensorTweeter',
    long_description="TensorTweeter",


    url='http://metrolinx.com',


    author='chin',
    author_email='chin@chin.com',


    license='Copyright',


    classifiers=[
        'Development Status :: 1 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',



        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],


    packages=find_packages(exclude=['tests']),


    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    py_modules=["__main__"],

    entry_points={
        'console_scripts': [
            'tensor_tweeter = entry_to_app.__main__:main'
        ],
    },
)

# Copy the main file to the dist directory
#from shutil import copyfile
#copyfile("main.py", "dist/main.py")