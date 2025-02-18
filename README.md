# xml2arr
Extract bounding boxes from XML format.

## Instalation
```shell
pip install xml2arr
```

## Usage 
```python
from xml2arr import extract, extract_to_file

XML_PATH = "/path/to/xml/exmaple.xml"

# Result as a python list
result = extract(XML_PATH)

# Saved to output file
OUT_PATH = "/path/to/output"
extract_to_file(XML_PATH, OUT_PATH)

```

## Input
XML structure: 
```xml
<annotation>
	<folder>painted_nails</folder>
	<filename>n3.png</filename>
	<path>C:/Users/username/img/n3.png</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>0</width>
		<height>0</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>no</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>46</xmin>
			<ymin>294</ymin>
			<xmax>354</xmax>
			<ymax>718</ymax>
		</bndbox>
	</object>
<annotation>
```
## Output
Expected output, can be saved to file or returned as a list:
```python
[[46, 294, 354, 718]]
```