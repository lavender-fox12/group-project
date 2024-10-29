#define the function
def fizzBuzz(n):
  #create a new array
  answer = []
  #add the separated words and numbers into the empty array, for every use case
  for i in range(1, n + 1):
    if i %3 == 0 and i % 5 == 0:
      answer.append("FizzBuzz")
    elif i % 3 == 0:
      answer.append("Fizz")
    elif i % 5 == 0:
      answer.append("Buzz")
    else:
      answer.append(str(i))
  return answer
