from setuptools import setup, find_packages

VERSION = '0.1.4'

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name="xml2arr", 
  version=VERSION,
  author="Blazej Turczynowicz",
  author_email="blazejturczynowicz@gmail.com",
  description="Extract bounding boxes from XML format to list",
  packages=find_packages(),
  long_description=long_description,
  long_description_content_type='text/markdown',
  keywords=['bounding box', 'xml', 'xml2arr'],
)