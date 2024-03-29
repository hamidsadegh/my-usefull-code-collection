import sys
from helper import *
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import yaml
import json

# Main function
if __name__ == "__main__":
    print('###### YAML ######')

    # Open the user.yaml file as read only
    with open('user.yaml') as yamf:
        user_yaml = yaml.safe_load(yamf)
        # Load the stream using safe_load

    # Print the object type
    print("Type of user_yaml variable:")
    print(user_yaml)
    print('----------------------')

    # Iterate over the keys of the user_yaml and print them
    print('Keys in user_yaml:')
    for key in user_yaml:
        print(key)
    print('----------------------')

    # Create a new instance of class User
    user = User()
    # Assign values form the user_yaml to the object user
    user.id = user_yaml['id']
    user.first_name = user_yaml['first_name']
    user.last_name = user_yaml['last_name']
    user.birth_date = user_yaml['birth_date']
    user.score = user_yaml['score']
    user.address = user_yaml['address']

    # Print the user object
    print('User object:')
    print(user)
    #########################################
    #              Procedure 3              #
    #########################################
    print('##################')
    print('###### JSON ######')
    print('##################')

    # Create JSON structure from the user object
    user_jason = json.dumps(user, default=serializeUser,
                            indent=4, sort_keys=True)
    # Print the created JSON structure
    print('Print user_json:')
    print(user_jason)
    print('----------------------')

    # Create JSON structre with indents and soreted keys
    print('JSON with indents and sorted keys')
    print(user_jason)
    #########################################
    #              Procedure 4              #
    #########################################
    print('######################')
    print('# XML - Element Tree #')
    print('######################')

    # Parse the user.xml file
    tree = ET.parse('user.xml')
    # Get the root element
    root = tree.getroot()
    # Print the tags
    print('Tags in the XML:')
    for element in root:
        print(element.tag)
    print('----------------------')
    # Print the value of id tag
    print('id tag value:')
    print(tree.find('id').text)
    print('----------------------')

    # Find all elements with the tag address in root
    for element in root:
        print(element.tag, ':', tree.find(element.tag).text)
    # Print the adresses in the xml
    print('Addresses:')
    addresses = root.findall('address')
    for address in addresses:
        for i in address:
            print(i.tag, ':', i.text)
    print('----------------------')

    # Print the elements in root with their tags and values
    print('Print the structure')
    for k in root.iter():
        print(k.tag, ':', k.text)
    # Parsing XML files with MiniDOM
    print('######################')
    print('### XML - MiniDOM ####')
    print('######################')

    # Parse the user.xml file
    dom = MD.parse('user.xml')
    # Print the tags
    for node in dom.childNodes:
        printTags(node.childNodes)

    print('----------------------')
    # Accessing element value
    print('Accessing element value')
    idElements = dom.getElementsByTagName('id')
    print(idElements)
    elementId = idElements.item(0)
    print(elementId.childNodes)
    idValue = elementId.firstChild.data
    print(idValue)
    print('----------------------')

    # Print elements from the DOM with tag name 'address'
    print('Addresses:')

    print('----------------------')

    #########################################
    # Print the entire structure with printNodes
    dom = MD.parse('switch-ncclient-out.xml')
    print('Print the structure')
    count = 0
    for node in dom.childNodes:
        printNodes(node.childNodes)
    ########################################

    # Print the entire structure with printNodes
    print('The structure:')

    #########################################
    #              Procedure 5              #
    #########################################
    print('######################')
    print('#   Use Namespaces   #')
    print('######################')

    # Parse the user.xml file
    itemTree = ET.parse('item.xml')
    # Get the root element
    root = itemTree.getroot()
    # Define namespaces
    namespaces = {'a': 'https://www.example.com/network',
                  'b': 'https://www.example.com/furniture'}
    # Set table as the root element
    elementsInNSa = root.findall('a:table', namespaces)
    elementsInNSb = root.findall('b:table', namespaces)
    # Elements in NS a
    print('Elements in NS a:')
    for e in elementsInNSa:
        for i in e.iter():
            print(f'{i.tag}:{i.text}')
    print('----------------------')

    # Elements in NS b
    print('Elements in NS b:')
    for e in elementsInNSb:
        for i in e.iter():
            print(f'{i.tag}:{i.text}')

