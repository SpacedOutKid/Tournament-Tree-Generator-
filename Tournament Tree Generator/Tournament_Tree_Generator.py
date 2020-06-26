import random 

numberofEntries = eval(input('Enter the number of participants for the tournamanet: '))
entrys = 0
participants = []
participantsNum = 0
#Adds the participant to the list 
while entrys != numberofEntries:
    entryParticipants = input('Enter the name of the particpant: ')
    participants.append(entryParticipants)
    entrys += 1
    participantsNum +=1 #adds 1 number for each participant which begins the next loop
print('The participants in the tournament are ',*participants, sep = ",")
print(' ')  
#Chooses the participants playing eachother
while participantsNum != 0:
    choice1 = random.choice(participants)
    participants.remove(choice1)
    choice2 = random.choice(participants)
    participants.remove(choice2)
    participantsNum -=2 #resets the participation number back to 0 for the next loop and ends this loop
    print(f'{choice1} will face {choice2}\n')
#Loop 
loop = 'yes' 
while loop =='yes':
    entrys = 0
    winnersNum = 0
    winnersBracket =[]
    bracketContinues = input('Is there more than 1 winner? If YES enter "1", if NO enter "2": ')
    if bracketContinues == '1':
        numOfWinners = eval(input('\nHow many winners were there?: '))
        while entrys != numOfWinners:
            winners = input('\nEnter the name of the winner: ')
            winnersBracket.append(winners)
            entrys += 1
            winnersNum +=1
        while winnersNum != 0:
            choice1 = random.choice(winnersBracket)
            winnersBracket.remove(choice1)
            choice2 = random.choice(winnersBracket)
            winnersBracket.remove(choice2)
            winnersNum -=2 #resets the participation number back to 0 for the next loop and ends this loop
            print(f'{choice1} will face {choice2}\n')
            loop = 'yes'

    if bracketContinues == '2': 
        winner = input('\nEnter the winnners name: ')
        print(f'\nThe winner is: {winner}')
        break



