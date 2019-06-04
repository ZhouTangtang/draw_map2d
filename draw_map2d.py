import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
import yaml

map_filename="./vio_map.map"
pgm_filename="./vio_map.pgm"
yaml_filename="./vio_map.yaml"

vertices={}
lines={}
resolution = 0.05

# read the data
f_map=open(map_filename,'r')
for eachline in f_map.readlines():
    #print(line)
    if eachline[0]=='#' or len(eachline)<2:
        continue
    buf = eachline.split(' ')
    if buf[0] == 'vertice':
        vertices[int(buf[1])]=[float(buf[2]),float(buf[3]),float(buf[4])]
    if buf[0] == 'line':
        lines[int(buf[1])]=[int(buf[2]),int(buf[3])]

for (id,v) in vertices.items():
    print(id,v)
for (id,l) in lines.items():
    print(id,l)

f_map.close()

# create the mat
maxx=-1e9
maxy=-1e9
minx=1e9
miny=1e9

for (id,v) in vertices.items():
    if v[0]>maxx:
        maxx=v[0]
    if v[0]<minx:
        minx=v[0]
    if v[1]>maxy:
        maxy=v[1]
    if v[1]<miny:
        miny=v[1]
maxx+=resolution*100
minx-=resolution*100
maxy+=resolution*100
miny-=resolution*100

mat_out=np.ndarray([int((maxy-miny)/resolution),int((maxx-minx)/resolution),1],dtype=np.uint8)
mat_out[:]=205

for (id,l) in lines.items():
    p1=vertices[l[0]]
    p2=vertices[l[1]]
    x1=int((p1[0]-minx)/resolution)
    y1=int((p1[1]-miny)/resolution)
    x2=int((p2[0]-minx)/resolution)
    y2=int((p2[1]-miny)/resolution)
    cv2.line(mat_out,(x1,y1),(x2,y2),(0,0,0))
mat_out=cv2.flip(mat_out,0)


fs= open(yaml_filename,'w')

yaml.dump({'image':pgm_filename},fs)
yaml.dump({'resolution':resolution},fs)
yaml.dump({'origin':[minx,miny,0]},fs)
yaml.dump({'occupied_thresh':0.65},fs)
yaml.dump({'free_thresh':0.196},fs)
yaml.dump({'negate':0},fs)

fs.close()

