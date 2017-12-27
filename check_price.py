from bittrex.bittrex import Bittrex, API_V2_0
import requests

ratio = 1080

bitt = Bittrex(None,None)

bitt_markets = ('ETH-LTC','ETH-ETC','ETH-XRP','ETH-BCC','ETH-QTUM')
coinone_markets = (u'ltc',u'etc',u'xrp',u'bch',u'qtum')

r = requests.get('https://api.coinone.co.kr/ticker/',data={'currency':'eth'})


def krw_to_usd(float krw):
    return krw/ratio

def usd_to_krw(float usd):
    return usd*ratio

def get_Bittrex_price():
    prices = dict()
    for ticker in bitt_markets:
        ask = bitt.get_ticker(ticker)[u'result'][u'Ask']
        bid = bitt.get_ticker(ticker)[u'result'][u'Bid']
        dict[ticker] = (ask,bid)
    return prices

def get_Coinone_price():
    prices = dict()
    for ticker in coinone_markets:
        last = requests.get('https://api.coinone.co.kr/ticker/',{u'currency':ticker})
        prices[ticker.encode('ascii')] = last
    return prices




