# draw_map2d
make a map(.pgm and .yaml)  for map_server(ros package) from a .txt file 

USAGE:
python3 draw_map2d.py

NOTICE the format of vio_map.map
EXAMPLE:
# vertice id x y z
vertice 1 0.0 0.0 0.0
vertice 2 5.0 0.0 0.0
vertice 3 5.0 5.0 0.0
vertice 4 0.0 5.0 0.0
vertice 5 0.0 -1.0 0.0
vertice 6 1.0 -1.0 0.0
vertice 7 1.0 0.0 0.0

# line id p0 p1
line 1 1 5
line 2 5 6
line 3 6 7
line 4 7 2
line 5 2 3
line 6 3 4
line 7 4 1
