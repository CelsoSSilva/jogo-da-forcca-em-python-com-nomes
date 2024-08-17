import random

print('Jogo da Forca')
nomes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
         'Kleber', 'Larissa', 'Marcos', 'Nathalia', 'Otavio', 'Patricia', 'Ricardo', 'Sandra', 'Thiago', 'Viviane',
         'Alice', 'Brenda', 'Cesar', 'Diogo', 'Eliana', 'Fabio', 'Giovanna', 'Hugo', 'Isabela', 'Joao',
         'Karina', 'Leandro', 'Mariana', 'Natalia', 'Orlando', 'Paulo', 'Renata', 'Sergio', 'Tatiana', 'Vinicius',
         'Silva', 'Souza', 'Costa', 'Santos', 'Oliveira', 'Pereira', 'Lima', 'Carvalho', 'Ferreira', 'Ribeiro',
         'Almeida', 'Nascimento', 'Araujo', 'Melo', 'Barros', 'Freitas', 'Pinto', 'Dias', 'Rocha', 'Correia',
         'Moreira', 'Barbosa', 'Cardoso', 'Teixeira', 'Cavalcanti', 'Gomes', 'Martins', 'Fernandes', 'Castro', 'Vieira',
         'Ramos', 'Monteiro', 'Moura', 'Campos', 'Guimaraes', 'Machado', 'Mendes', 'Nascimento', 'Nogueira', 'Reis', 'Hellen']

sorteio = random.choice(nomes).upper() #sorteia os nomes da lista
progresso = ['_'] * len(sorteio)#coloca as linhas de acordo com os nomes sorteados
tentativas = 15 #quantidade de tentativas 

while tentativas > 0:
    print(f'Você tem {tentativas} tentativas!') # se a letra estiver no sorteio vai pegar a posição dela e colocar na linha
    print('Progresso:', ' '.join(progresso))#pega a posição da letra 
    
    encontra = input('Digite uma letra: ').upper()
    
    if encontra in sorteio:
        for i, letra in enumerate(sorteio):
            if letra == encontra:
                progresso[i] = letra
        
        if '_' not in progresso:
            print(f'Parabéns, você adivinhou a palavra {sorteio}!')#encerra o programa se todas as linhas forem completas
            break
    else:
        tentativas -= 1
        print('Letra não encontrada.')

    if tentativas > 0:
        r = input('Deseja dar um palpite [S/N]? ').upper().strip()#pergunta se deseja arriscar um palpite
        if r == 'S':
            palpite = input('Digite seu palpite: ').upper().strip()
            if palpite == sorteio:
                print(f'Parabéns, você acertou com {tentativas} tentativas restantes! O nome é {sorteio}.')#se o palpite estiver certo, encerra o programa
                break
            else:
                print(f'Você errou. A palavra era {sorteio}.')# se o palpite estiver errado, encerra o programa
                break

if tentativas == 0:
    print(f'Suas tentativas acabaram. A palavra era {sorteio}.')#encerra o programa se as tentativas acabarem

