import emoji

bandera = "Italia"

match bandera:
    case 'Italia':
        print('🇮🇹', language='es')
    case 'Emiratos Arabes':
        print('🇦🇪', language="es")
    case 'Afganistan':
        print('🇦🇫', language='es')
    case 'Argentina':
        print('🇦🇷', language='es')
    case 'Australia':
        print('🇦🇺', language='es')
    case 'Bélgica':
        print('🇧🇪', language='es')
    case 'Bolivia':
        print('🇧🇴', language='es')
    case _:
        print('País aún no registrado')