import sys
import traceback
import time
import keyboard
import pyautogui
import numpy as np
from PIL import Image
import matplotlib.pylab as plt
from skimage.metrics import structural_similarity as ssim
from skimage.feature import match_template
import cv2
from datetime import datetime
#%matplotlib inline
import sqlite3
from sqlite3 import Error
from playsound import playsound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import requests
from win32api import GetSystemMetrics
#from tkinter import *

def breakescape():
    global  __continuea__
    __continuea__ = True

def parar():
    global __continuea__
    __continuea__ = False

def hcorrer():
    correr()

def hsalir():
    salir_combate()

def hotluma():
    takescreen()
    print('Hay luma')
    bolv = hayluma_3()
    if bolv:
        alarma()
    print(str(bolv))
    #print(str(strssm))

def hotluma2():
    print('Hay luma3')
    bolv = hayluma_3()
    if bolv:
        alarma()
    print(str(bolv))

def hotsolo():
    takescreen()
    print('Esta solo')
    bolv = esta_solo()
    print(str(bolv))

def hotbig():
    print('Hay bigu')
    bolv = numero_bigu()
    print(str(bolv))

def hotgyalis():
    print('Hay bigu')
    bolv = numero_gyalis()
    print(str(bolv))

def hotshuine():
    print('Hay shuine')
    bolv = hayshuine()
    print(str(bolv))

def hotwiplump():
    print('Hay wimplum')
    bolv = solo_wiplump()
    print(str(bolv))

def hotcritico():
    print('Hay critico')
    bolv = haycritico()
    print(str(bolv))

def hotukama():
    print('Hay ukama')
    bolv = hayukama()
    print(str(bolv))

def initbuscarluma(temtem_route, isbot):
    global __continuea__
    __continuea__ = False
    '''con = sql_connection()
    sql_table(con)
    entities = (1, 0)
    sql_insert(con, entities)'''
    if isbot:
        keyboard.add_hotkey('f1', breakescape)
        keyboard.add_hotkey('f2', parar)
    else:
        keyboard.add_hotkey('f1', hcorrer)
        keyboard.add_hotkey('f2', hsalir)
    keyboard.add_hotkey('f3', hotluma)
    keyboard.add_hotkey('f4', hotluma2)


    # keyboard.call_later(breakescape())
    hayc = False
    count = 0
    while True:
        if __continuea__:
            try:
                if not hayc:
                    correr()
                else:
                    if numero_temtem(temtem_route) > 0:
                        aumentarContador()
                    luma1 = hayluma()
                    luma3 = hayluma_2()
                    luma5 = hayluma_3()
                    if luma1 or luma3 or luma5:

                        sendnotificationLuma()
                        time.sleep(1)
                        sendnotificationLuma()
                        time.sleep(1)
                        sendnotificationLuma()
                        alarma()
                        __continuea__ = False
                        break
                    else:
                        salir_combate()
                    count = 0
                    hayc = False
                    ''''''
                time.sleep(0.5)
                if count >= 2:
                    hayc = haycombate()
                count += 1
            except Exception:
                print(u'Error', )
                print(traceback.print_exc(), file=sys.stderr)

def initcapturar():
    global __continuea__
    __continuea__ = False
    keyboard.add_hotkey('f1', breakescape)
    keyboard.add_hotkey('f2', parar)
    keyboard.add_hotkey('f3', hotluma)
    #keyboard.add_hotkey('f3', hotshuine)
    keyboard.add_hotkey('f4', hotsolo)
    keyboard.add_hotkey('f5', hotwiplump)
    # keyboard.call_later(breakescape())
    hayc = False
    count = 0
    while True:
        if __continuea__:
            try:
                hayc = haycombate()
                rcapturado = estacapturado()
                if estaMenu():
                    print('Menu 108')
                    keyboard.press_and_release('esc')
                    time.sleep(.2)
                elif estaMenuCombate():
                    print('Menu 108')
                    keyboard.press_and_release('esc')
                    time.sleep(.4)
                if rcapturado:
                    print("Liberando")
                    #liberar()
                    if hay_50():
                        print("Guardando")
                        guardar()
                    else:
                        print("Liberando")
                        liberar()

                elif not hayc:
                    print("Corriendo")
                    correr()

                else:
                    print("Luma")
                    luma1 = hayluma()

                    if luma1:
                        __continuea__ = False
                        break
                    else:
                        hayShuine = hayshuine()
                        if hayShuine:
                            print("Shuine")
                            salir_combate()
                        else:
                            print("Esta capturado 123")
                            rcapturado = estacapturado()

                            if rcapturado:
                                print("Liberando 127")
                                #liberar()
                                if hay_50():
                                    print("Guardando")
                                    guardar()
                                else:
                                    print("Liberando")
                                    liberar()
                            else:
                                print("Capturando 130")
                                capturar_guardar()
                time.sleep(1.6)

            except Exception:
                print(u'Error', )
                print(traceback.print_exc(), file=sys.stderr)

