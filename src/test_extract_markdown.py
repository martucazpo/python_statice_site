import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_delimiter import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestExtractMarkdown(unittest.TestCase):

    def test_images_for_path(self):
        text = "This is some text with some images ![some cat eating](./images/somecateating.gif) and here is another image of the same cat ![some cat with a hairball](./images/catwithhairball.jpeg) and here are some words in parenthesis (some words in parenthesis)."
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("some cat eating", "./images/somecateating.gif"),
            ("some cat with a hairball", "./images/catwithhairball.jpeg")
        ], matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    ) 

    def test_links(self):
        links = "This is text with 2 links, the first [a link](http://localhost:3000/locallink) is a link to localhost and the second [another link!](#linkDiv) is a link to a section in the page with an id of linkDiv."
        matches = extract_markdown_links(links)
        self.assertListEqual([
            ("a link", "http://localhost:3000/locallink"),
            ("another link!", "#linkDiv")
        ], matches) 

    def test_link_extraction(self):

        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ]
        , new_nodes)