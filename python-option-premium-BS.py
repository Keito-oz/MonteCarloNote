#修正BS式

#正規分布の確率分布関数をインポート
from scipy.stats import norm
#指数関数、対数関数、二乗根関数をインポート
from math import exp,log,sqrt

#コール・オプションの価格関数を定義
def BS_Call(S0, sigma ,r,q,T,K):
    d1 = (log(S0 / K) + (r - q ) * T) / (sigma * sqrt(T))+sigma*sqrt(T)/ 2
    d2 = (log(S0 / K) + (r - q ) * T) / (sigma * sqrt(T))-sigma*sqrt(T)/ 2
    BS_Call = S0 * exp(-q * T)* norm.cdf(x=d1, loc=0, scale=1)\
    -K * exp(-r * T) * norm.cdf(x=d2, loc=0, scale=1)
    return BS_Call

#プット・オプションの価格関数を定義
def BS_Put(S0, sigma ,r,q,T,K):
    d1 = (log(S0 / K) + (r - q + sigma**2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    BS_Put = K * exp(-r * T) * norm.cdf(x=-d2, loc=0, scale=1)\
    -S0 * exp(-q * T) * norm.cdf(x=-d1, loc=0, scale=1)
    return BS_Put

#インプット
S0=100
sigma=30/100
r=5/100
q=0/100
T=1
K=100

#計算結果
BS_Call(S0, sigma ,r,q,T,K)
BS_Put(S0, sigma ,r,q,T,K)

#プット・コール・パリティの確認
BS_Call(S0, sigma ,r,q,T,K)+K*exp(-r*T)\
    -BS_Put(S0, sigma ,r,q,T,K)-S0*exp(-q*T)
