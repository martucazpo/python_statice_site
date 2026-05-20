from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    return links 

# text="This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)" 

# lettuce_c = text_to_textnodes(text)

# print("lettuce ",lettuce_c)