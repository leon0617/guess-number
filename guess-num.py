# 讓使用者決定隨機變數範圍 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對了的話印出 “終於猜對了!"
# 猜錯的話 要告訴他比答案大/小

import random

start = input("請輸入要猜的起始數字：")
start = int(start)
end = input("請輸入要猜的結束數字：")
end = int(end)

r = random.randint(start , end)

while True:
   num = input("請猜數字： ")
   num = int(num)
   if num == r:
       print("你終於猜對了!")
       break
   elif num > r:
       print("比答案大!")
   elif num < r:
       print("比答案小!")