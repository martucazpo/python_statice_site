import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This cat smells funny!", TextType.ITALIC, "http://localhost:3000/yoursmellycat")
        node2 = TextNode("This cat smells funny!", TextType.ITALIC)
        self.assertNotEqual(node, node2) 

    def test_different_text_type(self):
        node = TextNode("This cat smells funny!", TextType.CODE )
        node2 = TextNode("This cat smells funny!", TextType.TEXT)
        self.assertNotEqual(node, node2) 

    def test_different_text(self):
        node = TextNode("Did they shave that cat?", TextType.TEXT)
        node = TextNode("No, it is wearing a wig..., always looking for attention", TextType.TEXT)


if __name__ == "__main__":
    unittest.main()
