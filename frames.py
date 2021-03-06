#!/usr/bin/env python3
# Designed for use with boofuzz v0.2.0

from boofuzz import *


def main():
    """
    This example is a very simple FTP fuzzer. It uses no process monitory
    (procmon) and assumes that the FTP server is already running.
    """
    host = "192.168.1.22"
    port = 445
    proto = "tcp"

    session = Session(
        target=Target(
            connection = SocketConnection(host, port, proto)
            )
        )

    #FRAME EXAMPLES ################################################################

    # Tree Connect Request 102
    s_initialize("Tree_Connect_AndX_Request")
    s_bytes(value = b'\x00\x00\x00\x5a\xff\x53\x4d\x42\x75\x00\x00\x00\x00\x18\x07\xc8'
                    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe'
                    b'\x00\x08\xc0\x00\x04\xff\x00\x5a\x00\x08\x00\x01\x00\x2f\x00\x00'
                    b'\x5c\x00\x5c\x00\x31\x00\x39\x00\x32\x00\x2e\x00\x31\x00\x36\x00'
                    b'\x38\x00\x2e\x00\x31\x00\x2e\x00\x32\x00\x32\x00\x5c\x00\x59\x00'
                    b'\x4f\x00\x4c\x00\x4f\x00\x00\x00\x3f\x3f\x3f\x3f\x3f\x00')


    s_initialize("Trans2_Request")
    s_bytes(value=b'\x00\x00\x00\x56\xff\x53\x4d\x42\x32\x00\x00\x00\x00\x18\x07\xc8'
                  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x08\x9c\x0d'
                  b'\x01\x08\x02\x06\x0f\x12\x00\x00\x00\x0a\x00\x00\x40\x00\x00\x00'
                  b'\x00\x00\x00\x00\x00\x00\x00\x12\x00\x44\x00\x00\x00\x00\x00\x01'
                  b'\x00\x01\x00\x15\x00\x00\x00\x00\x16\x00\x56\x05\x06\x00\x04\x01'
                  b'\x00\x00\x00\x00\x5c\x00\x2a\x00\x00\x00')
                  
                  
    s_initialize("Create_Request") #file
    s_bytes(value=b'\x00\x00\x00\x56\xff\x53\x4d\x42\xa2\x00\x00\x00\x00\x18\x07\xc8'
                  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x08\x9c\x0d'
                  b'\x01\x08\x42\x09\x18\xff\x00\xde\xde\x00\x00\x00\x16\x00\x00\x00'
                  b'\x00\x00\x00\x00\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                  b'\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
                  b'\x02\x00\x00\x00\x03\x03\x00\x00\x00\x00')
                  
    s_initialize("Rename_Request") #rename file
    s_bytes(value=b'\x00\x00\x00\x76\xff\x53\x4d\x42\x07\x00\x00\x00\x00\x18\x07\xc8'
                  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x08\xff\xfe'
                  b'\x01\x08\x41\x13\x01\x16\x00\x51\x00\x04\x5c\x00\x1d\x04\x3e\x04'
                  b'\x32\x04\x4b\x04\x39\x04\x20\x00\x42\x04\x35\x04\x3a\x04\x41\x04'
                  b'\x42\x04\x3e\x04\x32\x04\x4b\x04\x39\x04\x20\x00\x34\x04\x3e\x04'
                  b'\x3a\x04\x43\x04\x3c\x04\x35\x04\x3d\x04\x42\x04\x2e\x00\x74\x00'
                  b'\x78\x00\x74\x00\x00\x00\x04\x3f\x5c\x00\x6b\x00\x65\x00\x6b\x00'
                  b'\x2e\x00\x74\x00\x78\x00\x74\x00\x00\x00')
    
    
    s_initialize("Write_Request") #write to file
    s_bytes(value=b'\x00\x00\x00\x4a\xff\x53\x4d\x42\x2f\x00\x00\x00\x00\x18\x07\xe8'
                  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x08\xff\xfe'
                  b'\x01\x08\x03\x71\x0e\xff\x00\xde\xde\x0c\xc0\x00\x00\x00\x00\xff'
                  b'\xff\xff\xff\x00\x00\x00\x00\x00\x00\x0a\x00\x40\x00\x00\x00\x00'
                  b'\x00\x0b\x00\xee\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x64')
    
    
    s_initialize("Read_Request") #read file
    s_bytes(value=b'\x00\x00\x00\x3b\xff\x53\x4d\x42\x2e\x00\x00\x00\x00\x18\x07\xe8'
                  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x08\xff\xfe'
                  b'\x01\x08\x43\x1b\x0c\xff\x00\xde\xde\x0a\x40\x00\x00\x00\x00\x0a'
                  b'\x00\x0a\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00')
    
    s_initialize("Close_Request") #close file
    s_bytes(value=b'\x00\x00\x00\x29\xff\x53\x4d\x42\x04\x00\x00\x00\x00\x18\x07\xc8'
                  b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x08\xff\xfe'
                  b'\x01\x08\x42\x2a\x03\x0a\x40\xff\xff\xff\xff\x00\x00')
    




    session.connect(s_get("Tree_Connect_AndX_Request"))
    session.connect(s_get("Trans2_Request"))
    session.connect(s_get("Create_Request"))
    session.connect(s_get("Rename_Request"))
    session.connect(s_get("Write_Request"))
    session.connect(s_get("Read_Request"))
    session.connect(s_get("Close_Request"))

    session.fuzz()


if __name__ == "__main__":
    main()
