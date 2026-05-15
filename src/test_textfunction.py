import unittest
from textnode import TextType, TextNode, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_anchor(self):
        node = TextNode("this is a link", TextType.LINK, "#") 
        html_node = text_node_to_html_node(node) 
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {'href': '#'}) 

    def test_image(self):
        node = TextNode("this is probably a cat", TextType.IMAGE, "http://localhost:8181/catssmell")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"alt": "this is probably a cat", "src": "http://localhost:8181/catssmell"})

if __name__=="__main__":
    unittest.main()
