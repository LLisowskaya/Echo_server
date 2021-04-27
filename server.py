#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import socket

# Set logging parameters.
log_format = '%(asctime)s %(name)s: %(levelname)s: %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
log_name = "TCP-Server"
logging.basicConfig(
    format=log_format, level=logging.INFO, datefmt=date_format)

# Create logging instance.
logger = logging.getLogger(log_name)

logger.info("Server is started.")
# Create IP/TCP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind server to 9090 port on all addresses.
sock.bind(('', 9090))
logger.info("Listening on 9090 port...")
# Run listening with 1 connection in the thread.
sock.listen(1)
# Get created socket and an address of a client.
while True:
    conn, addr = sock.accept()
    if not conn:
        continue

    logger.info(f"Client {addr[0]}:{addr[1]} is connected.")
    while True:
        data = conn.recv(1024)
        logger.info(f"Receive 1024 bytes from client {addr[0]}:{addr[1]}.")
        if not data:
            logger.info(f"Client {addr[0]}:{addr[1]} is disconnected.")
            break
        conn.send(data.upper())
        logger.info(f"Send data to client {addr[0]}:{addr[1]}.")
    conn.close()

logger.info("Server is stopped.")