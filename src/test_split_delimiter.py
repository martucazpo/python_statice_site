import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode


class TextSplitDelimiter(unittest.TestCase):

    def initial_test(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"`",TextType.CODE)
        self.assertEqual(
                new_nodes,
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word", TextType.TEXT),
                ]
        ) 
    def test_more_than_one_block(self):
        node = TextNode("This **text** is **brave** and **super bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(
                new_nodes,
                [
                    TextNode("This ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" is ", TextType.TEXT),
                    TextNode("brave", TextType.BOLD),
                    TextType(" and ", TextType.TEXT),
                    TextType("super bold"), TextType.BOLD,
                ]
        )




if __name__=="__main__":
    unittest.main()



