from htmlnode import HTMLNode, LeafNode, ParentNode 
import unittest

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        val = node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', val)

    def test_repr_empty(self):
        node = HTMLNode()
        self.assertEqual('HTMLNode(None, None, None, None)', str(node))

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual('', node.props_to_html()) 

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), 'Click me!')

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

    def test_parent_no_child(self):
        node = ParentNode('span', None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_empty_child(self):
        node = ParentNode('span', [])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode('p', 'great_grandchild')
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><p>great_grandchild</p></b></span></div>",
        )

    def test_to_html_with_two_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode('b', 'child2')
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>child2</b></div>")

