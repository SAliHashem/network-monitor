import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from network_scanner_service.scanner import scan_connections
from logger_service.logger import init_db, save_log, get_logs

def start_gui():
    init_db()

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Network Monitor")
    layout = QVBoxLayout()

    output = QTextEdit()
    output.setReadOnly(True)

    def refresh_connections():
        connections = scan_connections()
        output.clear()
        for conn in connections:
            save_log(conn)
            output.append(str(conn))

    def show_logs():
        logs = get_logs()
        output.clear()
        for log in logs:
            output.append(str(log))

    btn_refresh = QPushButton("Scan Connections")
    btn_refresh.clicked.connect(refresh_connections)

    btn_logs = QPushButton("Show Logs")
    btn_logs.clicked.connect(show_logs)

    layout.addWidget(btn_refresh)
    layout.addWidget(btn_logs)
    layout.addWidget(output)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())