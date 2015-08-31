### Setup

First create a virtual environment and activate it:
```sh
$ virtualenv Marshmallow-Env
$ cd Marshmallow-Env
$ source bin/activate
```

Then clone the repository:
```sh
$ git clone https://github.com/DarkDruiD/Marshmallow
$ cd Marshmallow
```

You need to install the dependencies:
```sh
$ pip install -r requirements.txt
$ sudo apt-get install mosquitto
```

## Usage

Run the mosquitto MQTT broker:

```sh
$ mosquitto -v
```

Run the publisher and subscriber in different terminals:

```sh
$ python transmitter.py
$ python receiver.py
```


## Explanations and considerations

* The program consist in a simple script that emulates some drone data like: 
    - GPS
    - Gyroscope
    - Height sensor
    - Accelerometers

* Is important to note that the most challenging part was to avoid the UTF-8 requirements in the MQTT client libraries, this is avoided by encoding in base64 before transmitting the information through MQTT, as shown here:

    ```py
    body = drn_pkg.encode('base64')
    ```
    
    and decoded in a similar fashion by doing:
    
    ```py
    data = base64.b64decode(str(msg.payload))
    ```
