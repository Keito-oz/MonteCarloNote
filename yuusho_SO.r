market.conition<-function(S,K,r,sigma,T,n,M,Q)
{
  P<-0    #SOの価格
  L<-0    #利得が生徒なるパスの数
  dt<-T/M #期間TをM分割
  for(i in 1:n)#nはシミュレーション回数
  {
    St<-S   #時点tの株価、初期値はS
    Smod<-S #満期までのStがノックアウト価格Qを下回ったら0に修正するための変数
    x<-rnorm(M,0,1)#M個の標準正規乱数
    for(j in 1:M)#Mは時点の数
    {
      St<-ST*exp((r-0.5*sigma^2)*dt+sigma*sqrt(dt)*x[j])
      #1時点前の株価にランダムウォークのモデルを当てはめてStを更新する
      if(Smod==0)
      {
        Smod<-0
        #下記のノックアウト判定の結果、一度でもSmodが0になったら、
        #その後永久に０とするための式
      }else if(St<Q)
      {
        Smod<-0
        #ノックアウト判定、StがQを下回ったらSmodを0に
      }else
      {
        Smod<-St
        #Stがノックアウト価格Q以上であればSmodは株価Stと同額
      }
    }
    P<-P+max(Smod-K,0)
    #満期のSmodはノックアウトされたら0、
    #されなければ満期におけるSt
    #このSmodを用いてオプション価格Pに各シミュレーション結果で算出された
    #満期の利得を順に合計
    
    if(Smod-K>0)
    {
      L<-L+1
      #満期のオプションの利得が正であるパスが発生するたび、
      #カウント変数Lをインクリメント
    }
  }
  P<-exp(-r*T)*P/n
  #n回実施結果を合計したオプションの利得合計を現在価値に割引き、
  #nで割って平均を出す。
  return(c("株価条件付きオプション価格"=P,"正となるパスの数"=L))
}

market.conition(600,600,0.00275,0.67,7.1,10000,10000,300)
