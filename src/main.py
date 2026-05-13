from textnode import TextNode, TextType

def main():
    

    tnode = TextNode("That cat smells funny", TextType.BOLD, "http:localhost:3000/catsarefun.com")

    print(tnode)

if __name__=="__main__":
    main()
