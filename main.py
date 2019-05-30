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
    print(cube_points)