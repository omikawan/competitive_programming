#https://yukicoder.me/problems/no/47

'''
Saraは、「ふしぎなポケット」を手に入れた。

「ふしぎなポケット」は、いくつかビスケットを入れて叩くと、入れたビスケットの数が２倍になる。
Saraは最初1枚のビスケットを持っていて、「ふしぎなポケット」を使ってちょうどN枚のビスケットにして、全部食べたいと思っている。
（食べきれないので枚数をオーバーしてはいけない）

この時、ちょうどN枚にするには、Saraは最低何回ポケットを叩く必要があるか求めてください。
'''
import time
start = time.time()

#10
# 1*2 = 2*2 = 4*2 = 8

#18
# 1*2 = 2*2 = 4*2 = 8*2 = 16

#39
# 1*2 = 2*2 = 4*2 = 8*2 = 16*2 = 32

N = int(input())
count = 0
num = 1
while num < N:
	count+=1
	num*=2

print(count)



print(time.time()-start)
	