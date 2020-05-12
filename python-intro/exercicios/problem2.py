print('######## Informations about you ##############')

name = input('Text your name here: ')
age = input('Text your age here: ')

print (f'Welcome. \n Your name is: {name} \n And your age is: {age}. \n Is your information correct?  ')
answer= input(str('If yes text y if not text n: '))
if answer == 'y':
    print('OK :) Your informations has been saved')
elif answer == 'n':
    print('Input your information all over again')
