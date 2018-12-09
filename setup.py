import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wayback_scraper",
    version="1.1",
    license='MIT',
    author="Ramaswamy Venkatachalam",
    author_email="ramasamynasa@gmail.com",
    description="A command line utility for scraping wayback snapshots from archive.org.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chocolatebrown/wayback_scraper",
    packages=setuptools.find_packages(),
    entry_points={
          'console_scripts': ['wayback-scraper = wayback_scraper.wayback_scraper:main'],
      },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
