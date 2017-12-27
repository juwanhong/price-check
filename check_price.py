from bittrex.bittrex import Bittrex, API_V2_0
import requests

ratio = 1080

bitt = Bittrex(None,None)

bitt_markets = ('ETH-LTC','ETH-ETC','ETH-XRP','ETH-BCC','ETH-QTUM')
coinone_markets = (u'ltc',u'etc',u'xrp',u'bch',u'qtum')

# gives ask/bid prices of coin w.r.t. eth
def get_Bittrex_price():
    prices = dict()
    for ticker in bitt_markets:
        bid = bitt.get_ticker(ticker)[u'result'][u'Bid']
        prices[ticker] = bid
    return prices

# gives last price of coins w.r.t. eth
def get_Coinone_price():
    prices = dict()
    eth = float(requests.get('https://api.coinone.co.kr/ticker/',{u'currency':u'eth'}).json()[u'last'])
    for ticker in coinone_markets:
        last = float(requests.get('https://api.coinone.co.kr/ticker/',{u'currency':ticker}).json()[u'last'])
        prices[ticker.encode('ascii')] = last/eth
    return prices

bitt_prices = get_Bittrex_price()
coinone_prices = get_Coinone_price()

#Steps into checking premium difference
#1.Check price of each coin w.r.t. eth on coinone
#2.Check price of each coin w.r.t. eth on bitt
#3.Calculate price diff (need bitt>coinone)

diff = dict()
diff['ltc'] = bitt_prices['ETH-LTC']-coinone_prices[u'ltc']
diff['etc'] = bitt_prices['ETH-ETC']-coinone_prices[u'etc']
diff['xrp'] = bitt_prices['ETH-XRP']-coinone_prices[u'xrp']
diff['bch'] = bitt_prices['ETH-BCC']-coinone_prices[u'bch']
diff['qtum'] = bitt_prices['ETH-QTUM']-coinone_prices[u'qtum']

for key in diff.keys():
    print key + ' : ' + str(diff[key])



