import random
import csv

gridSize = 3 #enter your desired grid size
cards = 4 #enter your desired number of bingo cards
minNum = 1
maxNum = 47
squares = (gridSize * gridSize) + 1

ladies = {"1":"Martha Washington", "2":"Abigail Adams", "3":"Martha Jefferson", "4":"Dolley Madison", "5":"Elizabeth Monroe", "6":"Louisa Adams", "7":"Rachel Jackson", "8":"Hannah Van Buren", "9":"Anna Harrison", "10":"Letitia Tyler", "11":"Julia Tyler", "12":"Sarah Polk", "13":"Margaret Taylor", "14":"Abigail Fillmore", "15":"Jane Pierce", "16":"Harriet Lane", "17":"Mary Todd Lincoln", "18":"Eliza Johnson", "19":"Julia Grant", "20":"Lucy Hayes", "21":"Lucretia Garfield", "22":"Ellen Arthur", "23":"Frances Cleveland", "24":"Caroline Harrison", "25":"Ida McKinley", "26":"Alice Roosevelt", "27":"Edith Roosevelt", "28":"Helen Taft", "29":"Ellen Wilson", "30":"Edith Wilson", "31":"Florence Harding", "32":"Grace Coolidge", "33":"Lou Hoover", "34":"Eleanor Roosevelt", "35":"Bess Truman", "36":"Mamie Eisenhower", "37":"Jacqueline Kennedy", "38":"Lady Bird Johnson", "39":"Pat Nixon", "40":"Betty Ford", "41":"Rosalynn Carter", "42":"Nancy Reagan", "43":"Barbara Bush", "44":"Hillary Clinton", "45":"Laura Bush", "46":"Michelle Obama", "47":"Melania Trump"}


with open('bingo.csv','a') as csvfile:
	fieldnames = []
	for i in range(1,squares):
		fieldnames.append('lady'+str(i))
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
	writer.writeheader()
	for n in range(cards):
		card = []
		card_names = []
		randRange = range(minNum, maxNum)
		card = random.sample(randRange, squares)
		for i in range(gridSize):
			for j in range(gridSize):
				card_names.append(ladies[str(card[i + j * gridSize])])
		d = {key:value for key, value in zip(fieldnames, card_names)}
		writer.writerow(d)
		d.clear()