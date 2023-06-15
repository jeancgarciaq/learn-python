# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    # TU C�DIGO AQU�
    indice = text.find(target_word)
    ancho = len(target_word) + indice - 1
    texto1 = [start:indice]
    texto2 = [ancho:end]
    mtext = texto1 + " " + replace_word + " " + texto2

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')