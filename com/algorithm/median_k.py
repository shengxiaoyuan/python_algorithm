from com.algorithm.quick_sort import quickSort


def midk(a,b,k):
    la=len(a)
    lb=len(b)
    init_k=k
    midk=init_k//2
    mina=0
    minb=0
    maxa=la-1
    maxb=lb-1
    while init_k>1:
        if mina <= maxa:
            mida=maxa if mina+midk-1 >= maxa else mina+midk-1
        if minb <=maxb:
            midb=maxb if minb+midk-1 >= maxb else minb+midk-1
        #两个数组都存在
        if mina<=maxa and minb<= maxb :
            if  a[mida] <=b[midb]:
                init_k=init_k-(mida-mina+1)
                mina=mida+1
                midk=init_k//2
            else:
                init_k=init_k-(midb-minb+1)
                minb+=midb+1
                midk=init_k//2
        else:
            #only  a remain
            if mina <=maxa:
                return a[mina+init_k-1]
            #only b  remain
            if minb <= maxb:
                return b[minb+init_k-1]
    #两个数组都存在
    if (len(a)+len(b))%2 ==0:
        if a[mina]< b[minb]:
            return (a[mina],b[minb])
        else:
            return (b[minb],a[mina])
    else:
        return a[mina] if a[mina] < b[minb] else b[minb]

if __name__ == '__main__':
    a1=[1,4,5,7,9,14]
    a2=[10,13,15,17,20,23,25,28,55,67]
    #
    a3=a1+a2
    mid=0
    if len(a3)%2==0:
        mid=int(len(a3)/2)
    else:
        mid=int(len(a3)/2)+1
    print(midk(a1,a2,mid))
    a3=a1+a2
    print(len(a3))
    quickSort(a3,0,len(a3)-1)
    print(a3)