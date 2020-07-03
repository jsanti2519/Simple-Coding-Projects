#8-Queens using Python
#@author: Jonathan Santiago
# July 3rd, 2020 (Using C++ code as reference)

def ok(q, c) :
  for i in range(c):
    if q[c] == q[i] or abs(q[c] - q[i]) == c - i : return False
  return True
  #end of ok function

def printF(q, s) :
  print("Solution #" + str(s))
  for i in q:
    for j in q:
      if q[i] == j : print(" X ", end = '')
      else : print(" O ", end = '')
    print()
  #end of printF function

def main():
  q = []
  s = 1
  for i in range(8): q.append(0)

  c = 0
  q[c] = 1

  while c >= 0:
    c += 1
    if c == 8:
      printF(q, s)
      s += 1
      c -= 1
    else: 
      q[c] = -1

    while c >= 0:
      q[c] += 1
      if q[c] == 8: c -= 1
      elif ok(q, c): 
        break
  #end of main function

#calling main function in order to process code
main()
