if __name__ == '__main__':
    n = int(input())
    var=""
    if n>=1 and n <= 150:
        for i in range(1,n+1,1):
            var+=str(i)
        print (var)