#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import socket

# Set logging parameters.
log_format = '%(asctime)s %(name)s: %(levelname)s: %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
log_name = "TCP-Client"
logging.basicConfig(
    format=log_format, level=logging.INFO, datefmt=date_format)

# Create logging instance.
logger = logging.getLogger(log_name)

server, port = "localhost", 9090

sock = socket.socket()
sock.connect((server, port))
logger.info(f"Connect to server {server} on port {port}.")

while True:
    data = input('Type message: ')

    if data == "exit":
        sock.close()
        logger.info(f"Disconnect from server {server}.")
        break

    if not data:
        print("You should type something!")
        continue

    sock.send(str.encode(data))
    logger.info(f"Send data to server {server}.")

    data = sock.recv(1024)
    logger.info(f"Receive data from server {server}.")

    print(data)