import socket 
from tqdm import tqdm
import os

IP = socket.gethostbyname(socket.gethostname)
PORT = 8080
ADDR = (IP, PORT)
SIZE = 1024 
FORMAT = 'utf-8'
FILENAME = input(str('Enter file name: '))
FILESIZE = os.path.getsize(FILENAME)

def main():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(ADDR)
  print(f'Connected to {IP}:{PORT}')
  data = f"{FILENAME}_{FILESIZE}"
  client.send(data.encode(FORMAT))
  msg = client.recv(SIZE).decode(FORMAT)
  print(f"server: {msg}")
  bar = tqdm(range(FILESIZE), f'Sending {FILENAME}', unit='B', unit_scale=True, unit_divisor=1024)
  with open(FILENAME, 'r') as f:
    while True:
      data = f.read(SIZE)

      if not data:
        break

      client.send(data.encode(FORMAT))

      msg = client.recv(SIZE).decode(FORMAT)

      bar.update(len(data))
  
  client.close()

if __name__ == '__main__':
  main()