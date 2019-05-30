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

class ProjectionViewer:


    def __init__(self, width, height):
        self.width = width
        self.height = height
        #configuracao padrao para tela
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Trabalho do miguel')
        self.background = (10,10,50)
        self.wireframes = {}
        self.displayPoints = True
        self.displayVertices = True
        self.pointColor = (255,255,255)
        self.verticeColor = (200,200,200)
        

    #Método básico de wireframe
    def addWireframe(self, name, wireframe):


        self.wireframes[name] = wireframe

    #Arquetipo básico da pygame de instancia de tela e controle por i/o
    def run(self):
        

        running = True
        pygame.key.set_repeat(50,50)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_function:
                        key_to_function[event.key](self)

            self.display()
            pygame.display.flip()

    #Desenha o cubo na tela
    def display(self):

        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.displayVertices:
                pygame.draw.aaline(self.screen, (0,255,0), (int(400+(wireframe.points[0][0]-400)*(1-wireframe.points[0][2]/1000)), int(300+(wireframe.points[0][1]-300)*(1-wireframe.points[0][2]/1000))), (int(400+(wireframe.points[1][0]-400)*(1-wireframe.points[1][2]/1000)), int(300+(wireframe.points[1][1]-300)*(1-wireframe.points[1][2]/1000))), 1)
                pygame.draw.aaline(self.screen, (0,255,0), (int(400+(wireframe.points[1][0]-400)*(1-wireframe.points[1][2]/1000)), int(300+(wireframe.points[1][1]-300)*(1-wireframe.points[1][2]/1000))), (int(400+(wireframe.points[3][0]-400)*(1-wireframe.points[3][2]/1000)), int(300+(wireframe.points[3][1]-300)*(1-wireframe.points[3][2]/1000))), 1)
                pygame.draw.aaline(self.screen, (0,255,0), (int(400+(wireframe.points[3][0]-400)*(1-wireframe.points[3][2]/1000)), int(300+(wireframe.points[3][1]-300)*(1-wireframe.points[3][2]/1000))), (int(400+(wireframe.points[2][0]-400)*(1-wireframe.points[2][2]/1000)), int(300+(wireframe.points[2][1]-300)*(1-wireframe.points[2][2]/1000))), 1)
                pygame.draw.aaline(self.screen, (0,255,0), (int(400+(wireframe.points[2][0]-400)*(1-wireframe.points[2][2]/1000)), int(300+(wireframe.points[2][1]-300)*(1-wireframe.points[2][2]/1000))), (int(400+(wireframe.points[0][0]-400)*(1-wireframe.points[0][2]/1000)), int(300+(wireframe.points[0][1]-300)*(1-wireframe.points[0][2]/1000))), 1)
                pygame.draw.aaline(self.screen, (0,0,255), (int(400+(wireframe.points[4][0]-400)*(1-wireframe.points[4][2]/1000)), int(300+(wireframe.points[4][1]-300)*(1-wireframe.points[4][2]/1000))), (int(400+(wireframe.points[5][0]-400)*(1-wireframe.points[5][2]/1000)), int(300+(wireframe.points[5][1]-300)*(1-wireframe.points[5][2]/1000))), 1)
                pygame.draw.aaline(self.screen, (0,0,255), (int(400+(wireframe.points[5][0]-400)*(1-wireframe.points[5][2]/1000)), int(300+(wireframe.points[5][1]-300)*(1-wireframe.points[5][2]/1000))), (int(400+(wireframe.points[7][0]-400)*(1-wireframe.points[7][2]/1000)), int(300+(wireframe.points[7][1]-300)*(1-wireframe.points[7][2]/1000))), 1)
                pygame.draw.aaline(self.screen, (0,0,255), (int(400+(wireframe.points[7][0]-400)*(1-wireframe.points[7][2]/1000)), int(300+(wireframe.points[7][1]-300)*(1-wireframe.points[7][2]/1000))), (int(400+(wireframe.points[6][0]-400)*(1-wireframe.points[6][2]/1000)), int(300+(wireframe.points[6][1]-300)*(1-wireframe.points[6][2]/1000))), 1)
                pygame.draw.aaline(self.screen, (0,0,255), (int(400+(wireframe.points[6][0]-400)*(1-wireframe.points[6][2]/1000)), int(300+(wireframe.points[6][1]-300)*(1-wireframe.points[6][2]/1000))), (int(400+(wireframe.points[4][0]-400)*(1-wireframe.points[4][2]/1000)), int(300+(wireframe.points[4][1]-300)*(1-wireframe.points[4][2]/1000))), 1)
                pygame.draw.aaline(self.screen, self.verticeColor, (int(400+(wireframe.points[0][0]-400)*(1-wireframe.points[0][2]/1000)), int(300+(wireframe.points[0][1]-300)*(1-wireframe.points[0][2]/1000))), (int(400+(wireframe.points[4][0]-400)*(1-wireframe.points[4][2]/1000)), int(300+(wireframe.points[4][1]-300)*(1-wireframe.points[4][2]/1000))), 1)
                pygame.draw.aaline(self.screen, self.verticeColor, (int(400+(wireframe.points[2][0]-400)*(1-wireframe.points[2][2]/1000)), int(300+(wireframe.points[2][1]-300)*(1-wireframe.points[2][2]/1000))), (int(400+(wireframe.points[6][0]-400)*(1-wireframe.points[6][2]/1000)), int(300+(wireframe.points[6][1]-300)*(1-wireframe.points[6][2]/1000))), 1)
                pygame.draw.aaline(self.screen, self.verticeColor, (int(400+(wireframe.points[1][0]-400)*(1-wireframe.points[1][2]/1000)), int(300+(wireframe.points[1][1]-300)*(1-wireframe.points[1][2]/1000))), (int(400+(wireframe.points[5][0]-400)*(1-wireframe.points[5][2]/1000)), int(300+(wireframe.points[5][1]-300)*(1-wireframe.points[5][2]/1000))), 1)
                pygame.draw.aaline(self.screen, self.verticeColor, (int(400+(wireframe.points[3][0]-400)*(1-wireframe.points[3][2]/1000)), int(300+(wireframe.points[3][1]-300)*(1-wireframe.points[3][2]/1000))), (int(400+(wireframe.points[7][0]-400)*(1-wireframe.points[7][2]/1000)), int(300+(wireframe.points[7][1]-300)*(1-wireframe.points[7][2]/1000))), 1)

            if self.displayPoints:
                for point in wireframe.points:
                    pygame.draw.circle(self.screen, self.pointColor, (int(400+(point[0]-400)*(1-point[2]/1000)), int(300+(point[1]-300)*(1-point[2]/1000))), self.nodeRadius, 0)

#Funcao de criar um cubo no centro da tela
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
    pv = ProjectionViewer(resolutionX, resolutionY)
    pv.addWireframe('cube', cube)
    pv.run()
  