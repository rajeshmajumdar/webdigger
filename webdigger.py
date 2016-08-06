#!/usr/bin/env python
#!WebDigger
#!A simple python program

import httplib
from colorama import init , Style, Back,Fore
import urllib
import socket
import urlparse
import os
import sys
import whois
import time
banner = """
  _  _  _        _        ______   _                         
 (_)(_)(_)      | |      (______) (_)                        
  _   _  _ _____| |       __    _  _   ____   ____ _____  ____ 
 | | || | | ___ | |  _   | |   | || | / _  | /  _ | ___ |/ ___)
 | | || | | ___ | |_) )  | |__/  /| |( (_| |( (_| | ____| |    
 \ _____ /|_____)____/   |_____ / |_| \___ | \___ |_____)_|    
                                     (_____|(_____|
 WebDigger - 
 Author :  Rajesh Majumdar (@freakym0nk)
 Thanks :  Shawar Khan     (www.shawarkhan.com)
    For eliminating some errors.
 """
def webdigger(): #simple
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print (Fore.BLUE+banner)
def again():   #launch again
     inp = raw_input(Fore.RED+"[?] [E]xit or launch [A]gain. (e/a)").lower()
     if inp == 'a':
        webdigger()
        crawler()
     elif inp == 'e':
        print (Fore.GREEN+"[*] Thanks for using WebDigger.")
        exit()
     else:
         print (Fore.RED+"[!] Incorrect argument.")
         again()
def importwl(file, lst):    #wordlist import function
    try:
        with open(file, 'r') as f:
            print (Fore.BLUE+"[+] Gathering required information.")
            for line in f:
                final = str(line.replace("\n",""))
                lst.append(final)
    except IOError:
        print (Fore.RED+"[!] ;( Uh Oh! Seems like database is not there.")
        again()
def crawler(): #main function
    try:
        try:
            url = raw_input(Fore.BLUE+"[?] Enter URL:\n[?] > ")#Takes URL
            if 'www' in url:
                pass
            else:
                url = "www."+url
            if 'https://' in url:
                pass
            elif 'http://' in url:
                pass
            else:
                url = "http://"+url
            print (Fore.GREEN+url+" locked.")
            splittedurl = url.split(".")
            site = splittedurl[1]
            domain = splittedurl[2]
            wordlist = raw_input(Fore.BLUE+"[?] Enter location of your custom database (Press Enter for default one)\n[?] > ")
            if len(wordlist) == 0:
                wordlist = 'wordlist.txt'
                print(Fore.GREEN+wordlist+" selected.")
            else:
                print(Fore.GREEN+wordlist+" selected.")
                pass
            payload = []
            importwl(wordlist,payload)
            print (Fore.BLUE+"[+] WebDigger started digging into web")
            print (Fore.BLUE+"[***] Give me a moment.[***]")
            for x in payload:
                finalurl = site+str(x)
                os.system('whois.pyc '+finalurl)
                with open('output.txt') as response:
                    for line in response:
                        if "No match for" in line:
                            print(Fore.RED+'[;(] '+finalurl+' NOT FOUND.\n')
                        elif "Registrar:" in line:
                            print(Fore.GREEN+'[:)] '+finalurl+' found.')
                        else:
                            pass
                os.remove('output.txt')
            again()
        except(httplib.HTTPResponse, socket.error) as Exit:
            print(Fore.RED+"[!] Something web wrong. :(")
            again()
    except(KeyboardInterrupt) as Exit:
        print(Fore.RED+"\nExit...")
webdigger()
crawler()
            
