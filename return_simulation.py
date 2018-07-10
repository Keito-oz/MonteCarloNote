from scipy.stats import norm  # 正規分布
from math import log #対数関数
def return_simulation(mu,sigma,t,r_target):
    x=(log(1+r_target)-(mu-sigma**2/2)*t)/sigma/t**(1/2)
    prob=1-norm.cdf(x, loc=0, scale=1)
    return prob

#以下手計算の残骸
# return_simulation(mu=5/100,sigma=22/100,t=30,r_target=0/100)
#
# mu=5/100
# sigma=20/100
# r_target=20/100
# t=10
# x=(log(1+r_target)-(mu-sigma**2/2)*t)/sigma/t**(1/2)
# prob=norm.cdf(x, loc=0, scale=1)
# print(prob)
