from setuptools import setup

long_description = open('README.rst').read()

setup(name="python-votesmart",
      version="0.3.3",
      py_modules=["votesmart"],
      description="Libraries for interacting with the Project Vote Smart API",
      author="James Turk <jturk@sunlightfoundation.com>",
      author_email = "jturk@sunlightfoundation.com",
      license="BSD",
      url="http://github.com/votesmart/python-votesmart/",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.5"
                   ],
       install_requires=["requests >= 2.26"]
      )

