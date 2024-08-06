from markdown2 import Markdown



converter = Markdown()

def md2html(text: str) -> str:
    result1 = converter.convert(text)
    return result1.strip()