from xml.dom.minidom import parse
import xml.dom.minidom as xmlp
import networkx as nx
import matplotlib.pyplot as plt

# g = nx.Graph()
# g.add_node(1)
# g.add_edge(1,2)
# g = nx.read_gml("marvel.gml")
#
# # g = nx.karate_club_graph()
# nx.draw_spring(g)
# plt.show()


def parse_xml_to_gml():
    DOMTree = xmlp.parse("marvel.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print "Root element : %s" % collection.getAttribute("shelf")

    # msg is used to store the whole write content of gml
    msg = "graph [\n"

    # obtain all the nodes in xml files
    nodes = collection.getElementsByTagName("node")
    for i in nodes:
        # data is used to reach either type or name
        type = i.getElementsByTagName('data')[0]
        # print type.childNodes[0].data
        name = i.getElementsByTagName('data')[1]
        # print name.childNodes[0].data
        # here stupid code to avoid node label duplication
        if type.childNodes[0].data == "hero":
            msg = msg + "node [\n" + "id \"" + i.getAttribute("id") + "\"\n" + "type \"" + type.childNodes[0].data + "\"\n" + "label \"" + name.childNodes[0].data +"\"\n]\n"
        else:
            msg = msg + "node [\n" + "id \"" + i.getAttribute("id") + "\"\n" + "type \"" + type.childNodes[
                0].data + "\"\n" + "label \"" + name.childNodes[0].data + " \"\n]\n"

    # obtain all the edges in xml files
    edges = collection.getElementsByTagName("edge")
    for j in edges:
        s = j.getAttribute("source")
        t = j.getAttribute("target")
        msg += "edge [\n" + "source \"" + s + "\"\n" + "target \"" + t + "\"\n]\n"
    #print msg

    msg += "]"

    file = open("marvel.gml", 'w')
    file.write(msg)
    file.close()


def _process_params(G, center, dim):
    # Some boilerplate code.
    import numpy as np

    if not isinstance(G, nx.Graph):
        empty_graph = nx.Graph()
        empty_graph.add_nodes_from(G)
        G = empty_graph

    if center is None:
        center = np.zeros(dim)
    else:
        center = np.asarray(center)

    if len(center) != dim:
        msg = "length of center coordinates must match dimension of layout"
        raise ValueError(msg)

    return G, center


def main():
    # build marvel.gml file
    # parse_xml_to_gml()
    g = nx.read_gml("marvel.gml")

    # circular layout implemented by the circular_layout
    pos_1 = nx.circular_layout(g)
    nx.draw(g, pos_1, with_labels=True, node_size=30, font_size=8, width=0.5)
    plt.show()

    # spring layout
    pos_2 = nx.spring_layout(g,k=1)
    nx.draw(g, pos_2, with_labels=True, node_size=30, font_size=8, width=0.5)
    plt.show()

    # kamada kawai layout
    pos_3 = nx.kamada_kawai_layout(g)
    nx.draw(g, pos_3, with_labels=True, node_size=30, font_size=8, width=0.5)
    plt.figure(figsize=(12, 12))
    plt.show()

    # bipartite layout
    top = nx.bipartite.sets(g)[0]
    pos_4 = nx.bipartite_layout(g,top)
    nx.draw(g, pos_4, with_labels=True, node_size=30, font_size=8, width=0.5)
    plt.show()



main()