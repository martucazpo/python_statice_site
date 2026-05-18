
from textnode import TextType, TextNode



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not text_type.TEXT:
            new_nodes.append(node)
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Invalid Markdown: {delimiter} must be part of an openning or closing pair")
        split_node_text = node.text.split(delimiter)
        only_text = list(filter(None, split_node_text))
        for index in range(len(only_text)):
            if index % 2 == 0:
                new_text_node = TextNode(only_text[index], TextType.TEXT)
                new_nodes.append(new_text_node)
            else:
                new_fancy_node = TextNode(only_text[index], text_type)
                new_nodes.append(new_fancy_node)
        print("new nodes ", new_nodes)
        return new_nodes




