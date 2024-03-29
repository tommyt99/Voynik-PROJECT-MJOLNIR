import math
import pygame

class buildEnvironment:

    def __init__(self, MapDimensions):
        self.pointCloud=[] #array containing coordinates of sensed objects (walls). Purely just (x,y) information.
        self.externalMap=pygame.image.load('floorplan.png')
        self.maph, self.mapw = MapDimensions
        self.MapWindowName = 'LiDAR Simulation'
        pygame.display.set_caption(self.MapWindowName)
        self.map= pygame.display.set_mode((self.mapw, self.maph)) #opens the pop-up window box
        self.map.blit(self.externalMap, (0,0)) #overlays floor plan ontop of blank canvas
        
        #Colors
        self.black = (0,0,0)
        self.grey = (70,70,70)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.red =(255,0,0)
        self.white = (255,255,255)


    #Key Concept: Helper Method that converts raw distance and angle data from sensor.py to cartesian coordinates
    #AD2pos means Angle, Distance to Position?

    #Uses Distance and Angle from data[] in sensors.sensesObstacles() to obtain cartesian coordinates of walls for point cloud
    def AD2pos(self, distance, angle, robotPosition):
        x = robotPosition[0] + distance * math.cos(angle)
        y = robotPosition[1] + distance * math.sin(angle) 
        return ( int(x), int(y) ) #returns cartesian coordinates of walls. 

    def dataStorage(self,data): # data = [Distance, Angle, (x,y)] --> This is the input. Storing data in point cloud. 
        print(len(self.pointCloud))
        if data != False: #if data exists, then start for loop
            for element in data:
                point = self.AD2pos(element[0],element[1],element[2]) #Input: data = [Distance, Angle, (x,y)]. Output: (x,y) coordinate of objects/walls.
                if point not in self.pointCloud: #Note: Point cloud should ONLY be the WALLS (x,y). If the wall has not already been sensed, then add to pointcloud.
                    self.pointCloud.append(point) #[(x1,y1), (x2,y2), (x3,y3)]






    def show_sensorData(self):
        self.infomap=self.map.copy() #information map DISPLAYS the coordinates of walls thru changing the colors of pixels in the pop-up window box. 
        for point in self.pointCloud:
            self.infomap.set_at( (int(point[0]), int(point[1])), (255,0,0) ) #show each object coordinate in the recorded point cloud as red dot in the pop-up box.


