# -*- coding: utf-8 -*-
import win32ui
import win32print
import win32con

def send_to_printer(title,txt):
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
    hDC.StartDoc(title)
    # hDC.Scale = 60
    hDC.StartPage()
    hDC.SetMapMode(win32con.MM_TWIPS)

    ulc_x = 100
    ulc_y = -100
    lrc_x = 11500
    lrc_y = -11500
    print txt
    print_txt = txt.encode('GBK')
    hDC.DrawText("'\\033[1;31;40m]' D:\\123.txt", (ulc_x, ulc_y, lrc_x, lrc_y), win32con.DT_LEFT)

    hDC.EndPage()
    hDC.EndDoc()

send_to_printer(u"123", u"我的小宝贝,很听话，爱\n<h1>Hello, world</h1>")









