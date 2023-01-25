import phonenumbers
import colorama
import sys,time



from colorama import Fore, Back, Style
colorama.init()
global numberCountryCode


print("         _                           _                         _ ")
print("        | |__   __ _ ___  __ _ _ __ | |____   ____ _ _ __ ___ | |")
print("        | '_ \ / _` / __|/ _` | '_ \| '_ \ \ / / _` | '__/ _ \| |")
print("        | | | | (_| \__ \ (_| | | | | | | \ V / (_| | | | (_) | |")
print("        |_| |_|\__,_|___/\__,_|_| |_|_| |_|\_/ \__,_|_|  \___/|_|")
print("     ")
print(Fore.RED , "                                                    @hasanhvarol")
time.sleep(1)
print(Fore.GREEN + "      Türkçe Telefon numarasından bilgiye hoşgeldiniz")
time.sleep(0.5)
numara = input("Numarayı girin örn: (+905555555555): ")
time.sleep(0.5)
print("            Tarama İşlemleri Başladı")
time.sleep(1)
from phonenumbers import geocoder
number = phonenumbers.parse(numara)
print(Fore.RED ,"- Konum: ", geocoder.description_for_number(number, 'tr'))
time.sleep(1)
from phonenumbers import carrier
number = phonenumbers.parse(numara)
print(Fore.RED, "- Operatör: ", carrier.name_for_number(number, 'tr'))
time.sleep(0.5)
print(" - Ülke Kodu : +90")
time.sleep(1)
from phonenumbers import timezone
number = phonenumbers.parse(numara)
print(Fore.RED, "- Saat: ", timezone.time_zones_for_number(number))