import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 55551
argument = (host, port)
sock.bind(argument)
sock.listen(10)  # 十個のクライアントの通信を受け取れる
clients = []


def loop_handler(connection, address):
    while True:
        try:
            # クライアントからデータを受信
            res = connection.recv(1024)
            if res == b'':
                # からの場合
                break

            receive_ip = address[0]
            receive_port = address[1]
            messages = f"発信元IP: {receive_ip}, Port: {receive_port}, message: {res}"
            print(messages)

            for client in clients:
                # 他のクライアントに受け取ったメッセージを送信
                client_ip = client[1][0]
                client_port = client[1][1]
                if client_ip == receive_ip and client_port == receive_port:
                    # 送信元のクライアントには送らないように処理
                    pass
                else:
                    # クライアントに受け取ったメッセージを送信
                    client[0].send(messages.encode('UTF-8'))


        except Exception as e:
            print(e)
            break

    clients.remove((connection, address))  # クライアントから対象のクライアントを削除
    connection.shutdown(socket.SHUT_RDWR)  # 対象のクライアントと接続を切断
    connection.close()
    return


while True:
    try:
        print("active_count", threading.active_count())
        print("wait")
        conn, addr = sock.accept()  # クライアントからの接続を受信,connは通信用オブジェクト、adrrはIPとポート番号

    except KeyboardInterrupt:
        print("KeyboardInterrupt")  # Ctrl + Cが入力された際に処理を中断
        sock.close()
        exit()
        break

    except Exception as e:
        print(e)
        break

    print(f"IP: {addr[0]}")
    print(f"Port:{addr[1]}")

    clients.append((conn, addr))  # clientsに格納
    # クライアントからデータを受信するためのスレッドを作成
    thread = threading.Thread(target=loop_handler, args=(conn, addr), daemon=True)
    thread.start()
    print("active_count", threading.active_count())
