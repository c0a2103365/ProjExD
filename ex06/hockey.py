import pygame as pg
import random
import sys

# 画面の大きさに関する定数
SCREENRECT = pg.Rect(0, 0, 1321, 701)


# スクリーンを生成するクラス
class Screen:
    def __init__(self, title, size, bgf):
        self.title = title
        self.size = size
        pg.display.set_caption(title)

        # FULLCREEN 変数
        self.winstyle = 0  # |FULLSCREEN
        self.bestdepth = pg.display.mode_ok(SCREENRECT.size, self.winstyle, 32)

        self.sfc = pg.display.set_mode(
            SCREENRECT.size, self.winstyle, self.bestdepth)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgf)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    def full_window(self):
        global fullscreen
        if not fullscreen:
            print("Changing to FULLSCREEN")
            screen_backup = self.sfc.copy()
            self.sfc = pg.display.set_mode(
                SCREENRECT.size, self.winstyle | pg.FULLSCREEN, self.bestdepth
            )
            self.sfc.blit(screen_backup, (0, 0))
        else:
            print("Changing to windowed mode")
            screen_backup = self.sfc.copy()
            self.sfc = pg.display.set_mode(
                SCREENRECT.size, self.winstyle, self.bestdepth
            )
            self.sfc.blit(screen_backup, (0, 0))
        pg.display.flip()
        fullscreen = not fullscreen


# プレイヤー（バー）を生成するクラス
class Player:
    def __init__(self, color, xy, yoko, tate, key_delta, scr: Screen):
        self.sfc = pg.Surface((yoko, tate))  # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc, color, (0, 0, yoko, tate), width=0)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.key_delta = key_delta

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):

        key_dct = pg.key.get_pressed()

        for key, delta in self.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            # if check_bound(self.rct, scr.rct) != (+1, +1):
            #     self.rct.centerx -= delta[0]
            #     self.rct.centery -= delta[1]
        self.blit(scr)


# ボールの描画クラス
class Ball:
    def __init__(self, color, rad, vxy, scr: Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))  # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 100
        self.rct.centery = 100
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


# スコアボードを生成するクラス
class Scoreboard:
    def __init__(self, color, xy, yoko, tate, px, scr: Screen):
        self.sfc = pg.Surface((yoko, tate))  # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc, color, (0, 0, yoko, tate), width=0)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.px = px

    def font_1(self, score: str):
        font = pg.font.Font(None, self.px)
        text = font.render(score, True, (255, 255, 255))
        self.blit(text, [20, 100])

    def font_2(self, score: str):
        font = pg.font.Font(None, self.px)
        text = font.render(score, True, (255, 255, 255))
        self.blit(text, [20, 100])

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.blit(scr)


# ボールの判定に関するクラス
def check_bound(obj_rct, scr_rct):
    # ボールの跳ね返りを判定する
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    global fullscreen
    clock = pg.time.Clock()
    # スクリーンのインスタンスを生成
    scr = Screen("2Dホッケー", SCREENRECT.size, "fig/tennis_court.jpg")
    fullscreen = False  # フルスクリーン無効

    key_delta_p1 = {
        pg.K_w:    [0, -1],
        pg.K_s:  [0, +1],
        pg.K_a:  [-1, 0],
        pg.K_d: [+1, 0],
    }
    # プレイヤー1（画面左側）のインスタンス生成
    p1 = Player((255, 0, 0), (100, 500), 10, 100, key_delta_p1, scr)
    p1.blit(scr)

    key_delta_p2 = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }
    # プレイヤー2（画面右側）のインスタンス生成
    p2 = Player((0, 255, 0), (900, 500), 10, 100, key_delta_p2, scr)
    p2.blit(scr)

    # ボールのインスタンス生成
    ball = Ball((0, 122, 122), 10, (1, 1), scr)
    ball.update(scr)

    board = Scoreboard((0, 0, 255), (670, 680), 500, 100, 55, scr)
    board.update(scr)

    # ゲームが続行している間
    while True:
        scr.blit()
        p1.update(scr)
        p2.update(scr)

        p1_score, p2_score = 0, 0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    scr.full_window()

        ball.update(scr)
        # ボールとの衝突
        if p1.rct.colliderect(ball.rct):
            if ball.vx == 0:
                ball.vx = +1
                ball.vy = random.randint(-1, 1)
            else:
                ball.vx *= -1
        elif p2.rct.colliderect(ball.rct):
            if ball.vx == 0:
                ball.vx = +1
                ball.vy = random.randint(-1, 1)
            else:
                ball.vx *= -1

        if ball.rct.left < scr.rct.left:
            ball.rct.center = (300, 400)
            ball.vx = 0
            ball.vy = 0
            p2_score += 1
        if scr.rct.right < ball.rct.right:  # 出たとき
            ball.rct.center = (1000, 350)
            ball.vx = 0
            ball.vy = 0
            p1_score += 1

        board.update(scr)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
