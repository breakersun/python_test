# -*- coding: utf-8 -*-

import os, datetime, getopt, sys


def err_stop_with(output, errmsg):
    print("")
    print("ERROR: #############################################")
    if (output != ""):
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


def parseTimeAndVoltage(idx, history):
    gap = len('0x1234 - 0x')
    startTimeH = '' + history[history.find(hex(idx)) + gap : history.find(hex(idx)) + gap + 4]
    startTimeH = startTimeH[2:] + startTimeH[:2]  # switch high and low bytes
    idx += 2
    startTimeL = '' + history[history.find(hex(idx)) + gap : history.find(hex(idx)) + gap + 4]
    startTimeL = startTimeL[2:] + startTimeL[:2]
    idx += 2
    endTimeH = '' + history[history.find(hex(idx)) + gap : history.find(hex(idx)) + gap + 4]
    endTimeH = endTimeH[2:] + endTimeH[:2]
    idx += 2
    endTimeL = '' + history[history.find(hex(idx)) + gap : history.find(hex(idx)) + gap + 4]
    endTimeL = endTimeL[2:] + endTimeL[:2]
    idx += 2
    vol = '' + history[history.find(hex(idx)) + gap : history.find(hex(idx)) + gap + 4]
    return '0x' + startTimeH + startTimeL, '0x' + endTimeH + endTimeL, '0x' + vol


def output():
    rawHistory = dumpHistory()
    for idx in range(0x4178, 0x41da, 10):
        start_epoch_sec = int(parseTimeAndVoltage(idx, rawHistory)[0], base=16)
        finish_epoch_sec = int(parseTimeAndVoltage(idx, rawHistory)[1], base=16)
        batt = int(parseTimeAndVoltage(idx, rawHistory)[2], base=16)
        print(hex(idx),
              'Charging Started at ' + datetime.datetime.fromtimestamp(start_epoch_sec).strftime('%m/%d/%Y %H:%M:%S'))
        print(hex(idx),
              'Charging Finished at ' + datetime.datetime.fromtimestamp(finish_epoch_sec).strftime('%m/%d/%Y %H:%M:%S'))
        print(hex(idx), 'Battery Level After Charging ', batt, '%')

try:
    arguments, values = getopt.getopt(sys.argv[1:], 'hdf:', ['help', 'device', 'file = '])

    for curArgument, curValue in arguments:
        if curArgument in ('-h', '--help'):
            print('== help info ==')
        elif curArgument in ('-d', '--device'):
            output()
        elif curArgument in ('-f', '--file'):
            print('Image File : ', curValue)
except getopt.error as err:
    print(str(err))
