import urllib.request
import io
import random
from PIL import Image
import time
import sys

myt=time.perf_counter()
#print(sys.argv[2])
#URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
#URL='https://gabrielnapoleon.files.wordpress.com/2013/03/groundhog.jpg?w=584'
URL=sys.argv[1]
f = io.BytesIO(urllib.request.urlopen(URL).read()) # Download the picture at the url as a file object
img = Image.open(f) # You can also use this on a local file; just put the local filename in quotes in place of f.
#img.show() # Send the image to your OS to be displayed as a temporary file
#print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
#print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].
#pix[2,5] = (255, 255, 255) # Set the pixel to white. Note this is called on “pix”, but it modifies “img”.


width,height=img.size
K=int(sys.argv[2])
newimg = Image.new("RGB", (width, height), 0)
newpix=newimg.load()
# #27 color naive quantization
# for w in range(width):
#     for h in range(height):
#         pr,pg,pb= pix[w,h]
#         if pr<255//K:
#             pr=0
#         elif pr<255*2//K:
#             pr=127
#         else:
#             pr=255
#         if pb<255//K:
#             pb=0
#         elif pb<255*2//K:
#             pb=127
#         else:
#             pb=255
#         if pg<255//K:
#             pg=0
#         elif pg<255*2//K:
#             pg=127
#         else:
#             pg=255
#         newpix[w,h]=pr,pg,pb
# newimg.show()
#
# K=2
# #8 color naive quantization
# for w in range(width):
#     for h in range(height):
#         pr,pg,pb= pix[w,h]
#         if pr<255//K:
#             pr=0
#         else:
#             pr=255
#         if pb<255//K:
#             pb=0
#         else:
#             pb=255
#         if pg<255//K:
#             pg=0
#         else:
#             pg=255
#         newpix[w,h]=pr,pg,pb
# newimg.show() # Now, you should see a single white pixel near the upper left corner


def distance(tuple1,tuple2):
    r1,g1,b1=tuple1
    r2,g2,b2=tuple2
    dist=(r2-r1)**2+(g2-g1)**2+(b2-b1)**2
    return dist

elements={}
pixels={}
totperel={}
while len(elements.keys())<K:
    w=random.randint(0,width-1)
    h=random.randint(0,height-1)
    elements[pix[w,h]]=[]
    totperel[pix[w,h]]=(0,0,0)

for w in range(width):
    for h in range(height):
        pixel=pix[w,h]
        pixels[pixel]=pixels.get(pixel,[])+[(w,h)]

while len(elements)>0:
    for pixel in pixels.keys():
        distances = [distance(pixel, elem) for elem in elements.keys()]
        element = list(elements.keys())[distances.index(min(distances))]
        for tup in pixels[pixel]:
            tempw,temph=tup
            newpix[tempw,temph]=element
        l = len(pixels[pixel])
        elements[element]=elements.get(element,[])+[pixel]*l
        a,b,c=totperel[element]
        d,e,t=pixel
        a+=l*d
        b+=l*e
        c+=l*t
        totperel[element]=(a,b,c)
    newelements = {}
    newtotperel={}
    for element in elements.keys():
        a,b,c=totperel[element]
        l=len(elements[element])
        newelement=(a//l,b//l,c//l)
        newelements[newelement]=[]
        newtotperel[newelement]=(0,0,0)
    l1, l2 = list(elements.keys()), list(newelements.keys())
    # total=0
    # for i in range(K):
    #     total = total + abs(sum(list(l1[i])) - sum(list(l2[i])))
    # #elements = {}
    # print(total)
    l1.sort()
    l2.sort()
    if l1==l2:
        elements={}
    else:
        elements = newelements
        totperel=newtotperel
    #newimg.show()



newimg.save("kmeansout.png") # Save the resulting image. Alter your filename as necessary.

print(time.perf_counter()-myt)