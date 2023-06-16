# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    # TU C�DIGO AQU�
    particion = text.partition(target_word)
    mtext = particion[0] + replace_word + particion[2]

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')