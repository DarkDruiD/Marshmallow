import uav_pb2

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print "Connected"


def on_msg(client, userdata, msg):
    drn_pkg = uav_pb2.DronPackage()
    drn_pkg.ParseFromString(str(msg.payload))

    print "GPS:    {} {}".format(drn_pkg.gps.longitude,
                                 drn_pkg.gps.latitude)

    print "Height: {} {}".format(drn_pkg.height.height)

    print "Gyro:   {} {}".format(drn_pkg.gyro.pitch,
                                 drn_pkg.gyro.roll)

    print "Accel:  {} {}".format(drn_pkg.accel.x,
                                 drn_pkg.accel.y,
                                 drn_pkg.accel.z)

    print "-------------------------------------------------------------------"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.onmessage = on_msg

mqttc.connect("127.0.0.1", 1883, 60)

mqttc.loop_forever()
