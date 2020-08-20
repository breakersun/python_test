# -*- coding: utf-8 -*-

import os

def err_stop_with(output, errmsg):
    print("")
    print("ERROR: #############################################")
    if(output != ""):
        print("ERROR: ################ OUT-MSG-BEG ################")
        print("ERROR: " + output)
        print("ERROR: ################ OUT-MSG-END ################")
    else:
        print("ERROR: #############################################")
    print("ERROR: " + errmsg)
    print("ERROR: #############################################")
    print("")
    exit(-1)

def dumpHistory():
    print('Read Charging History ...')
    dump = os.popen('D:\\CSR_uEnergy_SDK-2.6.1.7\\tools\\bin\\e2cmd.exe readblock 0x4178 50')
    output = dump.read()
    if output.find('successful') != -1:
        return output
    else:
        err_stop_with(output, 'Dumping NVM Failed')


def dumpBdAddr():
    dump_keyr = os.popen("D:\\CSR_uEnergy_SDK-2.6.1.7\\tools\\bin\csconfigcmd.exe dump tmp.keyr")
    output = dump_keyr.read()
    if (output.find("Success") != -1):
        with open("tmp.keyr", 'r') as keyr:
            lines = keyr.readlines()
            for i in range(0, len(lines)):
                if (lines[i].find("BDADDR") != -1):
                    bd_addr = lines[i].split("=")[1]
            keyr.close()
            os.remove('tmp.keyr')
            return bd_addr.replace(" ", "")
    else:
        err_stop_with(output, "Dump the keyr file from device FAIL!")


print(dumpBdAddr())