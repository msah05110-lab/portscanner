import socket

def scan_ports(target):

    try:
        target_ip = socket.gethostbyname(target)
    except:
        return [{"port":"Error","service":"Invalid Host"}]

    common_ports = {
        21:"FTP",
        22:"SSH",
        23:"TELNET",
        25:"SMTP",
        53:"DNS",
        80:"HTTP",
        110:"POP3",
        143:"IMAP",
        443:"HTTPS"
    }

    open_ports = []

    for port in range(1, 1025):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:

            service = common_ports.get(port, "Unknown")

            open_ports.append({
                "port": port,
                "service": service
            })

        sock.close()

    if len(open_ports) == 0:
        open_ports.append({
            "port":"None",
            "service":"No Open Ports Found"
        })

    return open_ports