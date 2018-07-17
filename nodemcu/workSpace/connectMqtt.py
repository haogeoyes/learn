from lib.simple import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

def sub_cb(topic, msg):
    print((topic, msg))
    if msg == 'on':
      Pin(2,Pin.OUT).vaue(0) #亮
    if msg == 'off':
      Pin(2,Pin.OUT).value(1) #灭
      

def fabu():
    c =MQTTClient("umqtt_client", server="192.168.0.107",port=61613,user="admin",password="password")
    #c.set_callback("test")
    
    c.connect()
    c.publish(b"test", b"ip")
    #c.subscribe("test")
    c.disconnect()
    



def dingyue(server="localhost"):
    c =MQTTClient("umqtt_client", server="192.168.0.107",port=61613,user="admin",password="password")
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"test")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()


if __name__ == "__main__":
    
    #fabu()
    dingyue()
