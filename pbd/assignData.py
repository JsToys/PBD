'''
 python3.8
 numpy 1.20.3
'''
import numpy as np
from pbd.dataStruct import *
# Read Inputs, and Define data in class of analysisSetData/particleSetData
#
class readInputs :

    def __init__(self,dirInputFile) : # self, inputFileName
        self.parsingInputFile(dirInputFile)
        self.arrangeInitialParticles() # Assign Initial Particles.
        self.analysisData = analysisSetData(dt                  = self.dt, 
                                            cfl                 = self.cfl,
                                            p_Radius            = self.p_Radius,
                                            p_Number            = len(self.InitPos[0]),
                                            BoxMin              = self.analysisBoxMin,
                                            BoxMax              = self.analysisBoxMax)
 
        self.particleData = particleSetData(InitPos             = self.InitPos,
                                            InitVel             = self.InitVel)

    def parsingInputFile(self,dirInputFile):

        self.analysisBoxMin = Vec2(0.0, 0.0)
        self.analysisBoxMax = Vec2(0.0, 0.0)

        f = open(dirInputFile,'r')
        lines = f.readlines()
        for ii,line in enumerate(lines) :
            try : 
                varNameAndValue = line.split('!')[0]
                varName         = varNameAndValue.split('=')[0]
                varValue        = varNameAndValue.split('=')[1]
                
                ## 01. Parsing Analysis Parameters    
                if varName == "DT"                  : self.dt = float(varValue)
                if varName == "DT"                  : self.newDt = float(varValue)
                if varName == "CFL"                 : self.cfl = float(varValue)
                if varName == "SizeOfParticle"      : self.p_Radius = float(varValue)
                if varName == "AnalysisBox_Xmin"    : self.analysisBoxMin.x = float(varValue)
                if varName == "AnalysisBox_Xmax"    : self.analysisBoxMax.x = float(varValue)
                if varName == "AnalysisBox_Ymin"    : self.analysisBoxMin.y = float(varValue)
                if varName == "AnalysisBox_Ymax"    : self.analysisBoxMax.y = float(varValue)
                
                ## 02. Parsing Particle Properties & Variable     
                if varName == "initialPosition_CenterX" : self.init_PosCenX = float(varValue)
                if varName == "initialPosition_CenterY" : self.init_PosCenY = float(varValue)
                if varName == "initialPosition_SizeX" : self.init_PosSizX = float(varValue)
                if varName == "initialPosition_SizeY" : self.init_PosSizY = float(varValue)
                if varName == "initialVelocity_X" : self.init_VelX = float(varValue)
                if varName == "initialVelocity_Y" : self.init_VelY = float(varValue)
            except : 
                print("Check {}-th line in \"{}\" => {}".format(ii, dirInputFile,line))


    def arrangeInitialParticles(self):
        self.InitPosCen = [self.init_PosCenX, self.init_PosCenY]
        self.InitPosSiz = [self.init_PosSizX, self.init_PosSizY]
        x = np.arange(-self.InitPosSiz[0]/2+self.p_Radius,self.InitPosSiz[0]/2-self.p_Radius,2*self.p_Radius) + self.InitPosCen[0]
        y = np.arange(-self.InitPosSiz[1]/2+self.p_Radius,self.InitPosSiz[1]/2-self.p_Radius,2*self.p_Radius) + self.InitPosCen[1]
        X,Y = np.meshgrid(x,y)
        self.InitPos = np.array([X.flatten(), Y.flatten()])
        self.InitVel = np.array([X.flatten()*0.0+self.init_VelX, Y.flatten()*0.0+self.init_VelY])


# Main Class : Computation Functions
#
class setupSimulation :
    def __init__(self,dirInputFile): 
        self.simulationData = readInputs(dirInputFile) # 

    def calculateVariousDt(self):
        velmax = max((self.simulationData.particleData.CurrVel[0]**2 + self.simulationData.particleData.CurrVel[1]**2)**0.5)
        cfl = self.simulationData.analysisData.cfl
        p_Radius = self.simulationData.analysisData.p_Radius
        self.simulationData.analysisData.newDt = cfl * p_Radius / velmax
    def calculateIntermediateVelocity(self):
        return
    def calculateNextPostion(self):
        self.simulationData.particleData.NextPos= self.simulationData.particleData.CurrPos + self.simulationData.analysisData.newDt * self.simulationData.particleData.CurrVel
        print("Caculated Next Position (dt={}, newDt={}): \n{}\n\n".format(self.simulationData.analysisData.dt,self.simulationData.analysisData.newDt,self.simulationData.particleData.NextPos))
        
        
    






