import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","link",None,"href='#'")
        expected = "tag: a, value: link, children: None, props: href='#'"
        self.assertEqual(node.__repr__(), expected)

    def test_props_to_html(self):
        node = HTMLNode("a", "link", None, { "href": "#", "target": "_blank" })
        expected = 'href="#" target="_blank"' 
        self.assertEqual(node.props_to_html(), expected)


    def test_repr(self):
        node = HTMLNode("a", "link", None, { "href": "#", "target": "_blank" })
        expected = "tag: a, value: link, children: None, props: {'href': '#', 'target': '_blank'}"
        self.assertEqual(node.__repr__(), expected)

    def what_about_the_children(self):
        node = HTMLNode("li", None, "<a href=\"#\">link</a>", {"style": "list-style: none;"})
        expected = "tag: li, value: None, children: <a href=\"#\">link</a>, props: {'style': 'list-style: none;'}"



if __name__ == "__main__":
    unittest.main()
