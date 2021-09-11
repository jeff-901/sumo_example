import traci
import traci.constants as tc
import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
sys.path.append(os.path.join('c:', os.sep, 'whatever', 'path', 'to', 'sumo', 'tools'))

sumoBinary = "sumo-gui"
sumoCmd = [sumoBinary, "-c", "play_ground.sumocfg"]
traci.start(sumoCmd)
vehID = "vehicle_1"
step = 0
maxspeed = 10
while step < 1000:
    traci.simulationStep()
    if traci.inductionloop.getLastStepVehicleNumber("induction0") > 0:
       traci.trafficlight.setRedYellowGreenState("gneJ9", "GrGr")
    step += 1
    # print("step", step)
    # speed = traci.vehicle.getSpeed(vehID)
    # print(speed, traci.vehicle.getAcceleration(vehID))
    # if speed <= 0 :
    #     traci.vehicle.slowDown(vehID, maxspeed, 8.0)
    #     # traci.vehicle.setSpeed(vehID, speed)
    #     traci.vehicle.changeLane(vehID, 0, 1.0)
    #     # traci.vehicle.changeSublane(vehID, -1)
    # elif speed >= maxspeed:
    #     traci.vehicle.slowDown(vehID, 0, 15.0)
    #     # traci.vehicle.setSpeed(vehID, speed)
    #     traci.vehicle.changeLane(vehID, 1, 1.0)
    #     # traci.vehicle.changeSublane(vehID, 1)
traci.close()