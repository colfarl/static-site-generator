from htmlnode import(
        HTMLNode,
        ParentNode,
        LeafNode,
)
from markdown_block_parser import markdown_to_blocks
from textnode import (
        TextNode,
        TextType,
)

import shutil
import os
import os.path

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
    
def main():
    src = 'static/'
    dest = 'public/'
    copy_driver(src, dest)

if __name__ == '__main__':
    main()
