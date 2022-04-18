import socket 
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
SIZE = 1024 
FORMAT = 'utf-8'

def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(ADDR)
  server.listen(5)
  print(f'Server is listening at {IP}:{PORT}')
  client, addr = server.accept()
  print(f'Connection from {addr[0]:{addr[1]}}')
  data = client.recv(SIZE)
  print(f'Received data: {data.decode(FORMAT)}')
  item = data.decode(FORMAT).split("_")
  FILENAME = item[0]
  FILESIZE = int(item[1])
  print(f'File name: {FILENAME}')
  print(f'File size: {FILESIZE}') 
  client.send(data)
  bar = tqdm(range(FILESIZE), f'Recieving {FILENAME}', unit='B', unit_scale=True, unit_divisor=1024)

  with open(f"recieved_{FILENAME}", 'w') as f:
    while True:
      data = client.recv(SIZE)
      if not data:
        break
      f.write(data.decode(FORMAT))
      client.send("Data received".encode(FORMAT))
      bar.update(len(data))

  client.close()
  server.close()

if __name__ == '__main__':
  main()