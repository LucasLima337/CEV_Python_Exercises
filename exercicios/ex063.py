# Sequência de Fibonacci v1.0
import emoji
fast = emoji.emojize(':fast_forward:', use_aliases=True)
flag = emoji.emojize(':checkered_flag:', use_aliases=True)
title = 'Fibonacci Sequence'
print('=-=' * 10)
print(f'{title:^30}')
print('=-=' * 10)
print('')
stop = int(input('How many terms do you want to show? '))
cont = t2 = 1
fib = t1 = 0
print('')
while cont <= stop:
    print(f'{fib}', end=f' {fast} ')
    if cont < 3:
        fib = 1
    else:
        t1 = t2
        t2 = fib
        fib = t1 + t2 
    cont += 1
print(f'{flag}')
print('\n\n')

# Modo de resolução do exercício
'''
0 --> 1 --> 1 --> 2 --> 3 --> 5 --> 8 ...
t1    t2   fib

0 --> 1 --> 1 --> 2 --> 3 --> 5 --> 8 ...
      t1    t2   fib

t1 = t2
t2 = fib
fib = t1 + t2
'''
