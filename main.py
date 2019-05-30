import pygame
import numpy as np
import math

key_to_function = {
    pygame.K_LEFT: (lambda x: x.translateAll('LEFT',10)),
    pygame.K_RIGHT:(lambda x: x.translateAll('RIGHT',10)),
    pygame.K_DOWN: (lambda x: x.translateAll('BACKWARD',10)),
    pygame.K_UP:   (lambda x: x.translateAll('FORWARD',10)),
    pygame.K_1:    (lambda x: x.translateAll('UP',10)),
    pygame.K_2:    (lambda x: x.translateAll('DOWN',10))
}
   
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

    def transform(self, matrix):
        self.points = np.dot(self.points, matrix)

    def translationMatrix(self, dx=0, dy=0, dz=0):

        matrix = np.array([[1,0,0,0],
                           [0,1,0,0],
                           [0,0,1,0],
                           [dx,dy,dz,1]])
        return matrix

    #calculo do ef e eg para mover para frente e assim por diante
    def unitVectorFront(self):

        EF = self.points[5]-self.points[4]
        EG = self.points[6]-self.points[4]
        orthognal = np.array([(EF[1]*EG[2]-EG[1]*EF[2]), (EG[0]*EF[2]-EF[0]*EG[2]), (EF[0]*EG[1]-EG[0]*EF[1])])
        unit = -orthognal/math.sqrt((orthognal[0]**2)+(orthognal[1]**2)+(orthognal[2]**2))
        
        return unit

    def unitVectorBack(self):
       
        AC = self.points[2]-self.points[0]
        AB = self.points[1]-self.points[0]
        orthognal = np.array([(AC[1]*AB[2]-AB[1]*AC[2]), (AB[0]*AC[2]-AC[0]*AB[2]), (AC[0]*AB[1]-AB[0]*AC[1])])
        unit = -orthognal/math.sqrt((orthognal[0]**2)+(orthognal[1]**2)+(orthognal[2]**2))
        return unit

    def unitVectorLeft(self):
       
        AB = self.points[1]-self.points[0]
        AE = self.points[4]-self.points[0]
        orthognal = np.array([(AB[1]*AE[2]-AE[1]*AB[2]), (AE[0]*AB[2]-AB[0]*AE[2]), (AB[0]*AE[1]-AE[0]*AB[1])])
        unit = -orthognal/math.sqrt((orthognal[0]**2)+(orthognal[1]**2)+(orthognal[2]**2))
        return unit

    def unitVectorRight(self):
        
        CG = self.points[6]-self.points[2]
        
        CD = self.points[3]-self.points[2]
        
        orthognal = np.array([(CG[1]*CD[2]-CD[1]*CG[2]), (CD[0]*CG[2]-CG[0]*CD[2]), (CG[0]*CD[1]-CD[0]*CG[1])])
        
        unit = -orthognal/math.sqrt((orthognal[0]**2)+(orthognal[1]**2)+(orthognal[2]**2))
        print(unit)
        return unit

    def unitVectorTop(self):
       
        BD = self.points[3]-self.points[1]
        BF = self.points[5]-self.points[1]
        orthognal = np.array([(BD[1]*BF[2]-BF[1]*BD[2]), (BF[0]*BD[2]-BD[0]*BF[2]), (BD[0]*BF[1]-BF[0]*BD[1])])
        unit = -orthognal/math.sqrt((orthognal[0]**2)+(orthognal[1]**2)+(orthognal[2]**2))
        return unit

    def unitVectorBottom(self):
        
        AE = self.points[4]-self.points[0]
        AC = self.points[2]-self.points[0]
        orthognal = np.array([(AE[1]*AC[2]-AC[1]*AE[2]), (AC[0]*AE[2]-AE[0]*AC[2]), (AE[0]*AC[1]-AC[0]*AE[1])])
        unit = -orthognal/math.sqrt((orthognal[0]**2)+(orthognal[1]**2)+(orthognal[2]**2))
        return unit


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
        self.nodeRadius = 4
        

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


    def translateAll(self, direction, increment):

        for wireframe in self.wireframes.values():
            if direction == 'FORWARD':
                vector = wireframe.unitVectorFront()*increment
            if direction == 'BACKWARD':
                vector = wireframe.unitVectorBack()*increment
            if direction == 'UP':
                vector = wireframe.unitVectorTop()*increment
            if direction == 'DOWN':
                vector = wireframe.unitVectorBottom()*increment
            if direction == 'RIGHT':
                vector = wireframe.unitVectorRight()*increment
            if direction == 'LEFT':
                vector = wireframe.unitVectorLeft()*increment
            matrix = wireframe.translationMatrix(*vector)
            wireframe.transform(matrix)

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
  