def capturar():
    capturado = False
    countcombate = 0
    resultcombate = -1
    isRondaDos = False
    while not capturado:
        rcapturado = estacapturado()
        rsuelto = estasuelto()

        if rcapturado:
            print('Liberando 147')
            #liberar()
            guardar()
            if resultcombate != 1:
                capturado = True
                isRondaDos = False
                break
            else:
                isRondaDos = True

        if rsuelto:
            print('Correr 151')
            capturado = True
            break
        if estaMenu():
            print('Menu suelto')
            capturado = True
            keyboard.press_and_release('esc')
            time.sleep(.2)
            break
        if estaMenuCombate():
            print('Menu 157')
            keyboard.press_and_release('esc')
            time.sleep(.2)
            keyboard.press_and_release('esc')
            time.sleep(.2)
            keyboard.press_and_release('esc')

        bolhayCombate = haycombate()
        if not bolhayCombate:
            print('No hay combate 157')
            print(str(capturado))
            if countcombate > 6:
                keyboard.press_and_release('esc')
                time.sleep(.2)
                keyboard.press_and_release('esc')
                time.sleep(.2)
                keyboard.press_and_release('esc')
                time.sleep(5)
                continue
            countcombate += 1
            time.sleep(1)
        elif hayanimacion():
            countcombate = 0
            print('Hay animacion')
            time.sleep(2)
        else:
            countcombate = 0
            print('Combate 170')
            resultcombate = tipocombate()
            if resultcombate == 5 or resultcombate == 6:
                estasolo = True
            elif resultcombate == 2:
                keyboard.press_and_release('1')
                time.sleep(.8)
                keyboard.press_and_release('f')
                time.sleep(.8)
                keyboard.press_and_release('2')
                time.sleep(.8)
                keyboard.press_and_release('f')
                break
            else:
                estasolo = False

            if estadodormido():
                if estadocongelado():
                    if estasolo:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(2)
                    else:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('6')
                        time.sleep(2)
                elif estadoenfriamiento():
                    if estasolo:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(2)
                    else:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('6')
                        time.sleep(2)
                else:
                    if estasolo:
                        print('Solo dormido')
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        keyboard.press_and_release('f')
                        time.sleep(2)
                    else:
                        print('Dos dormido')
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('6')
                        keyboard.press_and_release('6')
                        time.sleep(2)
            else:
                if estadocongelado():
                    if estasolo:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(2)
                    else:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('6')
                        time.sleep(2)
                elif estadoenfriamiento():
                    keyboard.press_and_release('3')
                    time.sleep(.8)
                    keyboard.press_and_release('f')
                    time.sleep(.8)
                    keyboard.press_and_release('1')
                    time.sleep(.8)
                    keyboard.press_and_release('f')
                    time.sleep(2)
                else:
                    if isRondaDos:
                        keyboard.press_and_release('6')
                        time.sleep(2)
                        keyboard.press_and_release('1')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                    else:
                        keyboard.press_and_release('1')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('1')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                    if estasolo:
                        time.sleep(2)
                    else:
                        time.sleep(2)
        '''if estaatorado1():
            keyboard.press_and_release('esc')
            time.sleep(.8)
            print('Atorado')'''

