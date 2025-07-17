import textnode as tn

def main():
    content = "this is some anchor text"
    text_type = tn.TextType.LINK
    url = 'https://www.boot.dev'

    node = tn.TextNode(content, text_type, url)
    print(node)


if __name__ == '__main__':
    main()
