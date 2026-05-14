



class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children 
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method has not implemented yet")

    def props_to_html(self):
        str = ""
        for key, value in self.props.items():
            str += f"{key}=\"{value}\" " 
        return str.strip()
        
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props) 

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have a value") 
        if self.tag == None:
            return f"{self.value}" 
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>" 
        return f"<{self.tag}>{self.value}</{self.tag}>" 

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props_to_html()}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props) 

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent nodes must have a tag") 
        if self.children == None:
            raise ValueError("Parents by definition must have children")
        child_str = ""
        for child in self.children:
            child_str += child.to_html()
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{child_str}</{self.tag}>" 
        return f"<{self.tag}>{child_str}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