def capturar_guardar():
    capturado = False
    countcombate = 0
    resultcombate = -1
    isRondaDos = False
    while not capturado:
        rcapturado = estacapturado()
        rsuelto = estasuelto()

        if rcapturado:
            print('Liberando 147')
            #liberar()
            if hay_50():
                print("Guardando")
                guardar()
            else:
                print("Liberando")
                liberar()
            if resultcombate != 1:
                capturado = True
                isRondaDos = False
                break
            else:
                isRondaDos = True

        if rsuelto:
            print('Correr 151')
            capturado = True
            break
        if estaMenu():
            print('Menu suelto')
            capturado = True
            keyboard.press_and_release('esc')
            time.sleep(.2)
            break
        if estaMenuCombate():
            print('Menu 157')
            keyboard.press_and_release('esc')
            time.sleep(.2)
            keyboard.press_and_release('esc')
            time.sleep(.2)
            keyboard.press_and_release('esc')

        bolhayCombate = haycombate()
        if not bolhayCombate:
            print('No hay combate 451')
            print(str(capturado))
            if countcombate > 6:
                keyboard.press_and_release('esc')
                time.sleep(.2)
                keyboard.press_and_release('esc')
                time.sleep(.2)
                keyboard.press_and_release('esc')
                time.sleep(5)
                continue
            countcombate += 1
            time.sleep(1)
        elif hayanimacion():
            countcombate = 0
            print('Hay animacion')
            time.sleep(2)
        else:
            countcombate = 0
            print('Combate 170')

            besta_solo = esta_solo()
            print("esta solo: "  +  str(besta_solo))
            if estadocongelado() :#or estadocongelado2()
                keyboard.press_and_release('7')
                time.sleep(.8)
                keyboard.press_and_release('f')
                time.sleep(.8)
                print("Congelado")
                if not besta_solo:
                    keyboard.press_and_release('f')
                    time.sleep(.8)
                    keyboard.press_and_release('7')
                    time.sleep(.8)
                    keyboard.press_and_release('f')
                    time.sleep(.8)
                    keyboard.press_and_release('up')
                    time.sleep(.8)
                    keyboard.press_and_release('f')
                    time.sleep(.8)
                else:
                    keyboard.press_and_release('7')
                    time.sleep(.8)
                    keyboard.press_and_release('f')
                    time.sleep(.8)
            elif estadoenfriamiento():
                print("Enfriamiento")
                keyboard.press_and_release('1')
                time.sleep(.8)
                keyboard.press_and_release('f')
                time.sleep(.8)
                if not besta_solo:
                    keyboard.press_and_release('1')
                    time.sleep(.8)
                    keyboard.press_and_release('up')
                    time.sleep(.8)
                    keyboard.press_and_release('f')
                else:
                    keyboard.press_and_release('1')
                    time.sleep(.8)
                    keyboard.press_and_release('f')
                time.sleep(2)
            else:
                print("Ninguno")
                keyboard.press_and_release('1')
                time.sleep(.5)
                keyboard.press_and_release('f')
                time.sleep(.5)
                keyboard.press_and_release('1')
                time.sleep(.5)
                if not besta_solo:
                    keyboard.press_and_release('up')
                    time.sleep(.8)
                keyboard.press_and_release('f')
                time.sleep(2)



def liberar():
    time.sleep(.8)
    keyboard.press_and_release('left')
    time.sleep(.8)
    keyboard.press_and_release('right')
    time.sleep(.8)
    keyboard.press_and_release('f')
    time.sleep(.8)
    keyboard.press_and_release('f')

def guardar():
    time.sleep(.8)
    keyboard.press_and_release('left')
    time.sleep(.8)
    keyboard.press_and_release('f')
    time.sleep(.5)
    keyboard.press_and_release('f')


def capturar2():
    capturado = False

    while not capturado:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'./img/screenshot1.png')
        rcapturado = estacapturado()
        rsuelto = estasuelto()
        if rcapturado:
            print('Capturado')
            guardar()
            capturado = True
        elif rsuelto:
            print('soltar')
            capturado = True
        else:
            resultcombate = tipocombate()
            if resultcombate == 5 or resultcombate == 6:
                estasolo = True
            else:
                estasolo = False


            if estadodormido():
                if estadocongelado():
                    if estasolo:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(17)
                    else:
                        keyboard.press_and_release('7')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(.8)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('6')
                        time.sleep(8)
                elif estadoenfriamiento():
                    if estasolo:
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(17)
                    else:
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('6')
                        time.sleep(8)
                else:
                    if estasolo:
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(17)
                    else:
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('6')
                        time.sleep(8)
            else:
                if estadocongelado():
                    if estasolo:
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(17)
                    else:
                        keyboard.press_and_release('7')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('f')
                        time.sleep(1)
                        keyboard.press_and_release('6')
                        time.sleep(10)
                elif estadoenfriamiento():
                    keyboard.press_and_release('3')
                    time.sleep(1)
                    keyboard.press_and_release('f')
                    time.sleep(1)
                    keyboard.press_and_release('1')
                    time.sleep(1)
                    keyboard.press_and_release('f')
                    time.sleep(6)
                else:
                    keyboard.press_and_release('1')
                    time.sleep(1)
                    keyboard.press_and_release('f')
                    time.sleep(1)
                    keyboard.press_and_release('1')
                    time.sleep(1)
                    keyboard.press_and_release('f')
                    print('Inicio')
                    if estasolo:
                        time.sleep(14)
                    else:
                        time.sleep(20)





def correr():
    # print(str(__continuea__))
    keyboard.press('up')
    time.sleep(1)
    keyboard.release('up')
    keyboard.press('down')
    time.sleep(0.9)
    keyboard.release('down')
    keyboard.press('up')
    time.sleep(1)
    keyboard.release('up')
    keyboard.press('down')
    time.sleep(0.9)
    keyboard.release('down')

