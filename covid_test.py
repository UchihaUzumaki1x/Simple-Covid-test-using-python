import random

def options():
	print('1. Yes')
	print('2. No')
	ans = int(input())
	return ans

def run_covid_test():
	score = 60
	for i in range(len(ques_list)):
		print('\n')
		copy_ques_list = ques_list
		random_ques = random.choice(ques_list)
		copy_ques_list.remove(random_ques)
		if random_ques == ques1:
			print(ques1)
			ans = options()
			score += 2.5 if ans == 2 else None
		elif random_ques == ques2:
			print(ques2)
			ans = options()
			score += 2.5 if ans == 2 else None
		elif random_ques == ques3:
			print(ques3)
			ans = options()
			score += 2.5 if ans == 2 else None
		elif random_ques == ques4:
			print(ques4)
			ans = options()
			score += 2.5 if ans == 2 else None
		elif random_ques == ques5:
			print(ques5)
			ans = options()
			score += 2.5 if ans == 1 else None
		elif random_ques == ques6:
			print(ques6)
			ans = options()
			score += 2.5 if ans == 2 else None
		elif random_ques == ques7:
			print(ques7)
			ans = options()
			score += 2.5 if ans == 1 else None
		elif random_ques == ques8:
			print(ques8)
			ans = options()
			score += 2.5 if ans == 2 else None

	return score

print('CORONA')
print('How Much Safe Are You?\n')
name = input('Enter your name: ')

#### Questions
ques1 = 'Do you often touch your face?'
ques2 = 'Do you have any immune disease?'
ques3 = 'Are you travelling during lockdown period?'
ques4 = 'Are you in close contact with sick people?'
ques5 = 'Do you use a face mask?'
ques6 = 'Do you have a fever?'
ques7 = 'Do you wash your hands often?'
ques8 = 'Are you coughing?'

ques_list = [ques1,ques2,ques3,ques4,ques5,ques6,ques7,ques8]

score = run_covid_test()

print('\n')
print(name)
print('You are {}% Safe'.format(int(score)))
