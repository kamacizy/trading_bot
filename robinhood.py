from praw.models import base
import pyotp
import robin_stocks.robinhood as ro
import sys
import json

lines = open('secret.txt').read().splitlines()

totp=pyotp.TOTP((lines[0])).now()
login = ro.login(str(lines[1]), str(lines[2]), mfa_code=totp)

def QUOTE(ticker):
    r=ro.get_latest_price(ticker)
    print(ticker.upper()+": $"+str(r[0]))

def PROFILE():
    p=ro.build_holdings()
    x=ro.build_user_profile()
    y=ro.load_crypto_profile()

    print("My stock holdings information: \n", p)
    print("My profile information: \n", x)
    print("My c-profile information: \n", y)

def CRYPTOHIST(sym):
    x=ro.get_crypto_historicals(symbol=sym, interval='hour', span='week', bounds='24_7', info=None)
    print("Crypto historicals of: \n", x)

def BUY(sym, amount):
    ro.order_buy_market(sym, amount)

def SELL(sym, amount):
    ro.order_sell_market(sym, amount)



#TICKER = sys.argv[1:][0].upper()
#TRADE(TICKER)
#PROFILE()
#CRYPTOHIST(TICKER)
#QUOTE(TICKER)