import json
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv
from webhook import send_msg_discord

load_dotenv()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(os.getenv('MQTT_SUBSCRIBE'))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    data = json.loads( msg.payload.decode( "utf-8" ) )
    decoded = data[ "uplink_message" ][ "decoded_payload" ]
    send_msg_discord( msg.topic, str( decoded ) )
# Création d'un client MQTT
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# Configuration du nom d'utilisateur et du mot de passe
mqttc.username_pw_set(os.getenv('MQTT_USER'), os.getenv('MQTT_PASSWORD'))
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(os.getenv('MQTT_HOST'), 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()