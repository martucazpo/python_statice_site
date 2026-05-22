


def markdown_to_blocks(markdown):
    stripped = []
    split = markdown.split("\n\n")
    for block in split:
        if block == "":
            continue
        block = block.strip()
        stripped.append(block)
    return stripped 

