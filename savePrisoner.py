def fun(n,m,s):
     start=s-1
     if n<m:
          m = m%n
     no = s+m-1
     if no > n:
          no=no-n
     elif no < 1:
          no=n
     return no






if __name__ == "__main__":
    print(fun(3 ,7 ,3
))