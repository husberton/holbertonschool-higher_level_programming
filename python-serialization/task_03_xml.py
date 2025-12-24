import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """ Serialize a dictionary to an XML file """
    root = ET.Element("root")
    for key, value in dictionary.items():
        item = ET.SubElement(root, "item", key=str(key))
        item.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)
    return "The data has been serialized and saved to 'data.xml'"

def deserialize_from_xml(filename):
    """ Deserialize an XML file to a dictionary """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for item in root.findall("item"):
        key = item.get("key")
        value = item.text
        dictionary[key] = value
    return dictionary   