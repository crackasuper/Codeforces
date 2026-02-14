
case = int(input())

for _ in range(case):
  word = input()

  first_letter = word[0]
  second_letter = word[-1]
  
  answer = len(word) - 2
  
  print(first_letter + answer + second_letter)
