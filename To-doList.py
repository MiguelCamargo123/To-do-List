print('============= Lista de tarefas ===============')

lista = []

perguntaSairEntrar = input('Você quer entrar ou sair? (S/N) ').lower().upper()

while perguntaSairEntrar == 'S':
    print()
    print('O que você deseja fazer?')
    print()
    perguntaFazer = input('[A]dicionar ======= [L]istar ========== [R]emover ').lower().upper()
    print()

    if perguntaFazer == 'A':
        adicionar  = input('Digite o que deseja adicionar: ')
        lista.append(adicionar)
        print(f'A tarefa {adicionar} foi adicionada com sucesso')

    if perguntaFazer == 'L':
        for i in lista:
            print('Até o momento você adicionou as seguintes tarefas:')
            print(i)
            
    if perguntaFazer == 'R':
        remover = input('Digite o que deseja remover: ')
        if remover in lista:
            lista.pop(remover)

