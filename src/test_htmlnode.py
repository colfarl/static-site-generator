import htmlnode as hn
import unittest

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        node = hn.HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        val = node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', val)

    def test_repr_empty(self):
        node = hn.HTMLNode()
        self.assertEqual('HTMLNode(None, None, None, None)', str(node))

    def test_props_to_html_empty(self):
        node = hn.HTMLNode()
        self.assertEqual('', node.props_to_html()) 
