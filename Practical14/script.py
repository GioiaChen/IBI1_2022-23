from xml.dom.minidom import parse
import xml.dom.minidom
from pandas import DataFrame

# Create four lists to store the information from the xml file.
id_list = []
name_list = []
definition_list = []
childnodes_list = []

# Read the file and get the elements by searching for "term".
go = xml.dom.minidom.parse("C:/Users/gioia/Desktop/IBI1/Practical 14/go_obo.xml")
obo = go.documentElement
terms = obo.getElementsByTagName("term")

# Define a function to calculate the number of childnodes.
dic = {}  # Create a dictionary to store all the "is_a" information.
def calculate(list):
    for i in list:
        if i in list:
            if i not in nodes:
                nodes.append(i)
                if i in dic:
                    calculate(dic[i])  # Reuse the function to achieve a cycle in calculation.
    return len(nodes)  # The number of nodes is represented by the length of the list called nodes.

# Create a dictionary to store all the ids with their "is_a" data.
for term in terms:
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    subordinate = term.getElementsByTagName('is_a')
    is_a_list = []
    for i in subordinate:
        is_a_list.append(i.childNodes[0].data)
    for is_a in is_a_list:
        if is_a not in dic:
            dic[is_a] = [id]
        else:
            dic[is_a].append(id)

# Extract the required elements.
for term in terms:
    id = term.getElementsByTagName('id')[0].childNodes[0].data
    name = term.getElementsByTagName('name')[0].childNodes[0].data
    definition = term.getElementsByTagName('defstr')[0].childNodes[0].data
    selected = definition.find("autophagosome")
    # Only continue when "autophagosome" can be found in the definition, which means the variable "selected" is larger than 0.
    if selected > 0:
        id_list.append(id)
        name_list.append(name)
        definition_list.append(definition)
        childnode = 0
        nodes = []
        if id in dic:
            childnode = calculate(dic[id])  # Use the function to calculate.
        childnodes_list.append(childnode)  # Assign the data to lists.

data = {'id': id_list,
        'name': name_list,
        'definition': definition_list,
        'childnodes': childnodes_list}  # Store the lists of data in a dictionary.
df = DataFrame(data)  # Transform the dictionary into a dataframe.
df.to_excel("autophagosome.xlsx", sheet_name = "Sheet1")
