import traci
import traci.constants as tc
sumoBinary = "sumo-gui"
sumoCmd = [sumoBinary, "-c", "control.sumocfg"]
traci.start(sumoCmd)
vehID = "vehicle_0"
step = 0
maxspeed = 20
while step < 1000:
    traci.simulationStep()
    step += 1
    print("step", step)
    speed = traci.vehicle.getSpeed(vehID)
    print(speed, traci.vehicle.getAcceleration(vehID))
    if speed <= 0 :
        traci.vehicle.slowDown(vehID, maxspeed, 8.0)
        # traci.vehicle.setSpeed(vehID, speed)
        traci.vehicle.changeLane(vehID, 0, 1.0)
        # traci.vehicle.changeSublane(vehID, -1)
    elif speed >= maxspeed:
        traci.vehicle.slowDown(vehID, 0, 15.0)
        # traci.vehicle.setSpeed(vehID, speed)
        traci.vehicle.changeLane(vehID, 1, 1.0)
        # traci.vehicle.changeSublane(vehID, 1)

traci.close()