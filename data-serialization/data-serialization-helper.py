# Helper module with User class and additional functions
import contextlib
from datetime import date


# User Class
class User:
    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.address = None
        self.score = None

    # Print the object
    def __repr__(self):
        return str(self.__dict__)


# User object serialization
def serializeUser(object):
    if isinstance(object, User):
        return object.__dict__

    if isinstance(object, date):
        return object.__str__()


# Used For MiniDom
# Print the tags of a nodeList object
def printTags(nodeList):
    for node in nodeList:
        if node.nodeName != '#text':
            print(node.nodeName)


# Recursively print the node list childern's name (tag) and its value
def printNodes(nodeList, level=0):
    with open('structured-data.txt', 'a') as f:
        for node in nodeList:
            if node.nodeName != '#text':
                with contextlib.suppress(Exception):
                    print(("  ")*level + node.nodeName +
                          ':' + node.firstChild.data)
                    f.write(("  ")*level + node.nodeName +
                            ':' + node.firstChild.data + '\n')
                printNodes(node.childNodes, level+1)
