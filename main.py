# python3

def parallel_processing(n, m, data):
    output = []
    time = []
    lastingtime =[]
    flag =[]
    for i in range(n):
      flag.append(0)
      time.append(0)
      lastingtime.append(0)
      j=0
    for i in range (m):
      while True:
        if(flag[j]==0):
          flag[j]=data[i]
          #print (j,"-",i,"-",time[j])
          output.append((j,lastingtime[j]))
          break;
        else:
          if time[j]==flag[j]:
            #print ("a",j,"-",i,"-",time[j])
            flag[j]=0
            time[j]=0
          else:
            time[j]=time[j]+1
            lastingtime[j]=lastingtime[j]+1
            #print ("b",j,"-",i,"-",time[j])
            if j==n-1:
              j=0
            else:
              j=j+1
          
        

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    mn = list(map(int, input().split()))
    # n - thread count 
    # m - job count
    n = mn[0]
    m = mn[1]

  

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i, j in result:
        print(i, j)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()

