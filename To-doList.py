import json

print('============= Lista de tarefas ===============')

lista = []

perguntaSairEntrar = input('Você quer entrar ou sair? (S/N) ').lower().upper()

while perguntaSairEntrar == 'S':
    print('O que você deseja fazer?')
    print()
    perguntaFazer = input('[A]dicionar ======= [L]istar ========== [R]emover ').lower().upper()

