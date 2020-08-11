# Analisando e gerando Dicionários

def notas(*notas, sit=False):
    '''
    --> Função que retorna um dicionário com as seguintes informações:
        * Total de notas passadas;
        * Maior nota passada;
        * Menor nota passada;
        * Média das notas;
    
    --> Parâmetros:
        * notas > recebe um número ilimitado de notas;
        * sit   > recebe valores lógicos para exibir a situação da turma;
            >> ESTE PARÂMETRO É OPCIONAL;
            >> True:  exibe se a situação é boa, razoável ou ruim;
            >> False: não exibe a situação da turma;
    '''

    turma = {
        'Total': f'{len(notas)} notas',
        'Maior nota': max(notas),
        'Menor nota': min(notas),
        'Media': float(f'{(sum(notas) / len(notas)):.1f}')
    }

    if turma['Media'] < 5:
        situacao = 'Ruim'
    elif 5 <= turma['Media'] < 8:
        situacao = 'Razoável'
    else:
        situacao = 'Boa'
    
    if sit == True:
        turma['Situacao'] = situacao
    else:
        pass

    return turma


# Main Script
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
