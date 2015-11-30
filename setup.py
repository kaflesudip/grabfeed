from setuptools import setup
setup(
    name='grabfeed',
    packages=['grabfeed'],
    version='0.3.1',
    description='Detects and return RSS feeds for a given website.',
    author='Sudip Kafle',
    author_email='soodip.kafle@gmail.com',
    url='https://github.com/kaflesudip/grabfeed',
    download_url='https://github.com/kaflesudip/grabfeed/tarball/0.3.1',
    keywords=['RSS', 'Feeds', 'Scraping'],
    install_requires=[
        'beautifulsoup4==4.4.1',
        'requests==2.8.1'
    ],
    classifiers=[],
)
