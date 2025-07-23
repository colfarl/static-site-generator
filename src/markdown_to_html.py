from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_block_parser import block_to_block_type, markdown_to_blocks, BlockType
from markdown_parser import text_to_textnodes 
from textnode import text_node_to_html_node 

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children

def make_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode('p', text_to_children(paragraph), None)

def make_code(block):
    child = LeafNode('code', block[3:-3], None)
    return ParentNode('pre', [child], None)

def make_heading(block):
    num_pounds = len(block.split()[0])
    return LeafNode(f'h{num_pounds}', block[num_pounds + 1:], None)

def make_ordered_list(block):
    children = []
    for line in block.split('\n'):
        text = text_to_children(line.split(' ', 1)[1])
        children.append(ParentNode('li', text, None))
    return ParentNode('ol', children, None)

def make_unordered_list(block):
    children = []
    for line in block.split('\n'):
        text = text_to_children(line.split(' ', 1)[1])
        children.append(ParentNode('li', text, None))
    return ParentNode('ol', children, None)

def make_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def exctract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING and block.startswith('# '):
            block = block.lstrip('# ')
            block = block.strip()
            return block
    raise Exception('No title found in markdown, markdown must contain "# <Title>"')

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children.append(make_paragraph(block))
            case BlockType.CODE:
                children.append(make_code(block))
            case BlockType.QUOTE:
                children.append(make_quote(block))
            case BlockType.HEADING:
                children.append(make_heading(block)) 
            case BlockType.ORDERED_LIST:
                children.append(make_ordered_list(block))
            case BlockType.UNORDERED_LIST:
                children.append(make_unordered_list(block))
    return ParentNode('div', children, None)

