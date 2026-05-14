import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_with_props(self):
        node = LeafNode("p", "Hello, world!", {"style":"color:red;font-size:3em"})
        self.assertEqual(node.to_html(), "<p style=\"color:red;font-size:3em\">Hello, world!</p>")

    def test_with_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_repr(self):
        node = LeafNode("p","Hello, world!", {"style":"color:red;"})
        self.assertEqual(node.__repr__(), "tag: p, value: Hello, world!, props: style=\"color:red;\"")

if __name__ == "__main__":
    unittest.main()
