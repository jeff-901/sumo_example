sumoBinary = "sumo-gui"
sumoCmd = [sumoBinary, "-c", "my.sumocfg"]
import traci
import traci.constants as tc
traci.start(sumoCmd)
vehID = "vehicle_0"
traci.vehicle.subscribe(vehID, (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
print(traci.vehicle.getSubscriptionResults(vehID))
step = 0
while step < 1000:
    traci.simulationStep()
    print("step", step)
#    if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
    #    traci.trafficlight.setRedYellowGreenState("0", "GrGr")
    print(traci.vehicle.getSubscriptionResults(vehID))
    print(traci.vehicle.getSpeed(vehID), traci.vehicle.getAcceleration(vehID))
    print(traci.vehicle.getLaneChangeStatePretty(vehID, 0), traci.vehicle.getLaneChangeStatePretty(vehID, 1))
    step += 1

traci.close()