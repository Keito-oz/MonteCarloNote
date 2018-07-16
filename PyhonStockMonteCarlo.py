#必要なモジュールと関数をインポート
import numpy as np
from math import exp,sqrt
import random
import matplotlib.pyplot as plt

#幾何ブラウン運動株価過程を関数として定義
def gBM(S,sigma,mu,t,z):
    gBM= S*exp((mu - sigma**2/2)*t + sigma * sqrt(t) * z)
    return gBM

#パラメタを入力
sigma=0.3
mu=0.05
delta_t=0.01

#各時点の株価を格納する空の配列を用意し、株価の初期値\(S_0\)を設定
process=np.zeros(10000) #10,000ステップ
process[0]=100 #初期値

#標準正規乱数の発生とシミュレーション
for n in range(1,len(process)):
    process[n]=gBM(process[n-1],sigma,mu,delta_t,random.gauss(0,1))

#配列をプロット
plt.plot(process)
plt.show()
