#tic-tac-toe
import random
import userClass
REWARDS = ["Sensei", "Master", "Voodoo", "Magician", "Predictor"]
VALID_STEPS = ['Rock', 'Scissors', 'Paper']	# для отображения хода pc текстом (через index)
COLORS = {"Red": "\u001b[41m", "Green": '\u001b[42m', "Res":"\u001b[0m"}
WINS = ["-----Winner Pc-----", "----Winner User----", "--------TIE--------"]

#name = input("Enter your name: ").title()
name = input("Enter your name: ").title()
player = userClass.User(name)
player.readScore()


def showWelcome():
	""" Эта функция отображает инструкцию"""
	print('\n-------Game--------\nRock/Scissors/Paper\n(1)     (2)    (3)\n') # 

def pcChoice():
	""" Эта функция отображает выбор компьютера """
	randomNumer = random.randrange(1, 3)	# 1 = Камень, 2 = Кожницы, 3 = Бумага
	return randomNumer

def userChoice():
	""" Опрашивает пользовательский ход """
	choice = int(input('Your move: '))
	if choice > 0 and choice < 4:
		return choice
	else:	# если некоректный выбор
		print('[ EROOR ] Invalid choice')
		raise SystemExit

def showResults():
	print(player)
	player.writeScore()
	#print( 'Computer move is ' + VALID_STEPS[pcStep] ) 		# вывести ход pc на экран

	

def winnerCalculation(pcChoice, userChoice):
	""" Определение победителя """
	if pcChoice == userChoice:						# Если выбор равен
		print('\n{0:-^19}'.format('TIE'))
		showResults()		
	elif pcChoice == 1 and userChoice == 2:			# pc = Rock, user = Scissors
		print(COLORS["Red"] + WINS[0] + COLORS["Res"])
		showResults()
	elif pcChoice == 1 and userChoice == 3:			# pc = Rock, user = Paper
		print(COLORS["Green"] + WINS[1] + COLORS["Res"])
		player.win()
		startProgram()

	elif pcChoice == 2 and userChoice == 1:			# pc = Scissors, user = Rock
		print(COLORS["Green"] + WINS[1] + COLORS["Res"])
		player.win()
		startProgram()

	elif pcChoice == 2 and userChoice == 3:			# pc = Scissors, user = Paper
		print(COLORS["Red"] + WINS[0] + COLORS["Res"])
		showResults()
	elif pcChoice == 3 and userChoice == 1:			# pc = Paper, user = Rock
		print(COLORS["Red"] + WINS[0] + COLORS["Res"])
		showResults()
	elif pcChoice == 3 and userChoice == 2:			# pc = Paper, user = Scissors
		print(COLORS["Green"] + WINS[1] + COLORS["Res"])
		player.win()
		startProgram()
	

def startProgram():
	showWelcome()
	pcStep = pcChoice()	# запись хода pc в переменную
	winnerCalculation(pcStep, userChoice()); pcStep -= 1	# кто выиграл?, отнимаем 1 для дальнейшего коректного отображения (index)
	print( 'Computer move is ' + VALID_STEPS[pcStep] )

	
	
	
if __name__ == '__main__':
	startProgram()
