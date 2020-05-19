
import pygame
from pygame.locals import *
import sys#sysはシステムパラメータ関数のライブラリ


def main():
    clock = pygame.time.Clock()	#単位時間あたりに処理させるフレームすなわち「コマ」の数を示す、頻度の数値である。			
    pygame.init()                  	# Pygameの初期化
    screen = pygame.display.set_mode((800, 600)) # 800*600の画面
    px = 100 #初期座標
    vx = 5	 #x方向の速度
    py = 100 #初期座標
    vy = 5	 #y方向の速度
    ay = 0	#重力加速度
    
    while (1): #繰り返し無限ループ
        screen.fill((255,255,255))  		# 画面を白に
        pygame.draw.circle(screen,(10,10,10), (px,py), 50,)  #ボールのカスタマイズ,101010は色,50はボールの大きさxy
        px += vx# 次の位置を計算
        vy += ay#y方向に重力をかける 重力は縦に働く       
        py += vy#y座標にy速度をかける
        
        if px >= 750 or px <= 50:# 左右の壁	
            vx *= -1#??
        if py >= 550 or py <= 50:	# 上下の壁
            vy *= -1#??
        print(py,vy,ay)		 #座標の表示
        pygame.display.update()     				# 画面更新
        clock.tick(60)		 #60fpsごとに画面を更新

        # イベント処理
        for event in pygame.event.get(): #イベントからキーボードやマウスの動きを取得
            if event.type == QUIT: # 閉じるボタンが押されたら終了
                pygame.quit()      # Pygameの終了(ないと終われない)
                sys.exit()    # 終了（ないとエラーで終了することになる）

if __name__ == "__main__":
    main()