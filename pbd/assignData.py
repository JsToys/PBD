'''
 python3.8
 numpy 1.20.3
'''
import numpy as np




class analysisSetData :

    def __init__(self, dt, cfl, p_Radius, p_Number) : 
        #Analysis Info
        self.dt = dt 
        self.cfl = cfl 
        self.newDt = dt
        #Particle Info
        self.p_Radius = p_Radius
        self.p_Number = p_Number

class particleSetData :

    def __init__(self, InitPos, InitVel):
        # 파티클 개수 확인 => 메모리할당 가능?
        # np.array형식 확인

        self.CurrPos = InitPos
        self.CurrVel = InitVel
        self.IntrPos = InitPos
        self.IntrVel = InitVel
        self.NextPos = InitPos
        self.NextVel = InitVel

        print("Current Particle Position : \n{}\n\n".format(self.CurrPos))
        print("Current Particle Velocity : \n{}\n\n".format(self.CurrVel))





class readInputs :

    def __init__(self,dirInputFile) : # self, inputFileName
        self.parsingInputFile(dirInputFile)
        self.analysisData = analysisSetData(dt                  = self.dt, 
                                            cfl                 = self.cfl,
                                            p_Radius            = self.p_Radius,
                                            p_Number            = self.p_Number)
        self.particleData = particleSetData(InitPos    = self.InitPos,
                                            InitVel    = self.InitVel)

    def parsingInputFile(self,dirInputFile):
        f = open(dirInputFile,'r')
        lines = f.readlines()
        for ii,line in enumerate(lines) :
            try : 
                varNameAndValue = line.split('!')[0]
                varName = varNameAndValue.split('=')[0]
                varValue= varNameAndValue.split('=')[1]
                
                ## 01. Parsing Analysis Parameters    
                if varName == "DT"                  : self.dt = float(varValue)
                if varName == "DT"                  : self.newDt = float(varValue)
                if varName == "CFL"                 : self.cfl = float(varValue)
                if varName == "SizeOfParticle"      : self.p_Radius = float(varValue)
                
                ## 02. Parsing Particle Properties & Variable     
                if varName == "initialPosition_CenterX" : self.init_PosCenX = float(varValue)
                if varName == "initialPosition_CenterY" : self.init_PosCenY = float(varValue)
                if varName == "initialPosition_SizeX" : self.init_PosSizX = float(varValue)
                if varName == "initialPosition_SizeY" : self.init_PosSizY = float(varValue)
                if varName == "initialVelocity_X" : self.init_VelX = float(varValue)
                if varName == "initialVelocity_Y" : self.init_VelY = float(varValue)
            except : 
                print("Check {}-th line in \"{}\" => {}".format(ii, dirInputFile,line))
        self.arrangeInitialParticles()
        # self.InitPos = np.array([1,2,3])
        # self.InitVel = np.array([2,3,4])
        self.p_Number = len(self.InitPos[0])

    def arrangeInitialParticles(self):
        self.InitPosCen = [self.init_PosCenX, self.init_PosCenY]
        self.InitPosSiz = [self.init_PosSizX, self.init_PosSizY]
        x = np.arange(-self.InitPosSiz[0]/2+self.p_Radius,self.InitPosSiz[0]/2-self.p_Radius,2*self.p_Radius) + self.InitPosCen[0]
        y = np.arange(-self.InitPosSiz[1]/2+self.p_Radius,self.InitPosSiz[1]/2-self.p_Radius,2*self.p_Radius) + self.InitPosCen[1]
        X,Y = np.meshgrid(x,y)
        self.InitPos = np.array([X.flatten(), Y.flatten()])
        self.InitVel = np.array([X.flatten()*0.0+self.init_VelX, Y.flatten()*0.0+self.init_VelY])








class setupSimulation :
    def __init__(self,dirInputFile): 
        self.simulationData = readInputs(dirInputFile)

    def calculateVariousDt(self):
        velmax = max((self.simulationData.particleData.CurrVel[0]**2 + self.simulationData.particleData.CurrVel[1]**2)**0.5)
        cfl = self.simulationData.analysisData.cfl
        p_Radius = self.simulationData.analysisData.p_Radius
        self.simulationData.analysisData.newDt = cfl * p_Radius / velmax

    def calculateNextPostion(self):
        self.simulationData.particleData.NextPos= self.simulationData.particleData.CurrPos + self.simulationData.analysisData.newDt * self.simulationData.particleData.CurrVel
        print("Caculated Next Position (dt={}, newDt={}): \n{}\n\n".format(self.simulationData.analysisData.dt,self.simulationData.analysisData.newDt,self.simulationData.particleData.NextPos))
        
    

dirInputFile = '../test.input'
SIMULATION = setupSimulation(dirInputFile)
SIMULATION.calculateVariousDt()
SIMULATION.calculateNextPostion()





