import pytube as pt
import os

yt = pt.YouTube('https://www.youtube.com/watch?v=LPwJnL0GEWI ')
#print(yt.title)

vids = yt.streams.all()
for x in vids:
    print(x)

#for v in vids:
 #   print(str(s)+"."+str(v))
  #  s+=1

#print("enter no of videos")
#n=int(input())
#videos = vids[n-1]

s=int(input("enter number"))
vid=vids[s]
dest = os.path.dirname('E:\\projects\\python\\Youtube\\')
vid.download(dest)




