from bluetooth import *
import time

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


    return target_address


if __name__ == '__main__':

    find_address('HC05')
    address = '98:D3:31:F5:A7:47'
    port = 1
    socket = BluetoothSocket(RFCOMM) 
    socket.connect((address, port))
    socket.send('1')
    socket.close()
    #отправка
    time.sleep(5)

    server_sock=BluetoothSocket(RFCOMM )
    port = 1
    server_sock.bind(("",port))
    server_sock.listen(1)
    address = '98:D3:31:F5:A7:47'
    port = 1
    client_sock = BluetoothSocket(RFCOMM)
    client_sock.connect((address, port))
    data = client_sock.recv(1024)
    print("received [%s]" % data)
    client_sock.close()
    server_sock.close()
    #получение













































    