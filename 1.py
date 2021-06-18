from bluetooth import *
import serial
import socket

def find_address(target_name):
    target_address = None

    print("scaning bluetooth device...")
    nearby_devices = discover_devices()

    print("find bluetooth device:\n")
    for address in nearby_devices:
        name = lookup_name(address)
        if target_name == name:
            target_address = address
            print("\033[32mtarget address:\n")
            print(str(name) + '\t' + address)
            break
        print(str(name) + '\t' + address)

    if target_address is None:
        print("\n\033[031m\ntarget device not found!\n")

    print('\033[0m')
    return target_address

if __name__ == '__main__':
    server_sock=BluetoothSocket(RFCOMM )

    port = 1
    server_sock.bind(("",port))
    server_sock.listen(1)

    # client_sock,address = server_sock.accept()
    # print("Accepted connection from ",address)

    address = '98:D3:31:F5:A7:47'
    port = 1
    client_sock = BluetoothSocket(RFCOMM)
    client_sock.connect((address, port))

    data = client_sock.recv(1024)
    print("received [%s]" % data)

    client_sock.close()
    server_sock.close()


















































    # address = find_address('HC05') # BQ-5530L # Mi Phone
    # address = '98:D3:31:F5:A7:47'
    # # address = '40:DF:8B:90:30:84'
    # # address = 'D8:63:75:7F:48:44' # vadim
    # # port = 0xFA0 # 4000
    # port = 1
    # socket = BluetoothSocket(RFCOMM) # L2CAP

    # socket.bind((address, port))

    # # print(socket)

    # print(socket.connect((address, port)))

    # print(socket.send('1'))

    # # try:
    #     print('try connection')
    #     print(socket.connect((address, port)))

    # except:
    #     print('connection error')

    # socket.close()

    # serverSocket = socket.socket(socket.AF_BLUETOOTH,
    #                          socket.SOCK_STREAM,
    #                          socket.BTPROTO_RFCOMM)

    # serverSocket.setTimeout(1)
    # serverSocket.bind((address, port))
    # serverSocket.listen(1)

    # ser = serial.Serial('/dev/rfcomm0', 115200, timeout=1)