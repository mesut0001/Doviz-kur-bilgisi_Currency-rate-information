from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from modül import *

ayarlar=webdriver.ChromeOptions()
ayarlar.headless=True
driver = webdriver.Chrome(options=ayarlar)

def dolar():
    driver.get("https://www.bloomberght.com/doviz/dolar")
    try:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.downRed").text
    except:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.upGreen").text

def euro():
    driver.get("https://www.bloomberght.com/doviz/euro")
    try:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.downRed").text
    except:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.upGreen").text

def sterlin():
    driver.get("https://www.bloomberght.com/doviz/ingiliz-sterlini")
    try:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.downRed").text
    except:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.upGreen").text

def altınons():
    driver.get("https://www.bloomberght.com/altin/altin-ons")
    try:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.downRed").text
    except:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.upGreen").text

def altıngr():
    driver.get("https://www.bloomberght.com/altin/gram-altin")
    try:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.downRed").text
    except:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.upGreen").text

def btc():
    driver.get("https://www.bloomberght.com/doviz/bitcoin")
    try:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.downRed").text
    except:
        return driver.find_element(by=By.CLASS_NAME, value="LastPrice.upGreen").text


def window ():
    global yazı
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setWindowTitle("Döviz Programı")
    win.setFixedSize(480, 200)
    yazı=QLabel(win)
    yazı.setFont(QFont("Arial", 24))

    buton_dolar = QPushButton("Dolar $", win)
    buton_dolar.setGeometry(50, 20, 60, 50)
    buton_dolar.setStyleSheet("background-color:lightgreen")
    buton_dolar.clicked.connect(dolar_göster)

    buton_euro = QPushButton("Euro €", win)
    buton_euro.setGeometry(100, 20, 60, 50)
    buton_euro.setStyleSheet("background-color:orange")
    buton_euro.clicked.connect(euro_göster)

    buton_sterlin = QPushButton("Sterlin £", win)
    buton_sterlin.setGeometry(160, 20, 60, 50)
    buton_sterlin.setStyleSheet("background-color:pink")
    buton_sterlin.clicked.connect(sterlin_göster)

    buton_altınons = QPushButton("Ons Altın", win)
    buton_altınons.setGeometry(220, 20, 80, 50)
    buton_altınons.setStyleSheet("background-color:Yellow")
    buton_altınons.clicked.connect(altınons_göster)

    buton_altıngr = QPushButton("Gram Altın", win)
    buton_altıngr.setGeometry(300, 20, 80, 50)
    buton_altıngr.setStyleSheet("background-color:LightYellow")
    buton_altıngr.clicked.connect(altıngr_göster)

    buton_btc = QPushButton("Bitcoin ₿", win)
    buton_btc.setGeometry(380, 20, 60, 50)
    buton_btc.setStyleSheet("background-color:LightBlue")
    buton_btc.clicked.connect(btc_göster)


    win.show()
    sys.exit(app.exec())

def dolar_göster():
    yazı.setGeometry(125, 45, 310, 250)
    yazı.setText("1 $ ="+dolar()+" ₺")
def euro_göster():
    yazı.setGeometry(125, 45, 310, 250)
    yazı.setText("1 € ="+euro()+" ₺")
def sterlin_göster():
    yazı.setGeometry(125, 45, 310, 250)
    yazı.setText("1 £ ="+sterlin()+" ₺")
def altınons_göster():
    yazı.setGeometry(115, 45, 310, 250)
    yazı.setText("1 XAU ="+altınons()+" $")
def altıngr_göster():
    yazı.setGeometry(115, 45, 310, 250)
    yazı.setText("1 GAU ="+altıngr()+" ₺")
def btc_göster():
    yazı.setGeometry(115, 45, 310, 250)
    yazı.setText("1 ₿ ="+btc()+" ₺")

window()
