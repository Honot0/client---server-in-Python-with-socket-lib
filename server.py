import socket
import threading
import time

def logicka(request):
    print("request",request)
    superUser = 0
    places = []
    if request=='1'or '0':
        if request == '1':
            superUser=1
        concerts = ["Imagine Dragons", "Tarkov", "KINO", "Kazah-Han", "Coiner"]
        if superUser==1:
            places = ["Ряды 1-5: 500 рублей", "Ряды 6-9: 400 рублей", "Ряды 10-15: 200 рублей", "Партер 700 рублей"]
        if superUser==0:
            places = ["Ряды 1-5: 1000 рублей", "Ряды 6-9: 800 рублей", "Ряды 10-15: 600 рублей", "Партер 1500 рублей"]
        else:print('aaaa')
        rg = bytes(str([concerts, places]), 'utf8')
        # rg = b"byte"

        response = rg
        return response

    else:
        #S.find(str, [start], [end])
        #rg = bytes(str(request.decode('utf-8')), 'utf8')
        rg = ascii(request.decode("utf-8"))
        buy = request.split('/')
        print("\n","buy_____:",buy)
        pass
    pass



def process_request(conn, addr):
    print('connected:', addr)
    conn.settimeout(120)
    while True:
        try:
            data = conn.recv(1024)
            request = data.decode('utf-8')
            response = logicka({ascii(request)})
            # print(f'Получен запрос: {ascii(request)}')
            # print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
            conn.send(response)
            if not data:
                time.sleep(1)
        except socket.timeout:
            print("close connection by timeout")
            conn.close()
            break

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    th = threading.Thread(target=process_request, args=(conn, addr))
    th.start()












