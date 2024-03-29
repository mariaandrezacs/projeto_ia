problema = { 
            'estadoInicial' : 'T',
            'estadoObjetivo' : 'RL',
            'Acao': {
                1 : ['T', 'C', 3],
                2 : ['C', 'T', 3],
                3 : ['T', 'F', 8],
                4 : ['F', 'T', 8],
                5 : ['F', 'C', 4],
                6 : ['C', 'F', 4],
                7 : ['C', 'P', 2],
                8 : ['P', 'C', 2],
                9 : ['P', 'F', 6],
                10 : ['F', 'P', 6],
                11 : ['P', 'CA', 5],
                12 : ['CA', 'P', 5],
                13 : ['F', 'G', 4],
                14 : ['G', 'F', 4],
                15 : ['G', 'CA', 6],
                16 : ['CA', 'G', 6],
                17 : ['CA', 'BB', 14],
                18 : ['BB', 'CA', 14], 
                19 : ['G', 'TM', 8],
                20 : ['TM', 'G', 8],
                21 : ['TM', 'BB', 4],
                22 : ['BB', 'TM', 4],
                23 : ['TM', 'E', 6],
                24 : ['E', 'TM', 6],
                25 : ['E', 'RL', 12],
                26 : ['RL', 'E', 12]
                } 
            }


 

def criarNo(Estado, NoPai = None, Acao = None, Custo = 0, Profundidade = 0):
  no = []
  no['Estado'] = Estado
  no['NoPai'] = NoPai
  no['Acao'] = Acao
  no['Custo'] = Custo
  no['Profundidade'] = Profundidade
  return no

borda = []
  
def buscarEmArvore(problema, borda):
    borda.append(criarNo(problema['estadoInicial']))
    
    while(True):
        if len(borda) == 0:
            print("Falha")
            
        no = borda.pop()
        
        if problema['EstadoInicial'] == no['estado']:
            print('sucesso')
            print(no)
            return
        
        borda = [*borda, *expandir(no, problema)]
