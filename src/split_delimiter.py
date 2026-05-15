
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not text_type.TEXT:
            new_nodes.append(node)
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Invalid Markdown: {delimiter} must be part of an openning or closing pair")
        split_node_text = node.text.split(delimiter) 
        if len(split_node_text) == 1:
            new_nodes.append(node)
        else:
            new_nodes.extend(handle_split_list(split_node_text,delimiter))
    return new_nodes


                                
def handle_split_list(split_list, delimiter, nodes=[]):
    if len(split_list) == 0:
        return nodes
    list_of_subs = []
    new_node_type = TextNode(None,None,None)
    if len(split_list) == 1:
        if split_list[0].TextType != TextType.TEXT:
            list_of_subs.append([""])
        else:
            nodes.extend(split_list)
            return nodes
    list_of_subs.extend(split_list) 
    match delimiter:
        case "**":
            new_node_type = TextNode("b", list_of_subs[1], TextType.BOLD)
        case "_":
            new_node_type = TextNode("i", list_of_subs[1], TextType.ITALIC)
        case "`":
            new_node_type = TextNode("code", list_of_subs[1], TextType.CODE)
        case _:
            raise Exception("invalid delimiter: must be '**','_' or '`'") 
    nodes.extend([TextNode(list_of_subs[0], TextType.TEXT), new_node_type]) 
    list_of_subs.pop(0).pop(0) 
    return handle_split_list(list_of_subs, delimiter, nodes)


