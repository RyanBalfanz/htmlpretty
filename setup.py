"""
htmlpretty
----------

Prettify your HTML.
"""
from setuptools import setup


setup(
    name='htmlpretty',
    version='0.1.0',
    url='https://github.com/RyanBalfanz/htmlpretty',
    license='MIT',
    author='Ryan Balfanz',
    author_email='ryan@ryanbalfanz.net',
    description='Prettify your HTML.',
    long_description=__doc__,
    # packages=['htmlpretty.py'],
    # namespace_packages=['htmlpretty'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'BeautifulSoup',
    ],
    classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.7",
		"Topic :: Internet",
		"Topic :: Text Processing",
		"Topic :: Text Processing :: Markup :: HTML",
		"Topic :: Utilities",
    ]
)
