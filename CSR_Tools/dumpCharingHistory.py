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
    return startTimeH + startTimeL, endTimeH + endTimeL, vol


def outputDevice():
    rawHistory = dumpHistory()
    for idx in range(0x4178, 0x41da, 10):
        start_epoch_sec = int(parseTimeAndVoltage(idx, rawHistory)[0], base=16)
        finish_epoch_sec = int(parseTimeAndVoltage(idx, rawHistory)[1], base=16)
        batt = int(parseTimeAndVoltage(idx, rawHistory)[2], base=16)
        print(hex(idx), 'Charging Started at ' + datetime.datetime.fromtimestamp(start_epoch_sec).strftime('%m/%d/%Y %H:%M:%S'))
        print(hex(idx), 'Charging Finished at ' + datetime.datetime.fromtimestamp(finish_epoch_sec).strftime('%m/%d/%Y %H:%M:%S'))
        print(hex(idx), 'Battery Level After Charging ', batt, '%')


def outputFile(img_file):
    lines = img_file.readlines()

    for i in range(0, len(lines)):
        if (lines[i].find('@004178') != -1):
            starting = i
            break

    for i in range(0, 50, 5):
        starting_epoch_sec_h = lines[starting + i][-3:-1] + lines[starting + i][-5:-3]
        starting_epoch_sec_l = lines[starting + i + 1][-3:-1] + lines[starting + i][-5:-3]
        ending_epoch_sec_h = lines[starting + i + 2][-3:-1] + lines[starting + i][-5:-3]
        ending_epoch_sec_l = lines[starting + i + 3][-3:-1] + lines[starting + i][-5:-3]
        batt = lines[starting + i + 4][-5:-1]

        starting_epoch_sec = starting_epoch_sec_h + starting_epoch_sec_l
        ending_epoch_sec = ending_epoch_sec_h + ending_epoch_sec_l
        starting_epoch_sec = int(starting_epoch_sec, base=16)
        ending_epoch_sec = int(ending_epoch_sec, base=16)
        batt = int(batt, base=16)

        print(lines[i + starting][0:7],
              'Charging Started at ' + datetime.datetime.fromtimestamp(starting_epoch_sec).strftime('%m/%d/%Y %H:%M:%S'))
        print(lines[i + starting][0:7],
              'Charging Finished at ' + datetime.datetime.fromtimestamp(ending_epoch_sec).strftime('%m/%d/%Y %H:%M:%S'))
        print(lines[i + starting][0:7], 'Battery Level After Charging ', batt, '%')

try:
    arguments, values = getopt.getopt(sys.argv[1:], 'hdf:', ['help', 'device', 'file = '])

    for curArgument, curValue in arguments:
        if curArgument in ('-h', '--help'):
            print('== help info ==')
            print('-d : Read from Device Directly')
            print('-f dump.img : Read from dump image file')
        elif curArgument in ('-d', '--device'):
            outputDevice()
        elif curArgument in ('-f', '--file'):
            print('Image File : ', curValue)
            with open(curValue, 'r') as dump_img:
                outputFile(dump_img)
                dump_img.close()
except getopt.error as err:
    print(str(err))
