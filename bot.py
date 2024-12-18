import pyautogui as bot
import random
import time

time.sleep(5)


msg = "TE AMO MUITO MEU AMOR, VC É A MELHOR COISA QUE ME ACONTECEU, EU TE AMO"

for i in range(1000):
    bot.write(msg)
    bot.press("enter")
    time.sleep(0.5)

print("acabou")