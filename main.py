import pygame
import numpy as np
import math



class Wireframe:
    def __init__(self):
        self.points = np.zeros((0, 4))
        self.vertices = []
  
    def addPoints(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.points = np.vstack((self.points, ones_added))
    
    def addVertices(self, verticeList):
        self.vertices += verticeList
    
    def showVertices(self):
        print("\n Vertices:")
        for i, (node1, node2) in enumerate(self.vertices):
            print("   %d: %d -> %d" % (i, node1, node2))

    def showPoints(self):
        print("\n Points:")
        print("  [P]: ( x, y, z)")
        for i, (x, y, z, _) in enumerate(self.points):
            print("   %d: (%d, %d, %d)" % (i, x, y, z))
            

def cubeCreateInCenter(centerX, centerY, centerZ, sideLength):
        
    pos_cord = np.zeros((8,3))
    pos_cord[0] = [centerX-(sideLength/2), centerY-(sideLength/2), centerZ-(sideLength/2)]
    pos_cord[1] = [centerX-(sideLength/2), centerY-(sideLength/2), centerZ+(sideLength/2)]
    pos_cord[2] = [centerX-(sideLength/2), centerY+(sideLength/2), centerZ-(sideLength/2)]
    pos_cord[3] = [centerX-(sideLength/2), centerY+(sideLength/2), centerZ+(sideLength/2)]
    pos_cord[4] = [centerX+(sideLength/2), centerY-(sideLength/2), centerZ-(sideLength/2)]
    pos_cord[5] = [centerX+(sideLength/2), centerY-(sideLength/2), centerZ+(sideLength/2)]
    pos_cord[6] = [centerX+(sideLength/2), centerY+(sideLength/2), centerZ-(sideLength/2)]
    pos_cord[7] = [centerX+(sideLength/2), centerY+(sideLength/2), centerZ+(sideLength/2)]
    return pos_cord

if __name__ == "__main__":
    cubo = Wireframe()
    resolutionX = 1000
    resolutionY = 800
    cube = Wireframe()
    cube_points = cubeCreateInCenter(resolutionX/2,resolutionY/2,0,100)
    cube.addPoints(cube_points)
    cube.addVertices([(n,n+4) for n in range(0,4)])
    cube.addVertices([(n,n+1) for n in range(0,8,2)])
    cube.addVertices([(n,n+2) for n in (0,1,4,5)])
    cube.showPoints()
    cube.showVertices()
    
    print(cube_points)