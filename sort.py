
def sort(list,n):
  l=0
  u=len(list)
  for i in range(0,len(list)):
        m=(l+u)//2
        if len(m)==n:
          return True
        else:
            if len(m)>n:
              l=m
            else:
              u=m
list=[2,4,6,8,20,13]
n=20
if sort(list,n):
  print("FOUND IT")
 else:
  print("NOT FOUND")
