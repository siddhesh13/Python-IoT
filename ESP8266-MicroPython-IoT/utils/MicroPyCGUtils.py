import socket, network, time

def http_get(url):
    dataRecieved=False
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(250)
        if data:
            s.close()
            dataRecieved=True
            return str(data, 'utf8')
        else:
            dataRecieved=False
            break        
    if (not dataRecieved):
        return None
    
    


def connectToWifi(SSID, Password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        #print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, Password)
        while not sta_if.isconnected():
            pass
        #print sta_if.ifconfig()
        return sta_if.ifconfig()
