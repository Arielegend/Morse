# Txt_to_Morse is the helper method that plays the message, and returns the msg in morse syntax.
from utils.utilities import Txt_to_Morse


class Morse:
    """
    Morse class. has 3 fields
        1. playing (boolean): Indicating weather a message is currently being played or not.
        2. log        (list): Holds the successful played message in chronological order.
        3. mode        (int): An integer in range of [1,10], indicated the sound tuple to use playing morse code.
    """

    def __init__(self):
        self.playing = False
        self.log = []
        self.mode = 1

    def getPlay(self) -> bool:
        return self.playing

    def setPlay(self, playing: bool) -> None:
        self.playing = playing

    def getMode(self) -> int:
        return self.mode

    def setMode(self, mode: int) -> None:
        self.mode = mode

    def playMessage(self, msg: str) -> None:
        # Method Txt_to_Morse is playing the code, and returns the message in 'morse'.
        morse_string = Txt_to_Morse(msg=msg, mode=self.getMode())

        # Updating the log field of morse_object.
        self.append_log(msg, morse_string)

    # Helper method, appending log field with object of form {msg, morse}
    def append_log(self, msg, morse) -> None:
        log_to_append = {'msg': msg, 'morse': morse}
        self.log.append(log_to_append)

    # Method returns last 'num' of played messages.
    # It does so by reaching each iteration the last log_member, minus a helper running index
    def get_log(self, num: int):
        if len(self.log) <= num:
            return self.log
        if num == 0:
            return []

        response = []
        index_helper = 1         # Each iteration we increase index
        len_log = len(self.log)  # Helper variable for prettier code
        while index_helper < (num + 1):
            temp = self.log[len_log - index_helper]
            index_helper += 1
            response.append(temp)

        return response
