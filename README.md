## Morse service

At morse service, we set up a Flask server, listening at port 8000. 
Service allowing you:
* Send messages for encryption, and play them
* Modify different sounds
* Get log of successful plays.


### Installation
* git clone https://github.com/Arielegend/Morse.git
* cd Morse
* python3 -m venv venv
* source venv/bin/activate
* pip install .

#### _Once pip finished_

* (at venv) run main.py file
* Flask server should open at a local host, port 8000. 
### Usage
<p>Morse service has 3 endpoint</p>

* POST  /morse
    * Params -
      * msg: message to encrypt and play
    
* POST /setup
    * Params - 
      * sound: Integer representing different set of sounds to play code with.
    
* GET /log
    * Params - 
        * n: Integer representing the n'th last successfully played codes to receive as a response.
    
### Examples 
#### Using Postman
* POST /morse
    * http://127.0.0.1:8000/internal/morse
    * {"msg":"SoS"}
 ![Alt text](pics/post_msg.png?raw=true "Title")
  

* POST /setup
    * http://127.0.0.1:8000/internal/setup
    * {"sound":5}
 ![Alt text](pics/post_sound.png?raw=true "Title")
  

* GET /log
    * http://127.0.0.1:8000/internal/log?n=1
 ![Alt text](pics/get_log.png?raw=true "Title")
  
