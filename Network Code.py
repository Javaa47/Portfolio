import socket

def _read_host() -> str:
    while True:
        host = input('Host: ').strip()

        if host != '':
            return host

        print('Please specify a host')
        
def _read_port() -> int:
    while True:
        try:
            port = int(input('Port: '))

            if 0 <= port <= 65535:
                return port
        except ValueError:
            pass

        print('Ports must be a integers between 0 65535')
def _read_message() -> str:
    return input('Message: ')


def _print_response(response: str) -> None:
    print(f'Response: {response}')

    
def _send_message(connection: 'connection', message: str) -> None:
    echo_socket, echo_input, echo_output = connection

    echo_output.write(message + '\r\n')
    echo_output.flush()
def _recieve_message(connection: 'connection') -> str:
    echo_socket, echo_input, echo_output = connection

    return echo_input.readline()[:-1]
    
def _connect(host: str, port: int) -> 'connection':
    echo_socket = socket.socket()
    echo_socket.connect((host, port))

    echo_input = echo_socket.makefile('r')
    echo_output = echo_socket.makefile('w')

    return echo_socket, echo_input, echo_output

def _close(connection: 'connection')  -> None:
    echo_socket, echo_input, echo_output = connection

    echo_input.close()
    echo_output.close()
    echo_socket.close()
    
def run() -> None:
    host = _read_host()
    port = _read_port()

    connection = None
    try:
        print(f'Connecting to {host} (port {port}...')
        connection = _connect(host, port)
        print(f'Connected!')

        while True:
            message = _read_message()
            if message == '':
                break
            else:
                _send_message(connection, message)
                response = _recieve_message(connection)
                _print_response(response)
    finally:
        if connection != None:
            _close(connection)
            print('Closed connection; goodbye')
if __name__ == '__main__':
    run()
