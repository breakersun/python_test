import socket, datetime, calendar, pyaes, binascii

# 组播组IP和端口
mcast_group_ip = '224.0.0.225'
mcast_group_port = 12345
padding = 0

def encrypt(msg : bytes, DID : str):
    iv = 0x00
    iv = iv.to_bytes(16, byteorder='big')
    key = DID[0:16].encode('ascii')
    aes = pyaes.AESModeOfOperationCBC(key, iv)
    ciphertext = aes.encrypt(msg[0:16])
    ciphertext = ciphertext + aes.encrypt(msg[16:])
    print('Ciphertext : ', binascii.hexlify(ciphertext))
    return ciphertext

def create_ring_msg(tone_idx : int):
    #utc timestamp
    epoch_time = datetime.datetime.utcnow()
    epoch_time = calendar.timegm(epoch_time.utctimetuple())
    #target N41 MAC
    mac = 'AA365E4D5054'
    #target N41 DID
    DID = "LFUSY41WDH9L9P210207"
    padding_byte = 0
    msg = epoch_time.to_bytes(4, byteorder='big') \
          + bytes.fromhex(mac) \
          + tone_idx.to_bytes(1, byteorder='big') \
          + DID.encode('ascii') \
          + padding_byte.to_bytes(1, byteorder="little")
    return msg

def sender(message : bytes):
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # message = "01"
    send_sock.sendto(message, (mcast_group_ip, mcast_group_port))


if __name__ == "__main__":
    message = encrypt(create_ring_msg(1), 'LFUSY41WDH9L9P210207')
    sender(message)