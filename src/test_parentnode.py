import unittest 

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )  

    def test_to_html_with_valued_children_and_props(self):
        grandchild_node = LeafNode("a","link",{"style":"text-decoration:none;"})
        child_node = ParentNode("li", [grandchild_node], {"id":"list", "class":"short-list"})
        parent_node = ParentNode("ul", [child_node], {"id":"listDiv", "class":"list-div"})
        self.assertEqual(
                parent_node.to_html(),
                "<ul id=\"listDiv\" class=\"list-div\"><li id=\"list\" class=\"short-list\"><a style=\"text-decoration:none;\">link</a></li></ul>",
        )

if __name__ == "__main__":
    unittest.main()
