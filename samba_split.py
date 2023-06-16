# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    # TU C�DIGO AQU�
    direccion = smb_path.lstrip('//')
    separado = direccion.split('/', maxsplit=1)
    host = separado[0]
    path = '/' + separado[1]

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')