import unittest
from markdown_block_parser import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
)

class TestMarkDownBlockParsing(unittest.TestCase):

    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
                )

    def test_markdown_to_blocks_extra_spaces(self):
                md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
                """
                blocks = markdown_to_blocks(md)
                self.assertEqual(
                    blocks,
                    [
                        "This is **bolded** paragraph",
                        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                        "- This is a list\n- with items",
                    ],
                )
    
    def test_heading(self):
        block = '# heading'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)
    
    def test_heading_1(self):
        block = '## heading'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)
    
    def test_heading_2(self):
        block = '### heading'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)
    
    def test_heading_3(self):
        block = '#### heading'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)
    
    def test_heading_4(self):
        block = '##### heading'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)
    
    def test_heading_5(self):
        block = '###### heading'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)

    def test_heading_6(self):
        block = '####### heading'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_code(self):
        block = '``` some code ```'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.CODE)

    def test_code_1(self):
        block = '``` not code'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_code_2(self):
        block = '``````'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.CODE)

    def test_quote(self):
        block = '> quote 1\n> quote2'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.QUOTE)
    
    def test_quote_1(self):
        block = '> quote 1\n quote2'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)
    
    def test_quote_2(self):
        block = '> quote 1\n > quote2'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_unordered_0(self):
        block = '- entry one\n- entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.UNORDERED_LIST)

    def test_unordered_1(self):
        block = '- entry one\n-entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_unordered_2(self):
        block = '- entry one\n - entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_ordered_0(self):
        block = '1. entry one\n2. entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.ORDERED_LIST)

    def test_ordered_1(self):
        block = '1. entry one\n2.entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_ordered_2(self):
        block = '2. entry one\n1. entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_ordered_3(self):
        block = '1. entry one\n3. entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_ordered_4(self):
        block = '1 entry one\n2. entry two'
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


































    
    
    


    


    
    
    


    


    
    
    


    


    
    
    


    


