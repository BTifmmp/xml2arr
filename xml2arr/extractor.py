import re
import string
import xml.etree.ElementTree as ET


def extract(xml_file: string) -> list:
  tree = ET.parse(xml_file)
  root = tree.getroot()

  coordinates = []

  # Loops through each object
  for obj in root.findall('.//object'):
      xmin = obj.find('.//bndbox/xmin').text
      ymin = obj.find('.//bndbox/ymin').text
      xmax = obj.find('.//bndbox/xmax').text
      ymax = obj.find('.//bndbox/ymax').text

      # Append the coordinates
      coordinates.append([int(xmin), int(ymin), int(xmax), int(ymax)])
  
  return coordinates


def extract_to_file(xml_path: string, out_path: string, pprint: bool=False) -> None:
  result = extract(xml_path)
  with open(out_path, "w") as f:
    if pprint:
      f.write("\n".join([str(x) for x in result]))
    else:
      f.write(str(result))