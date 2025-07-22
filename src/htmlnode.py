class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        res = ' '
        if self.props == None:
            return '';
        for key in self.props.keys():
            res += f'{key}="{self.props[key]}" '
        res = res[:-1]
        return res

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value

        open_tag = f'<{self.tag}{self.props_to_html()}>'
        close_tag = f'</{self.tag}>'

        return f'{open_tag}{self.value}{close_tag}'

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('tag is not an optional feature for class ParentNode')
        if self.children is None or len(self.children) == 0:
            raise ValueError('ParentNode must have children')
        
        child_html = ''
        for child in self.children:
            child_html += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>'

