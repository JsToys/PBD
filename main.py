import pbd


dirInputFile = './test.input'
SIMULATION = pbd.assignData.setupSimulation(dirInputFile)
SIMULATION.calculateVariousDt()
SIMULATION.calculateNextPostion()