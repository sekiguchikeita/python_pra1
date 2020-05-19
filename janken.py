#じゃんけんゲーム #モジュールの取り込み
import random
import math #手をリストで表現
hand = ["グー", "チョキ", "パー", "ゲーム終了"]

print("===ジャンケンゲーム===")
score = 0
count = 0

# 無限ループ
while True:
   try:
      if count > 0:
          win = math.floor(score / count * 100)
          print(count, "戦目")
          print("スコア：", score, "/", count)
          print("勝率：", win) 

      com = random.randint(0, 2) #コンピュータの手

      for i in enumerate(hand):
          print(i)#hand 0 1 2 3が表示
      you = int(input("出す手を数値で入力:"))
      if you  == 3: break #ここで終了
   except:
       print("0から3の間で入力してね")
       continue
   #手を表示
   print("---")
   print("自分：", hand[you])
   print("相手：", hand[com]) #randomのところ
   input("---")

   #じゃんけんの勝敗を判定
   j = (you - com + 3) % 3  #仕組みの理解が必要
   if j == 0:
       print("あいこ")
   elif j == 1:
       print("残念！負け！")
       count += 1
   else:
       print("おめでとう！勝ち！")
       count += 1
       score += 1
   input("---")

   
