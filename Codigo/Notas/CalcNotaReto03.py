print('******* CALCULO NOTA DEFINITIVA ESTUDIANTE *******')
ListaNotas = [0] * 10
SumaNota10 = 0
SumaNota90 = 0
ErorText = ''
Eror = False
Notas = 0
for i in range (10):
    while True:
        try:
            Notas = float(input('Digite nota {}: '.format(i+1)))
            if Notas <= 0 or Notas > 10:
                print('******* Datos fuera de rango, solo valores de 1 a 10 *******')
                continue
            else:
                ListaNotas[i] = Notas
                if i <= 6:
                    SumaNota10 += ListaNotas[i]
                elif i > 6:
                    SumaNota90 += ListaNotas[i]
                break
        except ValueError:
            print('Ha ocurrido un error: ')
SumaNota10 = (SumaNota10 / 7) * 0.1
SumaNota90 = (SumaNota90 / 3) * 0.9
NotaDef = SumaNota10 + SumaNota90
print(ListaNotas)
print('                                                                      |          90%                |')
print('                                    10%                               |   30%   |   30%   |   30%   |')
print('| NOTA 01 | NOTA 02 | NOTA 03 | NOTA 04 | NOTA 05 | NOTA 06 | NOTA 07 | NOTA 08 | NOTA 09 | NOTA 10 |')
print('|   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |  {}   |'.format(ListaNotas[0],ListaNotas[1],ListaNotas[2],ListaNotas[3],ListaNotas[4],ListaNotas[5],ListaNotas[6],ListaNotas[7],ListaNotas[8],ListaNotas[9]))
print('|NOTA DEFINITIVA:   |   {}   |'.format(round(NotaDef,1)))
