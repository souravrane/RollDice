import random as rn
import sys
while True:
	n=int(input(" \n Enter the number of players...(Min. number = 2) "))
	if(n>1):
		time=int(input("Number of rounds ? "))					#round limit
		l=list(range(n))										#player numbers
		score=[0]*n 											#respective player's score
		print("\n\n")
		start = rn.randrange(n)									#toss for the opening player
		print("player ",start+1,"begins the game ! \n")
		t=time
		while time:
			print("ROUND :- ",t-time+1)

			for i in range(n):
				print("	Turn: Player ",start+1)
				print("	Roll the dice ..... (hit enter)")
				inp = input()
				dice = rn.randrange(1,6)						#rolling the dice
				score[start]+=dice								#respective player gains the score
				for i in range(n):
					print("		player ",i+1,"-> ",score[i])	#displays the respective player's score
				print()
				start=(start+1)%n 								#chooses the next player in the line 

			time-=1

		highscore = score.index(max(score))						#index of the highest scorer
		print()
		print("THE WINNER IS : PLAYER ",highscore+1)
	else:
		print("More players needed... \n")
		continue

	choice = input("	Re - Match ... ? press 'Y' or 'N' :- ")
	if choice == 'y' or choice == 'Y':
		print("	Restart...\n")
		continue
	else:
		sys.exit()


