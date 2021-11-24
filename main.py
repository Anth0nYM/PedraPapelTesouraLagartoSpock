import random

escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]
emojis = ["⛰️", "📃", "✂️", "🦎", "🖖"]

vencer = {
    "pedra": [2, 0, 1, 1, 0],
    "papel": [1, 2, 0, 0, 1],
    "tesoura": [0, 1, 2, 1, 0],
    "lagarto": [0, 1, 0, 2, 1],
    "spock": [1, 0, 1, 0, 2],
}

codigo = {
    "pedra": 0,
    "papel": 1,
    "tesoura": 2,
    "lagarto": 3,
    "spock": 4
}

repetir = "s"
pontuacao = 0

print("\n"*100)
print('''
Pedra⛰️ , Papel📃, Tesoura✂️ , Spock🖖 e Lagarto🦎
----------------------------------------------------
⛰️  esmaga 🦎, 🦎 envenena 🖖
🖖 destroi ✂️ , ✂️  corta 📃
📃 refuta 🖖, 🖖 vaporiza ⛰️
⛰️  esmaga ✂️ , ✂️  mata 🦎
🦎 come 📃 e 📃 cobre ⛰️

Escolha entre uma dessas
opções e batalhe contra 
o computador!

Vitória: +3 pontos
Derrota: -1 ponto
Empate: +1 ponto

Mas, antes de começar.
''')

nome = str(input("Qual seu nome (Somente o primeiro nome)? Com ele suas vitórias serão salvas\n"))
nome = nome.replace(" ", "")

tabela = open("pontuacao.txt", "r").read()
tabela = tabela.splitlines()
for u in tabela:
    nomeSalvo, pontuacaoSalva = u.split("|")

    if (nomeSalvo == nome):
        pontuacao = int(pontuacaoSalva)

while repetir == "s":
    jogador = str(input('pedra, papel, tesoura, lagarto ou spock?\n'))
    escolhido = random.choice(escolhas)

    escolhaJogador = codigo[jogador]
    escolhaComputador = vencer[escolhido]

    for i in range(0, len(escolhas), 1):
        if (i == escolhaJogador):
            resultado = escolhaComputador[i]

    if(resultado == 0):
        resultado = "{} ganha de {}. Você venceu!".format(jogador, escolhido)
        pontuacao += 3

    elif(resultado == 1):
        resultado = "{} ganha de {}. Você perdeu!".format(escolhido, jogador)
        if( pontuacao > 0):
            pontuacao -= 1

    elif (resultado == 2):
        resultado = "Empate"
        pontuacao += 1

    print("\n"*100)
    print('''
O computador escolheu: {}

{}  VS {}

{}
Você agora possuí {} pontos.
    '''.format(escolhido, emojis[escolhaJogador], emojis[codigo[escolhido]],resultado, pontuacao))

    repetir = str(input("Deseja jogar novamente? (s/n)\n"))

    if(repetir == "s"):
        print("\n"*100)
    else:
        tabela = open("pontuacao.txt", "r").read()
        tabela = tabela.splitlines()

        novaTabela = open("pontuacao.txt", "w")

        if len(tabela) > 0:
            tabelaModificada = str()
            jaSalvo = False

            for u in tabela:
                nomeSalvo, pontuacaoSalva = u.split("|")

                if (nomeSalvo == nome):
                    jaSalvo = True
                    tabelaModificada += "{}|{}\n".format(nome, pontuacao)
                else:
                    tabelaModificada += "{}|{}\n".format(
                        nomeSalvo, pontuacaoSalva)

            if not jaSalvo:
                tabelaModificada += "{}|{}\n".format(nome, pontuacao)

            novaTabela.write(tabelaModificada)
            novaTabela.close()
        else:
            novaTabela.write("{}|{}".format(nome, pontuacao))
            novaTabela.close()