from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    lst = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 != 1:
                raise Exception(f'not valid markdown {delimiter} not closed')
            for i in range(len(split_text)):
                if i % 2 == 1:
                    lst.append(TextNode(split_text[i], text_type))
                elif len(split_text[i]) > 0:
                    lst.append(TextNode(split_text[i], TextType.TEXT))
        else:
            lst.append(node)
    return lst


def extract_markdown_images(text):
    # images if this breaks below should work 
    # r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    # regular links if this breaks this string should work
    # r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    lst = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_images(node.text)
            if matches == None or len(matches) == 0:
                lst.append(node)
                continue
            text = node.text
            for match in matches:
                split_text = text.split(f'![{match[0]}]({match[1]})', 1)
                if len(split_text) != 2:
                    raise Exception('invalid split')
                if split_text[0] != '':
                    lst.append(TextNode(split_text[0], TextType.TEXT, None))
                lst.append(TextNode(match[0], TextType.IMAGE, match[1])) 
                text = split_text[1]
            if text != '':
                lst.append(TextNode(text, TextType.TEXT, None))
        else:
            lst.append(node)
    return lst


def split_nodes_link(old_nodes):
    lst = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_links(node.text)
            if matches == None or len(matches) == 0:
                lst.append(node)
                continue
            text = node.text
            for match in matches:
                split_text = text.split(f'[{match[0]}]({match[1]})', 1)
                if len(split_text) != 2:
                    raise Exception('invalid split')
                if split_text[0] != '':
                    lst.append(TextNode(split_text[0], TextType.TEXT, None))
                lst.append(TextNode(match[0], TextType.LINK, match[1])) 
                text = split_text[1]
            if text != '':
                lst.append(TextNode(text, TextType.TEXT, None))
        else:
            lst.append(node)
    return lst

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT, None)
    new_nodes = split_nodes_delimiter([initial_node], '**', TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes 
