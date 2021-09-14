from dataclasses import dataclass

@dataclass
class Vec2 :
    x: float = None
    y: float = None

@dataclass
class Vec3 :
    x: float = None
    y: float = None
    z: float = None

# Define Analysis Data.
#
class analysisSetData :

    def __init__(self, dt, cfl, p_Radius, p_Number, BoxMin, BoxMax) : 
        #Analysis Info
        self.dt = dt 
        self.cfl = cfl 
        self.newDt = dt
        self.BoxMin = BoxMin
        self.BoxMax = BoxMax
        #Particle Info
        self.p_Radius = p_Radius
        self.p_Number = p_Number

# Define Particle Data.
#
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

        print("Initialized Particles.")
        print("Current Particle Position : \n{}".format(self.CurrPos))
        print("Current Particle Velocity : \n{}\n".format(self.CurrVel))