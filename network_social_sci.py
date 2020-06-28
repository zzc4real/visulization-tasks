import networkx as nx
import matplotlib.pyplot as plt

# global variable

msg = "graph [\n"

# implementing node_person
def parse_person_node(filename):
    global msg
    for line in open(filename,"r"):
        line = line[:-1]
        msg = msg + "node [\n" + "id \"" + line + "\"\n" + "label \"" + line + "\"\n" + "type \"person\"]\n"


def parse_company_node(filename):
    global msg
    for line in open(filename, "r"):
        data = line[:-1].split(',')
        msg = msg + "node [\n" + "id \"" + data[0] + "\"\n" + "label \"" + data[0] + "\"\n" + "type \"" + data[4][1:] + "\"]\n"


def parse_c_to_p_edge(filename):
    global msg
    for line in open(filename, "r"):
        data = line[:-1].split(' ',2)

        if data[1][0] == '-':
            data[1] = data[1][1]
            msg += "edge [\n" + "source \"" + data[0] + "\"\n" + "target \"" + data[2] + "\"\n" + "group \"" + data[
                1] + "\"\n]\n"
        # Allianz (Dresdner Bank) case
        elif data[1][0] == '(':
            data[0] += ' ' + data[1] + ' ' + data[2][:5]
            data[1] = data[2][7]
            data[2] = data[2][11:]
            msg += "edge [\n" + "source \"" + data[0] + "\"\n" + "target \"" + data[2] + "\"\n" + "group \"" + data[1] + "\"\n]\n"
        else:
            data[0] += ' ' + data[1]
            sub_data = data[2].split(' ', 1)
            sub_data[0] = sub_data[0][1]
            msg += "edge [\n" + "source \"" + data[0] + "\"\n" + "target \"" + sub_data[1] + "\"\n" + "group \"" + sub_data[
                0] + "\"\n]\n"


def parse_p_to_c_edge(filename):
    global msg
    for line in open(filename, "r"):
        data = line[:-1].split(' -> ')
        msg += "edge [\n" + "source \"" + data[0] + "\"\n" + "target \"" + data[1] + "\"\n" + "group \"" + "c" + "\"\n]\n"


parse_person_node("node_person.txt")
parse_company_node("node_company.txt")
parse_c_to_p_edge("edge_c_to_p.txt")
parse_p_to_c_edge("edge_p_to_c.txt")
msg += "]"
print msg

file = open("networkSocialSci.gml", 'w')
file.write(msg)
file.close()
