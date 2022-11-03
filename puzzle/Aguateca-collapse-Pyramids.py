def compute():

    table = [
        [0.00, 0.00, 1.00, 0.00, 0.00, 1.00, 0.00, 1.00], 
        [1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
        [0.00, 0.00, 0.00, 5.00, 5.00, 0.00, 5.00, 0.00], 
        [0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    ]

    {(0,5): ['azul', 3]}

    dict_pos = {
        'outro':
            [
                (7,7)
            ],
        'azul': [
            (6,5),
            (6,3),
            # (6,1)
            (0,5),
            (7,0)
        ],
        
        'ciano': [
            (5,6),
            (7,4),
            (4,3),
            (1,0),
            (6,1), # azul ou ciano?
            (4,0),
            (2,4)
            
        ],
        
        'amarelo': [
            (2,6),
            (0,2)
        ],
        
        'vermelho': [
            (4,7),
            (0,7),
            (5,2)
            
            
        ],
        
    }
    matriz = [[0 for item in list(range(8))] for item in range(8)]
    print(matriz)
    for k, y in dict_pos.items():
        if k == 'azul':
            for item in dict_pos[k]:
                matriz[item[0]][item[1]] = 3
        elif k == 'ciano':
            for item in dict_pos[k]:
                matriz[item[0]][item[1]] = 4
        elif k == 'amarelo':
            for item in dict_pos[k]:
                matriz[item[0]][item[1]] = 5
        elif k == 'vermelho':
            for item in dict_pos[k]:
                matriz[item[0]][item[1]] = 2
        elif k == 'outro':
            for item in dict_pos[k]:
                matriz[item[0]][item[1]] = 6
        else:
            print('hmmmmm, deu merda')


    #print(table)
    return matriz

def compute():

    n1 = '0'*15 + '1'
    
    n2 = '0110110010100010'
    #n2 = '1001001101011101'
    n3 = '0010001011000100'
    #n3 = '1101110100111011'
    n4 = '0'*16

    list_values = []
    for item in zip(n1,n2,n3,n4):
        if '1' in item:
            list_values.append('1')
        else:
            list_values.append('0')

    a = ''.join(list_values)
    a = a.replace('1', '2')
    a = a.replace('0','1')
    a = a.replace('2','0')
    return