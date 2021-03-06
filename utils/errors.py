from abc import abstractmethod

# Built in Error messages.
# Each error for a specific kind of failure.
__ParamsMsg__ = "\nMessage may contain only digit and letters and must not be empty"
__ParamsSound__ = "\nSound must be an Integer in range [1,10]"
__AlreadyRunning__ = "\n Server is currently busy with other message... Hold still!"
__LogNumber__ = "\nLog must be a non negative number!"


class Error(Exception):
    """
    Abstract Errors class
        Each instance of this class has a 'msg' method,
        indicating the specific problem caused for failure in system.
    """

    @abstractmethod
    def msg(self):
        pass


class ParamsError(Error):
    """
    Represents wrong parameters errors
    """
    def __init__(self, error_info):
        self.exec_info = error_info

    def msg(self):
        return f"Error: wrong Params error occurred\n {self.exec_info}"


# Method is validating the 'msg' input, that its length is larger than 0
def check_input_message(msg: str):
    if len(msg) > 0:
        pass
    else:
        err = ParamsError(__ParamsMsg__)
        raise Exception(err.msg())


# Method is checking for 'sound' input
# Validating its a valid integer, in range of [1, 10]
def check_input_sound(sound: int):
    if 0 < sound < 11:
        pass
    else:
        err = ParamsError(__ParamsSound__)
        raise Exception(err.msg())


# Method is checking if morse_object is currently playing a message
# If it does, we raise exception, otherwise we continue with the code normally.
def check_server_is_free(playing: bool):
    if not playing:
        pass
    else:
        err = ParamsError(__AlreadyRunning__)
        raise Exception(err.msg())


# Method is checking for a valid non negative 'n' for displaying last 'n' successful played messages
def check_input_log(n: int):
    if n > -1:
        pass
    else:
        err = ParamsError(__LogNumber__)
        raise Exception(err.msg())
