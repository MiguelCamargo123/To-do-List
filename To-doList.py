import json

print('============= Lista de tarefas ===============')

lista = []

perguntaSairEntrar = input('Você quer entrar ou sair? (S/N) ').upper()

while perguntaSairEntrar == 'S':
    print()
    pergunta = print('O que você deseja fazer?')
    print()
    perguntaFazer = input('[A]dicionar ======= [L]istar ========== [R]emover ').upper()
    print()

    if perguntaFazer == 'A':
        adicionar = input('Digite o que deseja adicionar: ')
        lista.append(adicionar)
        print(f'A tarefa {adicionar} foi adicionada com sucesso')

        with open('tarefas.json', 'w', encoding='utf-8') as tarefas:
            json.dump(lista, tarefas, ensure_ascii=False, indent=4)


    if perguntaFazer == 'L':
        with open('tarefas.json', 'r', encoding='utf-8') as tarefas:
            lista = json.load(tarefas)

        print('Até o momento você adicionou as seguintes tarefas:')
        for i in lista:
            print(i)

    if perguntaFazer == 'R':
        try:
            with open('tarefas.json', 'r', encoding='utf-8') as tarefas:
                lista = json.load(tarefas)
        except FileNotFoundError:
            lista = []

        print('Tarefas atuais:')
        for i, tarefa in enumerate(lista):
            print(f'{i} - {tarefa}')

        indice = int(input('Digite o número da tarefa para remover: '))

        if 0 <= indice < len(lista):
            removida = lista.pop(indice)
            print(f'Tarefa "{removida}" removida com sucesso.')

            with open('tarefas.json', 'w', encoding='utf-8') as tarefas:
                json.dump(lista, tarefas, ensure_ascii=False, indent=4)
        else:
            print('Índice inválido.')


    if perguntaFazer == 'N':
        break
    

