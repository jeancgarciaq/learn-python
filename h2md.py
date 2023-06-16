# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
    # TU C�DIGO AQU�
    if(html.startswith('<h1>') and html.endswith('</h1>')):
        limpiando = html.lstrip('<h1>').rstrip('</h1>')
        markdown = "# " + limpiando
    elif(html.startswith('<h2>') and html.endswith('</h2>')):
        limpiando = html.lstrip('<h2>').rstrip('</h2>')
        markdown = "## " + limpiando
    elif(html.startswith('<h3>') and html.endswith('</h3>')):
        limpiando = html.lstrip('<h3>').rstrip('</h3>')
        markdown = "### " + limpiando

    return markdown

if __name__ == '__main__':
    run('<h1>Core</h1>')