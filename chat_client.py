import socket
import threading
import time

# 接続先
host = "127.0.0.1"
port = 55551
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ソケット作成
sock.connect((host, port))  # 指定されたIPとポートで接続


def receive_handler(sock_):
    while True:
        try:
            res = sock_.recv(1024)
            if res == b'':
                break

            print("<" + res.decode() + ">")  # サーバーから送られてきた情報をプリント
            print(">")

        except Exception as e:
            print(e)
            break

    time.sleep(1)
    sock_.close()
    return


thread = threading.Thread(target=receive_handler, args=(sock,))
thread.start()

while True:
    your_input = input(">")
    if your_input == b'':
        print("処理終了です")
        break
    try:
        sock.send(your_input.encode("UTF-8")) #サーバーに対してデータを送る
    except Exception as e:
        print(e)
        break

    sock.shutdown(socket.SHUT_RDWR) #サーバーと接続を切る
    sock.close()
