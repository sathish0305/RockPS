from rps_logic import Game

g1 = Game()
print('Hello welcome to rock,paper and scissors game')
print('='*20)
round = int(input('Enter How many rounds do you want to play: '))
for i in range(round):
    print(f'Round {i+1}')
    option = int(input(f'Enter your option\n1.Rock\n2.Paper\n3.Scissors\n{"*"*20}\n'))
    value = {
        1:'Rock',
        2:'Paper',
        3:'Scissors'
    }
    print('-'*20)

    g1.play(value[option])
    print('-'*20)
g1.score()
