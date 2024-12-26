# Chat Room

**Chat Room** is a real-time messaging application built using Python sockets. It allows multiple clients to connect to a server and communicate with each other via a graphical user interface (GUI) built with `customtkinter`. The project consists of two main components: the server and the client.

## Features
- Real-time communication between multiple users.
- Simple and intuitive GUI for client interaction.
- Message broadcasting to all connected clients.
- Lightweight server capable of handling multiple clients simultaneously.

## Technologies Used
- **Backend**: Python sockets
- **Frontend**: `customtkinter` for GUI
- **Multithreading**: For handling multiple clients and real-time message updates.

---

## Installation and Usage

### 1. Prerequisites
- Python 3.x installed on your system.
- Install required libraries:
  ```bash
  pip install customtkinter pillow
### 2. Running the Server 
```bash
python server.py
```
### 3. Running the Client
```bash
python client.py
```
# Usage Instructions
- Start the server (server.py) to enable connections.
- Run multiple instances of the client (client.py) on the same or different machines to connect to the server.
- Type messages in the input box and press "Send" or hit "Enter" to broadcast your message.


