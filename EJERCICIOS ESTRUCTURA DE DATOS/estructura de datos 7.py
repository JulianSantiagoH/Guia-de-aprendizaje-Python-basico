diccionario={
    'Contenidos Digitales':[
        'produccion multimedial','Desarrollo VideoJuegos','Animacion 3D'
    ],

    'Desarrollo de Software':[
        'Analisis y Desarrollo de Software', 'Analisis y Desarrollo de Sistemas de informacion','Porgramacion de Software'
    ],

    'Infraestructura':[
        'Sistemas','Gestion de redes de datos','Implementacion de infraestructura de TIC'
    ]
}

for categoria,elementos in diccionario.items():
    print(f'{categoria}:')
    print('')

    if elementos:
        for elemento in elementos:
            print(f'-{elemento}')
            print('')
   
