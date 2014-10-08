from setuptools import setup, find_packages

version = '0.2'

setup(
    name='txrestapi',
    version=version,
    description="Easing the creation of REST API services in Python",
    long_description="""\
""",
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='',
    author='Ian McCracken',
    author_email='ian.mccracken@gmail.com',
    url='http://github.com/iancmcc/txrestapi',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
