from rps_logic import Game

class RoundError(Exception):
    pass

g1 = Game()
print('Hello welcome to rock,paper and scissors game')
print('='*20)
try:
    round = int(input('Enter How many rounds do you want to play(1/3/5): '))
    if round<1 or round%2 == 0 or round >5:
        raise RoundError
    else:
        count = 0
        while count < round:
            print(f'Round {count+1}')
            option = int(input(f'Enter your option\n1.Rock\n2.Paper\n3.Scissors\n{"*"*20}\n'))
            if option>=1 and option<=3:
                value = {
                    1:'Rock',
                    2:'Paper',
                    3:'Scissors'
                }
                print('-'*20)
                g1.play(value[option])
                count+=1
            else:
                print('INVALID OPTION TRY AGAIN!!!')
                print('-'*20)

    print('-'*20)
except ValueError as err:
    print('Alphabets are not allowed \nEnter positive integer number')
except RoundError as err:
    print('Round must be greater than 0, less than 6 and must be in odd numbers')
else:
    g1.score()
