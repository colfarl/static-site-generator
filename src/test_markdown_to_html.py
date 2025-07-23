import unittest
from markdown_to_html import exctract_title, markdown_to_html_node

class TestMarkDownToHTML(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph text in a p tag here


This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_heading_1(self):
        md = '# heading'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>heading</h1></div>'
        )


    def test_heading_2(self):
        md = '## heading'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h2>heading</h2></div>'
        )

    def test_heading_3(self):
        md = '## heading\n'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h2>heading</h2></div>'
        )

    def test_heading_4(self):
        md = '###### heading'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h6>heading</h6></div>'
        )

    def test_heading_5(self):
        md = '####### heading'
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>####### heading</p></div>'
        )

    def test_olist(self):
        md = """1. number one
2. number
"""     
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
           '<div><ol><li>number one</li><li>number</li></ol></div>'
        )

    def test_ulist(self):
        md = """- number one
- number
"""     
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
           '<div><ul><li>number one</li><li>number</li></ul></div>'
        )

    def test_exctract_title(self):
        md = '# Hello'
        title = exctract_title(md)
        self.assertEqual(
            title,
            'Hello'
        )

    def test_exctract_title_1(self):
        md = '#    Hello    '
        title = exctract_title(md)
        self.assertEqual(
            title,
            'Hello'
        )

    def test_exctract_title_2(self):
        md = '    Hello    '
        with self.assertRaises(Exception):
            title = exctract_title(md)
