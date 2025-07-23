from htmlnode import(
        HTMLNode,
        ParentNode,
        LeafNode,
)

from markdown_block_parser import (
    BlockType,
    block_to_block_type, 
    markdown_to_blocks,
)

from markdown_to_html import exctract_title, markdown_to_html_node
from textnode import (
        TextNode,
        TextType,
)

import shutil
import os
import os.path
import sys

def copy_directory(src, dest):
    for item in os.listdir(src):
        print('looking at item', item)
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            print('copying file:', item_path, 'from', src, 'to', dest)
            shutil.copy(item_path, dest)
        else:
            new_src = os.path.join(src, item)
            new_dest = os.path.join(dest, item)
            print('copying nested directory', new_src, 'to', new_dest)
            if not os.path.exists(new_dest):
                os.mkdir(new_dest)
            copy_directory(new_src, new_dest)

def copy_driver(src, dest):
    if not os.path.exists(src):
        raise Exception('source directory does not exist')
    
    if not os.path.exists(dest):
        print('creating:', dest)
        os.mkdir(dest)
    else:
        print('clearing out', dest)
        shutil.rmtree(dest)
        os.mkdir(dest)
    
    copy_directory(src, dest)

def get_file_contents(file_name):
    file = open(file_name, 'r')
    contents = file.read()
    file.close()
    return contents

def generate_page(from_path, template_path, dest_path, base_path):
    print("Generating page from", from_path, "to", dest_path, "using", template_path)
    md = get_file_contents(from_path)
    template = get_file_contents(template_path)
    html_node = markdown_to_html_node(md)
    html = html_node.to_html()  
    title = exctract_title(md)
    template = template.replace('{{ Title }}', title, 1)
    template = template.replace('{{ Content }}', html, 1)
    template = template.replace('href="/', 'href="{base_path}')
    template = template.replace('src="/', 'src="{base_path}')
    
    directory_name = os.path.dirname(dest_path)
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    with open(dest_path, 'w') as f:
        f.write(template)

def generate_page_recursive(dir_path_content, template_path, dest_path, base_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            print('generating content for', item, 'from', item_path, 'to', dest_path)
            generate_page(item_path, template_path, os.path.join(dest_path, item.replace('.md', '.html')), base_path)
        else:
            new_src = os.path.join(dir_path_content, item)
            new_dest = os.path.join(dest_path, item)
            print('moving down directory:', new_src, 'to', new_dest)
            generate_page_recursive(new_src, template_path, new_dest, base_path)
def main():
    if len(sys.argv) > 2:
        print('Usage: python3 main.py [basepath]')

    base_path = '/'
    if len(sys.argv) == 2:
        base_path = sys.argv[1]

    # copy over static assets
    src = 'static/'
    dest = 'docs/'
    copy_driver(src, dest)

    # write html to new file
    from_path = 'content/'
    template_path = 'template.html'
    dest_path = 'docs/'
    generate_page_recursive(from_path, template_path, dest_path, base_path)

if __name__ == '__main__':
    main()
