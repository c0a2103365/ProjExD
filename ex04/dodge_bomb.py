import openpyxl
import pygame as pg
import random
from random import randint
import sys
import time
import webbrowser


def check_bound(obj_rct, scr_rct):
    # 第1引数:こうかとんrectまたは爆弾rect
    # 第2引数:スクリーンrect
    # 範囲内:+1/範囲外:-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


# タイムスコアをExcel記録する関数
def create_xl_file(name, value):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws["A1"].value = value
    wb.save(name)


def main():
    global xl_file, time_score
    start = time.time()
    # Excelファイルのための名前
    xl_file = r"ex04/score.xlsx"
    clock = pg.time.Clock()
    # 練習1
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習3
    # ファイルをランダムに選ぶための数字の配列
    file_nums = [num for num in range(0, 10)]
    # ランダムにこうかとんを選ぶ
    tori_sfc = pg.image.load(f"fig/{random.choice(file_nums)}.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    # 練習5
    bomb_size = randint(20, 101)
    bomb_sizes = [bomb_size, bomb_size]
    bomb_sfc = pg.Surface(bomb_sizes)  # 正方形の空のSruface
    bomb_sfc.set_colorkey((0, 0, 0))
    # ゲームを初期化するごとに爆弾の色と大きさが変更
    pg.draw.circle(bomb_sfc, (randint(0, 256), randint(0, 256), randint(
        0, 256)), (bomb_sizes[0]/2, bomb_sizes[1]/2), bomb_sizes[0]/2)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    vx, vy = +1, +1
    # 練習2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        # 練習4
        key_dct = pg.key.get_pressed()  # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみでていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        # 練習6
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        # 練習8
        if tori_rct.colliderect(bomb_rct):
            # デフォルトブラウザでWebサイトを開く
            # 東京工科大学のHPを開く
            url = "https://www.teu.ac.jp/"
            webbrowser.open(url)
            return
        pg.display.update()
        clock.tick(1000)
        # 最終的な処理時間を算出
        time_score = time.time()-start


if __name__ == "__main__":
    pg.init()
    main()
    create_xl_file(xl_file, time_score)
    pg.quit()
    sys.exit()
