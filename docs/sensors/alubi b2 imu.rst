Alubi B2 9-Axis Inertial Measurement Unit (IMU)
===============================================

Setup
-----

RaspberryPi Zero Setup
^^^^^^^^^^^^^^^^^^^^^^

RaspberryPi Zero is used to read real-time data from IMUs via Bluetooth communication and pass them to Teensy via serial communication.

The default Wi-Fi name produced by RaspberryPi Zero is ``RaspberryPi AP02`` and the default password is ``raspberrypi``. To customize both settings, perform the following steps:

* Connect to RaspberryPi Zero using the default Wi-Fi name and password on a PC.
* Update the password and Wi-Fi name in the following python script and execute the python script on this PC.
  
  .. code-block:: python

    import requests
    import base64
    import json
    import time


    def put_wireless(ssid, passwd):
        '''
        Both ssid and passwd are of string type.
        '''
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        d = {
            "ssid": ssid,
            "passwd": passwd
        }
        url = 'http://192.168.12.1:8080/wireless'
        res = requests.put(url, data=json.dumps(d), headers=headers)
        print(res)

    put_wireless("desired_wifi_name","desired_wifi_password" )

  .. note:: 

    If successful, you should see <Response [200]> in the python terminal output.

* On the same PC, open http://192.168.12.1:8080/ in the browser, click “Shutdown”. Then disconnect the power to RaspberryPi Zero and reconnect the power to reboot it. Now you should be able to connect to it using the new Wi-Fi name and password.