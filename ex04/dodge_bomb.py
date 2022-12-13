import pygame as pg
import sys


def main():
    clock = pg.time.Clock()
    # 練習1
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.update()
        clock.tick(1000)
    """
    pgbg_sfc = pg.transform.rotozoom(pgbg_sfc, 0, 2.0)
    pgbg_rct.center = 400, 300
    """


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
