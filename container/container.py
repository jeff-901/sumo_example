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
sumoCmd = [sumoBinary, "-c", "container.sumocfg"]
traci.start(sumoCmd)
vehID = "vehicle_0"
junctionID = "gneJ9"
step = 0
maxspeed = 10
# Subscriptions
# traci.vehicle.subscribe(vehID, (tc.VAR_ROAD_ID, tc.VAR_LANEPOSITION))
# print(traci.vehicle.getSubscriptionResults(vehID))
# Context Subscriptions
traci.junction.subscribeContext(junctionID, tc.CMD_GET_VEHICLE_VARIABLE, 42, [tc.VAR_SPEED, tc.VAR_WAITING_TIME])
print(traci.junction.getContextSubscriptionResults(junctionID))

while step < 1000:
    # Subscriptions
    # print("step", step)
    # traci.simulationStep()
    # print(traci.vehicle.getSubscriptionResults(vehID))
    # Context Subscriptions
    print("step", step)
    traci.simulationStep()
    print(traci.junction.getContextSubscriptionResults(junctionID))
    step += 1
traci.close()