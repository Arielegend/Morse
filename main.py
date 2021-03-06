from flask import Flask, request, make_response, jsonify
import json

from utils.errors import check_input_message, check_input_sound, check_server_is_free, check_input_log
from utils.morse import Morse

INTERNAL = 'internal'

app = Flask(__name__)
morse_object = Morse()  # Constructing a single shared morse object.


@app.route(f'/{INTERNAL}/morse', methods=['POST'])
def playMorse():
    """
    Args:
        1. msg(str) : message to encrypt and play
    Reruns:
        Response to client
    """

    # At entry point, we check if morse_object is currently free
    # Meaning, morse_object "Playing" field, is set to False.
    # If morse_object.Playing is False, we set it to True until we finish playing the incoming message.
    check_server_is_free(morse_object.playing)
    morse_object.setPlay(True)

    # Fetching and validating the message to play.
    data = json.loads(request.data)
    msg = data['msg']
    check_input_message(msg=msg)

    # Once validated, playing the message.
    morse_object.playMessage(msg)

    # Building the response back, announcing good play
    response_body = msg + " had done playing successfully"
    response = {
        'status': 1,  # Status 1 is for good response
        'body': response_body
    }
    # Reset the 'Playing' field of morse_object, allowing new messages to be played.
    morse_object.setPlay(False)
    return make_response(response)


@app.route(f'/{INTERNAL}/setup', methods=['POST'])
def setup():
    """
    Args:
        1. mode(int) : Setting the mode for listening
    Reruns:
    """

    # Fetching and validating the sound input.
    data = json.loads(request.data)
    sound = int(data['sound'])
    check_input_sound(sound)

    # Setting the new sound to use while playing morse message
    morse_object.setMode(mode=sound)

    # Building the response back, announcing new mode
    response_body = "Successfully changed to set sounds " + str(sound)
    response = {
        'status': 1,
        'body': response_body
    }
    return make_response(response)


@app.route(f'/{INTERNAL}/log', methods=['GET'])
def log():
    # Fetching and validating argument 'n'
    log_number = request.args.get('n', type=int)
    check_input_log(log_number)

    # Building the response object by the validated n
    response_body = morse_object.get_log(log_number)
    response = {
        'status': 1,
        'body' : response_body

    }
    return make_response(jsonify(response))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
