import psutil

def scan_connections():
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
        proc = None
        try:
            proc = psutil.Process(conn.pid).name() if conn.pid else None
        except Exception:
            proc = "N/A"
        connections.append({
            "pid": conn.pid,
            "process": proc,
            "local_address": laddr,
            "remote_address": raddr,
            "status": conn.status
        })
    return connections