def correrabajo():
    # print(str(__continuea__))
    keyboard.press('down')
    time.sleep(0.7)
    keyboard.release('down')
    keyboard.press('up')
    time.sleep(0.5)
    keyboard.release('up')
    keyboard.press('down')
    time.sleep(0.7)
    keyboard.release('down')
    keyboard.press('up')
    time.sleep(0.5)
    keyboard.release('up')

def press3timesF():
    keyboard.press_and_release('f')
    time.sleep(0.5)
    keyboard.press_and_release('f')
    time.sleep(1)



def combatirk():
    keyboard.press_and_release('1')
    time.sleep(0.5)
    keyboard.press_and_release('f')
    time.sleep(0.8)
    keyboard.press_and_release('1')
    time.sleep(0.5)
    keyboard.press_and_release('f')

def salir_combate():
    keyboard.press_and_release('8')
    time.sleep(0.3)
    keyboard.press_and_release('8')

def haycombate():
    #print('Entro')
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./img/screenshot1.png')
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    #img_rgb = cv2.imread('mario.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(r'./img/template6.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True

    if result:
        img_rgb = cv2.imread(r'./img/screenshot1.png')
        now = datetime.now()  # current date and time
        year = now.strftime("%m%d%Y%H%M%S")
        #cv2.imwrite('./img/combate/c' + year + '.png', img_rgb)
    plt.close('all')
    myScreenshot = None
    img_rgb = None
    img_gray = None
    template = None


    return result



def haycombate2():
    combate = False
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./img/screenshot1.png')
    im = plt.imread(r'./img/screenshot1.png')
    #print(im.shape)
    im.shape
    im = im[599:745, 548:734, :]
    plti(im)
    plt.imsave(r'./img/screenshot2.png', im)
    plt.close()
    myScreenshot = None
    #print(im.shape)
    #print(combate)
    template = cv2.imread(r'./img/template.png')
    screen = cv2.imread(r'./img/screenshot2.png')
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    mse, ssim = compare_images(template, screen, "Templae vs. Live")
    #print("MSE: %.2f, SSIM: %.2f" % (mse, ssim))
    if mse < 200.0 or ssim > 0.70:
        print('hay combate ')
        return True
    else:
        return False

def estaMenu():
    #print('Entro')
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_menu.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    return result

def estaMenuCombate():
    #print('Entro')
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_menu_combate.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def en_Menu():
    result = estaMenu() or estaMenuCombate()
    return  result

def takescreen():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./img/screenshot1.png')

