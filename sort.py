
def sort(list,n):
  l=0
  u=len(list)
  for i in range(0,len(list)):
        mid=(l+u)//2
        if len(mid)==n:
          return True
        else:
            if len(mid)>n:
              l=mid
            else:
              u=mid
list=[2,4,6,8,20,13]
n=20
if sort(list,n):
  print("FOUND IT")
 else:
  print("NOT FOUND")
