from distutils.core import setup

setup(
    name='Twitter API CMSPlugin',
    version='0.1',
    pacakges=['cmsplugin-twitter'],
    license='copyright Tim Anderegg',
    long_description="""
        A plugin for DjangoCMS that uses the Twitter API to pull in content.
    """,
    install_requires=[
        'django>=1.6.5',
        'south>=0.8.4',
        'django-cms>=3.0.0',
        'python-twitter',
        'python-dateutil'
    ],
)
