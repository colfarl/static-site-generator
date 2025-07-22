from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    lst = []
    for block in blocks:
        block = block.strip()
        if block == '' or block == '\n':
            continue
        lst.append(block)
    return lst

def block_to_block_type(block):
    lines = block.split('\n')
    
    ## Determine Heading
    if len(lines) == 1:
        words = lines[0].split()
        if len(words) >= 2 and len(words[0]) <= 6 and len(words[0]) >= 1:
            flag = True
            for c in words[0]:
                if c != '#':
                    flag = False
            if flag:
                return BlockType.HEADING

    ## Determine Code
    if len(block) >= 6 and block[:3] == '```' and block[-3:] == '```':
        return BlockType.CODE
    
    ## Determine Quote
    flag = True
    for line in lines:
        if not line.startswith('>'):
            flag = False
    if flag:
        return BlockType.QUOTE

    ## Determine Unordered_List 
    flag = True
    for line in lines:
        if not line.startswith('- '):
            flag = False
    if flag:
        return BlockType.UNORDERED_LIST

    ## Determine ordered_List 
    flag = True
    curr_num = 1
    for line in lines:
        if not line.startswith(f'{curr_num}. '):
            flag = False
        curr_num += 1
    if flag:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

