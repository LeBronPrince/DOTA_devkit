import shapely.geometry as shgeo

a = [(1,2),(1,4),(3,4),(3,2)]
b = [(2,2),(2,4),(4,4),(4,2)]

a = shgeo.Polygon(a)
b = shgeo.Polygon(b)
c = a.intersection(b)
iou = c.area/a.area
print(iou)
c = shgeo.polygon.orient(c, sign=1)
out_poly = list(c.exterior.coords)
print(out_poly)
