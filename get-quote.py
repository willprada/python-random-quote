import random


def start():
  resp = input('Do you want to add more quotes?(y/n) ')
  resp = resp.lower()

  if resp == 'y':
    f = open("quotes.txt", "at")

    while resp == 'y':
      quote = input('New quote? >')
      f.write(quote+"\n")
      resp = input('Do you want to add more quotes?(y/n) ')
    f.close()
  print()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd], end="")
  rnd = random.randint(0, last)
  print(quotes[rnd], end="")




if __name__== "__main__":
  start()
