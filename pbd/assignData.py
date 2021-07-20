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

        print("Current Particle Position : ", self.CurrPos)
        print("Current Particle Velocity : ", self.CurrVel)

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
        ## 01. Parsing Analysis Parameters    
        for ii,line in enumerate(lines) :
            try : 
                varNameAndValue = line.split('!')[0]
                varName = varNameAndValue.split('=')[0]
                varValue= varNameAndValue.split('=')[1]
                if varName == "DT"                  : self.dt = float(varValue)
                if varName == "DT"                  : self.newDt = float(varValue)
                if varName == "CFL"                 : self.cfl = float(varValue)
                if varName == "SizeOfParticle"      : self.p_Radius = float(varValue)
                if varName == "NumberOfParticles"   : self.p_Number = float(varValue)
            except : 
                print("Check {}-th line in \"{}\" => {}".format(ii, dirInputFile,line))
 
        ## 02. Parsing Particle Properties & Variable
        self.InitPos = np.array([1,2,3])
        self.InitVel = np.array([2,3,4])






class setupAnalysis :
    def __init__(self,dirInputFile): 
        self.simulationData = readInputs(dirInputFile)

    def calculateVariousDt(self,ParticleSize, velocity, CFL):
        self.simulationData.analysisData.newDt = min(self.simulationData.analysisData.CFL * self.simulationData.analysisData.ParticleSize / self.simulationData.particleData.velocity)

    def calculateNextPostion(self):
        self.simulationData.particleData.NextPos= self.simulationData.particleData.CurrPos + self.simulationData.analysisData.newDt * self.simulationData.particleData.CurrVel
        print("Caculated Next Position (dt={}): {}".format(self.simulationData.analysisData.newDt,self.simulationData.particleData.NextPos))
        
    

dirInputFile = '../test.input'
SIMULATION = setupAnalysis(dirInputFile)
SIMULATION.calculateNextPostion()





