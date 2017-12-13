
from PyQt4.QtCore import QWaitCondition,QMutex
from ethereum import utils

class Task(object):

    def __init__(self, request):
        self._request = request
        self._cond = QWaitCondition()

    def getRequest(self):
        return self._request

    def waitForResponse(self):
        self._cond.wait(QMutex())
        x = self._response
        del self._response
        return x

    def addResponse(self, response):
        self._response = response
        self._cond.wakeAll()

def check_perms(filepath):
    """ Validates the signer binary on the path given"""
    import os
    import stat

    st = os.stat(filepath)
    a_w = bool(st.st_mode & stat.S_IWOTH)
    if a_w:
        print("ERR: Binary is world-writeable. Configure the signer binary to be writeable only by the user.")
        print("\t{}".format(filepath))
        return False
    g_w = bool(st.st_mode & stat.S_IWGRP)
    if g_w: 
        print("ERR: Binary is group-writeable. Configure the signer binary to be writeable only by the user. ")
        print("\t{}".format(filepath))
        return False
    

    return True

def check_hash(filepath):
    import hashlib

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filepath, 'rb') as f:
        data = f.read(65536)
        while data:
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
            data = f.read(65536)

    print("Hashes for {}:".format(filepath))
    print("{0}".format(md5.hexdigest()))
    print("{0}".format(sha1.hexdigest()))
    print("{0}".format(sha256.hexdigest()))
    # At this point, we have nothing to validate against. 
    return sha256.hexdigest()

def isAddress(func):
    x = func()
    return validate(text, True)


def validAddressOrEmpty(text, allow_empty=True):
    """
    returns ( address, error-msg )
    """
    text = str(text)

    if len(text) == 0 and allow_empty:
        return (None, None)

    if len(text) != 42:
        return (None, "Invalid address")

    if not text[:2] in ["0x", "0X"]:
        return (None, "Invalid address (not prefixed)")

    try:
        c = int(text,16)
    except ValueError as e:
        return (None, "Invalid hex {}".format(str(e)))

    # Not validating checksums at the moment, the signer is not capable
    # of forwarding the exact address that was sent to it. 
    # 
    #if not utils.check_checksum(text):
    #    print("Incorrect checksum on {}".format(text))#, should be {}".format(checksummed_addr))
    #    return (None, "Incorrect checksum")

    return (text, None)

def validInt( text):
    """
    Tries to parse an input-text as if it was an int. 
    Returns as a hex-encoded version 

    returns hexstring, error
    """
    text = str(text)
    if len(text) == 0:
        return (None, "Invalid value")

    try:
        return (hex(int(text,10)), None)
    except ValueError as e:
        return (None, "Invalid value {}".format(str(e)))

def validHex( text):
    """
    Tries to parse an input-text as if it is hexadecimal data. 
    returns hexstring, error
    """

    text = str(text).lower()
    # 0-length is ok
    if len(text) == 0:
        return ("", None)
    
    # If not 0-length, must be prefixed
    if len(text) < 2:
        return (None, "Invalid data (not prefixed)")

    if not text[:2] in ["0x", "0X"]:
        return (None, "Invalid data (not prefixed)")        

    try:
        b = bytes.fromhex(text[2:])
        return (text, None)
    except ValueError as e:
        return (None, "Invalid hex {}".format(str(e)))