def hayluma():
    #print('Entro')
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'./img/screenshot1.png')
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    #img_rgb = cv2.imread('mario.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(r'./img/template5.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        print('Hay luma')
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    if result:
        now = datetime.now()  # current date and time
        year = now.strftime("%m%d%Y%H%M%S")
        #print("year:", year)
        cv2.imwrite('./img/Luma'+year+'.png', img_rgb)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def hayluma_2():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    #img_rgb = cv2.imread('mario.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(r'./img/template_luma3.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        print('Hay luma')
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    if result:
        now = datetime.now()  # current date and time
        year = now.strftime("%m%d%Y%H%M%S")
        #print("year:", year)
        cv2.imwrite('./img/Luma'+year+'.png', img_rgb)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def hayluma_3():
    result = False
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    data = np.array(img_rgb)

    r1, g1, b1 = 255, 255, 255  # Original value
    r2, g2, b2 = 255, 255, 255#0, 0, 0  # Value that we want to replace it with

    red, green, blue = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:, :, :3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)
    im.save('./img/screenshotr.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(r'./img/template_luma4.png', 0)
    w, h = template.shape[::-1]
    cv2.imwrite('./img/test.png', img_gray)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        print('Hay luma')
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    if result:
        now = datetime.now()  # current date and time
        year = now.strftime("%m%d%Y%H%M%S")
        #print("year:", year)
        cv2.imwrite('./img/Luma'+year+'.png', img_rgb)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def hayluma_4():
    result = False
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    data = np.array(img_rgb)

    r1, g1, b1 = 255, 255, 255  # Original value
    r2, g2, b2 = 255, 255, 255#0, 0, 0  # Value that we want to replace it with

    red, green, blue = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:, :, :3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)
    im.save('./img/screenshotr.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(r'./img/template_luma4.png', 0)
    w, h = template.shape[::-1]
    cv2.imwrite('./img/test.png', img_gray)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        print('Hay luma')
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    if result:
        now = datetime.now()  # current date and time
        year = now.strftime("%m%d%Y%H%M%S")
        #print("year:", year)
        cv2.imwrite('./img/Luma'+year+'.png', img_rgb)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def hayshuine():
    #print('Entro')
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(r'./img/screenshot1.png')
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    #img_rgb = cv2.imread('mario.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(r'./img/template_shuine.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def hayblooze():
    #print('Entro')
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(r'./img/screenshot1.png')
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    #img_rgb = cv2.imread('mario.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(r'./img/template_blooze.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def haytemtem(templateruta):
    #print('Entro')
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(r'./img/screenshot1.png')
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    #img_rgb = cv2.imread('mario.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #template = cv2.imread('mario_coin.png', 0)
    template = cv2.imread(templateruta, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def haycritico():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_critico.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def estadoenfriamiento():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_enfriamineto.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def estadocongelado():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_congelado.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def hay_50():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_50.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def estadocongelado2():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_congelado2.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    print('Estado congelado2:')
    print(result)
    return result

def hayanimacion():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_animacion.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def estaatorado1():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_atorado_1.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    now = datetime.now()  # current date and time
    year = now.strftime("%m%d%Y%H%M%S")
    if result:
        cv2.imwrite('./img/atorado' + year + '.png', img_rgb)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def estadodormido():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_dormido.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def hayukama():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_ukama.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def estacapturado():
    result = estacapturado1() or estacapturado2()

    return result

def estacapturado1():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_capturado.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result


def estacapturado2():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_capturado2.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result


def estasuelto():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_suelto.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def tipocombate():
    resultado = 0
    ukamac = solo_ukama()
    wimlump = solo_wiplump()

    if ukamac == 2:
        resultado = 1
    elif ukamac == 1 and wimlump == 1:
        resultado = 4
    elif ukamac == 0 and wimlump == 2:
        resultado = 2
    elif ukamac == 0 and wimlump == 1:
        resultado = 6
    elif ukamac == 1:
        resultado = 5
    '''result = doble_ukama()
    if not result:
        result = der_ukama()
        resultado = 3
        if not result:
            result = izq_ukama()
            resultado = 4
            if not result:
                result = doble_wiplump()
                resultado = 2
                if not result:
                    result = solo_ukama()
                    resultado = 5
                    if not result:
                        result = solo_wiplump()
                        resultado = 6
                        if not result:
                            resultado = -1'''
    print('Tipo de combate')
    print(resultado)
    print(ukamac)
    print(wimlump)
    return resultado

def doble_ukama():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_ukama_doble.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result



def doble_wiplump():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_wiplump_doble.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    plt.close('all')
    img_rgb = None
    img_gray = None
    template = None
    return result

def izq_ukama():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_ukama_izq.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return result

def der_ukama():
    img_rgb = cv2.imread(r'./img/screenshot1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_ukama_der.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    result = False
    for pt in zip(*loc[::-1]):
        result = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return result

def esta_solo():
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    im2 = im2[25:80, 800:1080, :]
    plti(im2)
    plt.imsave(r'./img/estasolo.png', im2)
    img_rgb2 = cv2.imread(r'./img/estasolo.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_vida.png', 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    estasolo = True
    for pt in zip(*loc[::-1]):
        estasolo = False
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return estasolo


def solo_ukama():
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    im2 = im2[40:90, 1090:1250, :]
    plti(im2)
    plt.imsave(r'./img/hayu2.png', im2)
    img_rgb2 = cv2.imread(r'./img/hayu2.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_ukama_solo.png', 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    hayWimp2 = False
    for pt in zip(*loc[::-1]):
        hayWimp2 = True
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    im = plt.imread(r'./img/screenshot1.png')
    im.shape
    im = im[10:60, 810:970, :]
    plti(im)
    plt.imsave(r'./img/hayu1.png', im)
    img_rgb = cv2.imread(r'./img/hayu1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    hayWimp1 = False
    for pt in zip(*loc[::-1]):
        hayWimp1 = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    if hayWimp1 and hayWimp2:
        result = 2
    elif hayWimp1 or hayWimp2:
        result = 1
    else:
        result = 0
    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return result

def solo_wiplump():
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    im2 = im2[40:90, 1090:1250, :]
    plti(im2)
    plt.imsave(r'./img/hayw2.png', im2)
    img_rgb2 = cv2.imread(r'./img/hayw2.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_wiplump_solo.png', 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    hayWimp2 = False
    for pt in zip(*loc[::-1]):
        hayWimp2 = True
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    im = plt.imread(r'./img/screenshot1.png')
    im.shape
    im = im[10:60, 810:970, :]
    plti(im)
    plt.imsave(r'./img/hayw1.png', im)
    img_rgb = cv2.imread(r'./img/hayw1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    hayWimp1 = False
    for pt in zip(*loc[::-1]):
        hayWimp1 = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    if hayWimp1 and hayWimp2:
        result = 2
    elif hayWimp1 or hayWimp2:
        result = 1
    else:
        result = 0
    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return result

def plti(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    #plt.show()
    plt.close('all')
    imageA = None
    imageB = None
    return m, s


def sql_connection():

    try:

        con = sqlite3.connect('temtem.db')

        #print("Connection is established: Database is created in memory")

    except Error:

        print(Error)

    return con

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE contador(id integer PRIMARY KEY, contc integer)")

    con.commit()


def sql_insert(con, entities):
    cursorObj = con.cursor()

    cursorObj.execute(
        'INSERT INTO contador(id, contc) VALUES(?, ?)', entities)

    con.commit()

def sql_update(con, entities):

    cursorObj = con.cursor()

    cursorObj.execute('UPDATE contador SET cont = ? where id = 1', entities)

    con.commit()

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT contc FROM contador where id = 1')

    rows = cursorObj.fetchall()

    for row in rows:
        return row[0]
    return None

def initdatabase():
    con = sql_connection()
    sql_table(con)
    entities = (1, 0)
    sql_insert(con, entities)
    con.close()

def getCombatCount():
    con = sql_connection()
    print('Contador:')
    contador = sql_fetch(con)
    con.close()
    return contador

def sql_update(con):

    cursorObj = con.cursor()
    contador = int(sql_fetch(con))
    contador += 1
    valores = contador
    cursorObj.execute('UPDATE contador SET contc = ' + str(valores) +' where id = 1')

    con.commit()
    
def aumentarContador():
    con = sql_connection()
    sql_update(con)
    con.close()
#doesntwork
def hay_luma_exact():
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    x1 = int(round(0.0 * height, 0))
    x2 = int(round(0.98 * height, 0))
    y1 = int(round(0.0 * width, 0))
    y2 = int(round(0.9150805 * width, 0))

    im2 = im2[x1:x2, y1:y2, :]
    #im2 = im2[40:90, 1090:1250, :]
    plti(im2)
    plt.imsave(r'./img/hayb2.png', im2)
    img_rgb2 = cv2.imread(r'./img/hayb2.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/lumastar2.png', 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    hayBigu2 = False
    for pt in zip(*loc[::-1]):
        hayBigu2 = True
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    im = plt.imread(r'./img/screenshot1.png')
    im.shape
    x1 = int(round(0.0130208 * height, 0))
    #x2 = int(round(0.0781250 * height, 0))
    #x2 = int(round(0.28 * height, 0))
    y1 = int(round(0.5929721 * width, 0))
    y2 = int(round(0.7101024 * width, 0))
    im = im[x1:x2, y1:y2, :]
    #im = im[10:60, 810:970, :]
    plti(im)
    plt.imsave(r'./img/hayb1.png', im)
    img_rgb = cv2.imread(r'./img/hayb1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    hayBigu1 = False
    for pt in zip(*loc[::-1]):
        hayBigu1 = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    if hayBigu1 and hayBigu2:
        result = 2
    elif hayBigu1 or hayBigu2:
        result = 1
    else:
        result = 0
    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return result

def numero_temtem(temtem_route):
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    x1 = int(round(0.052083333 * height, 0))
    x2 = int(round(0.1171875 * height, 0))
    y1 = int(round(0.7950219 * width, 0))
    y2 = int(round(0.9150805 * width, 0))

    im2 = im2[x1:x2, y1:y2, :]
    #im2 = im2[40:90, 1090:1250, :]
    plti(im2)
    plt.imsave(r'./img/hayb2.png', im2)
    img_rgb2 = cv2.imread(r'./img/hayb2.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(temtem_route, 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    hayBigu2 = False
    for pt in zip(*loc[::-1]):
        hayBigu2 = True
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    im = plt.imread(r'./img/screenshot1.png')
    im.shape
    x1 = int(round(0.0130208 * height, 0))
    x2 = int(round(0.0781250 * height, 0))
    y1 = int(round(0.5929721 * width, 0))
    y2 = int(round(0.7101024 * width, 0))
    im = im[x1:x2, y1:y2, :]
    #im = im[10:60, 810:970, :]
    plti(im)
    plt.imsave(r'./img/hayb1.png', im)
    img_rgb = cv2.imread(r'./img/hayb1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    hayBigu1 = False
    for pt in zip(*loc[::-1]):
        hayBigu1 = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    if hayBigu1 and hayBigu2:
        result = 2
    elif hayBigu1 or hayBigu2:
        result = 1
    else:
        result = 0
    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return result


def numero_bigu():
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    im2 = im2[40:90, 1090:1250, :]
    plti(im2)
    plt.imsave(r'./img/hayb2.png', im2)
    img_rgb2 = cv2.imread(r'./img/hayb2.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_bigu.png', 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    hayBigu2 = False
    for pt in zip(*loc[::-1]):
        hayBigu2 = True
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    im = plt.imread(r'./img/screenshot1.png')
    im.shape
    im = im[10:60, 810:970, :]
    plti(im)
    plt.imsave(r'./img/hayb1.png', im)
    img_rgb = cv2.imread(r'./img/hayb1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    hayBigu1 = False
    for pt in zip(*loc[::-1]):
        hayBigu1 = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    if hayBigu1 and hayBigu2:
        result = 2
    elif hayBigu1 or hayBigu2:
        result = 1
    else:
        result = 0
    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return result

def numero_gyalis():
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    im2 = im2[40:90, 1090:1250, :]
    plti(im2)
    plt.imsave(r'./img/hayg2.png', im2)
    img_rgb2 = cv2.imread(r'./img/hayg2.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_gyalis.png', 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    hayGyalis2 = False
    for pt in zip(*loc[::-1]):
        hayGyalis2 = True
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    im = plt.imread(r'./img/screenshot1.png')
    im.shape
    im = im[10:60, 810:970, :]
    plti(im)
    plt.imsave(r'./img/hayg1.png', im)
    img_rgb = cv2.imread(r'./img/hayg1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    hayGyalis1 = False
    for pt in zip(*loc[::-1]):
        hayGyalis1 = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    if hayGyalis1 and hayGyalis2:
        result = 2
    elif hayGyalis1 or hayGyalis2:
        result = 1
    else:
        result = 0
    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return result

def numero_banapi():
    im2 = plt.imread(r'./img/screenshot1.png')
    im2.shape
    im2 = im2[40:90, 1090:1250, :]
    plti(im2)
    plt.imsave(r'./img/hayb2.png', im2)
    img_rgb2 = cv2.imread(r'./img/hayb2.png')
    img_gray2 = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'./img/template_banapi.png', 0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res2 >= threshold)
    hayBanapi2 = False
    for pt in zip(*loc[::-1]):
        hayBanapi2 = True
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    im = plt.imread(r'./img/screenshot1.png')
    im.shape
    im = im[10:60, 810:970, :]
    plti(im)
    plt.imsave(r'./img/hayb1.png', im)
    img_rgb = cv2.imread(r'./img/hayb1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    hayBpanapi1 = False
    for pt in zip(*loc[::-1]):
        hayBpanapi1 = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    if hayBpanapi1 and hayBanapi2:
        result = 2
    elif hayBpanapi1 or hayBanapi2:
        result = 1
    else:
        result = 0
    plt.close('all')
    im = None
    img_rgb = None
    img_gray = None
    im2 = None
    img_rgb2 = None
    img_gray2 = None
    return result


def initbuscarlumaBigu():
    global __continuea__
    __continuea__ = False
    keyboard.add_hotkey('f1', breakescape)
    keyboard.add_hotkey('f2', parar)
    keyboard.add_hotkey('f3', hotluma)
    keyboard.add_hotkey('f4', hotbig)


    # keyboard.call_later(breakescape())
    hayc = False
    count = 0
    while True:
        if __continuea__:
            try:
                if not hayc:

                    correr()
                else:
                    luma1 = hayluma()
                    luma2 = hayluma()
                    #luma3 = hayluma()
                    if numero_bigu() > 0:
                        aumentarContador()
                    if luma1 or luma2:
                        __continuea__ = False
                        break
                    else:
                        salir_combate()
                    count = 0
                    hayc = False
                    ''''''
                time.sleep(0.5)
                if count >= 2:
                    hayc = haycombate()
                count += 1
            except Exception:
                print(u'Error', )
                print(traceback.print_exc(), file=sys.stderr)

def initbuscarlumaBanapi():
    global __continuea__
    __continuea__ = False
    keyboard.add_hotkey('f1', breakescape)
    keyboard.add_hotkey('f2', parar)
    keyboard.add_hotkey('f3', hotluma)
    keyboard.add_hotkey('f4', hotbig)


    # keyboard.call_later(breakescape())
    hayc = False
    count = 0
    while True:
        if __continuea__:
            try:
                if not hayc:
                    correr()
                else:
                    luma1 = hayluma()
                    luma2 = hayluma()
                    #luma3 = hayluma()
                    if numero_banapi() > 0:
                        aumentarContador()
                    if luma1 or luma2:
                        alarma()
                        __continuea__ = False
                        break
                    else:
                        salir_combate()
                    count = 0
                    hayc = False
                    ''''''
                time.sleep(0.5)
                if count >= 2:
                    hayc = haycombate()
                count += 1
            except Exception:
                print(u'Error', )
                print(traceback.print_exc(), file=sys.stderr)

def initbuscarlumaGyalis():
    global __continuea__
    __continuea__ = False
    keyboard.add_hotkey('f1', breakescape)
    keyboard.add_hotkey('f2', parar)
    keyboard.add_hotkey('f3', hotluma)
    keyboard.add_hotkey('f4', hotgyalis)


    # keyboard.call_later(breakescape())
    hayc = False
    count = 0
    while True:
        if __continuea__:
            try:
                if not hayc:
                    correr()
                else:
                    luma1 = hayluma()
                    luma2 = hayluma()
                    #luma3 = hayluma()
                    if numero_gyalis() > 0:
                        aumentarContador()
                    if luma1 or luma2:
                        alarma()
                        __continuea__ = False
                        break
                    else:
                        salir_combate()
                    count = 0
                    hayc = False
                    ''''''
                time.sleep(0.5)
                if count >= 2:
                    hayc = haycombate()
                count += 1
            except Exception:
                print(u'Error', )
                print(traceback.print_exc(), file=sys.stderr)

def combatir():
    global __continuea__
    __continuea__ = False
    keyboard.add_hotkey('f1', breakescape)
    keyboard.add_hotkey('f2', parar)
    keyboard.add_hotkey('f3', hotluma)

    luma1 = hayluma()
    # keyboard.call_later(breakescape())
    hayc = False
    count = 0
    while True:
        if __continuea__:
            try:
                if not hayc:
                    correr()
                    press3timesF()
                else:

                    #luma2 = hayluma()
                    #luma3 = hayluma()

                    if luma1 :
                        alarma()
                        __continuea__ = False
                        break
                    else:
                        if hayblooze():# or haytemtem(r'./img/template_tuwai.png'):
                            salir_combate()
                        else:
                            combatirk()
                    count = 0
                    hayc = False
                    ''''''
                time.sleep(0.5)
                if count >= 2:
                    hayc = haycombate()
                count += 1
            except Exception:
                print(u'Error', )
                print(traceback.print_exc(), file=sys.stderr)

def combatirabajo():
    global __continuea__
    __continuea__ = False
    keyboard.add_hotkey('f1', breakescape)
    keyboard.add_hotkey('f2', parar)
    keyboard.add_hotkey('f3', hotluma)

    luma1 = hayluma()
    # keyboard.call_later(breakescape())
    hayc = False
    count = 0
    while True:
        if __continuea__:
            try:
                if not hayc:
                    correrabajo()
                    press3timesF()
                else:

                    #luma2 = hayluma()
                    #luma3 = hayluma()

                    if luma1 :
                        alarma()
                        __continuea__ = False
                        break
                    else:
                        combatirk()
                    count = 0
                    hayc = False
                    ''''''
                time.sleep(0.5)
                if count >= 2:
                    hayc = haycombate()
                count += 1
            except Exception:
                print(u'Error', )
                print(traceback.print_exc(), file=sys.stderr)


def alarma():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Control volume
    # volume.SetMasterVolumeLevel(-0.0, None) #max
    # volume.SetMasterVolumeLevel(-5.0, None) #72%
    volume.SetMasterVolumeLevel(-20.0, None)  # 51%
    playsound(r'./sound/loop.wav')
    volume.SetMasterVolumeLevel(-10.0, None)
    playsound(r'./sound/loop.wav')
    time.sleep(1)
    volume.SetMasterVolumeLevel(-5.0, None)
    playsound(r'./sound/loop.wav')
    volume.SetMasterVolumeLevel(-2.0, None)
    playsound(r'./sound/loop.wav')

def sendnotificationLuma():


    # api-endpoint
    URL = "https://v2-dot-hcmapp-271019.appspot.com/api/candidato/testnotificaction"

    # location given here
    location = "delhi technological university"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address': location}

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    #data = r.json()
'''
def launchwindow():
    root = Tk()
    root.title("Tem")
    root.wm_attributes("-topmost", 1)
    root.attributes('-alpha', 0.3)
    root.overrideredirect(1)
    root.overrideredirect(True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(True)
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()'''


#launchwindow()
print(getCombatCount())
#initbuscarluma(r'./img/template_valash.png', True)
#initdatabase()
#numero_temtem(r'./img/template_umishi.png')
#sendnotificationLuma()
initcapturar()

#aumentarContador()
#print(getCombatCount())


#combatir()
#combatirabajo()
#print(getCombatCount())