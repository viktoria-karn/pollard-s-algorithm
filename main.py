import random
import math
import csv

#f(a)=a^2+1
def func(a):
    return a**2 + 1

def my_gcd(a, b):
  count_gcd_cycle=0
  while a!=0 and b!=0:
    if a >= b:
      a = a % b
    else:
      b = b % a
    count_gcd_cycle+=1
  return [a+b,count_gcd_cycle]


def Pollard(N):
    count_first_cycle=0
    count_second_cycle=0
    #создаем список для хранения двух значений-вычисленного делителя и кол-ва итераций
    gcd_func=[]
    d = N
    while d==N:
        a = random.randint(0, N - 1)
        x = func(a) % N
        y = func(func(a)) % N
        gcd_func = my_gcd(abs(y-x),N)
        d=gcd_func[0]
        count_first_cycle+=gcd_func[1]
        while d==1:
            x = func(x) % N
            y = func(func(y))% N
            gcd_func = my_gcd(abs(y-x),N)
            d=gcd_func[0]
            count_second_cycle+=gcd_func[1]
    #если получили d во внешнем цикле
    if(count_second_cycle==0):
      iteration=count_first_cycle
    else:
      iteration=count_first_cycle*count_second_cycle
    return [d,iteration]


i=1
state=1
with open("some_primes.txt", "r") as file:
  with open("numbers.txt","w") as w_file:
    for line in file:
      if line[0]=='#' or i<=state:
        i+=1
        continue        
      w_file.write(line)
      state+=random.randint(0, 10)

composite_numbers=[]
count_i=1
with open("numbers.txt", "r") as file:
  for line in file:
    file.seek(0)
    i=0
    while i<count_i:
      line=file.readline()
      i+=1
    if(line==''):
      break
    main_prime=int(line)
    for line in file:
      composite_numbers.append(main_prime*int(line))     
    file.seek(0)
    count_i+=1

with open("result.csv",mode="w",newline="") as w_file:
    file_writer = csv.writer(w_file, delimiter=";")
    file_writer.writerow(["number to factorise", "first factor","second factor"])
    for number in composite_numbers:
      d=Pollard(number)[0]
      d1=number//d
      print([number,d,d1])
      file_writer.writerow([number,d,d1])
      if d*d1==number:
        print("All right")
      else:
        print("Everything is bad")
