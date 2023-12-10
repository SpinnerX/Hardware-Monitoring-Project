import psutil
import sys
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QProgressBar, QStatusBar, QListWidget, QPushButton
from PyQt5.QtCore import QTimer

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('System Monitor')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # CPU Usage
        self.cpu_label = QLabel()
        self.cpu_progress = QProgressBar()
        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.cpu_progress)

        # Memory Usage
        self.mem_label = QLabel()
        self.mem_progress = QProgressBar()
        self.layout.addWidget(self.mem_label)
        self.layout.addWidget(self.mem_progress)
        
        # Disk Usage
        self.disk_label = QLabel()
        self.disk_progress = QProgressBar()
        self.layout.addWidget(self.disk_label)
        self.layout.addWidget(self.disk_progress)

        # Status Bar
        self.statusbar = QStatusBar()
        self.layout.addWidget(self.statusbar)
        self.statusbar.showMessage("Monitor started")

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.killProcessButton = QPushButton('Kill Process')
        self.layout.addWidget(self.killProcessButton)
        self.killProcessButton.clicked.connect(self.killProcess)
        self.layout.addWidget(self.killProcessButton)

        # Timer for periodical update of values
        self.timer = QTimer()
        self.timer.timeout.connect(self.hardwareUsage)
        self.timer.start(2000)  # Refresh every 2 seconds
        self.updateProcessList()
        
    def hardwareUsage(self):
        cpu_percent = psutil.cpu_percent()
        self.cpu_label.setText(f'CPU Usage: {cpu_percent}%')
        self.cpu_progress.setValue(int(cpu_percent))

        mem = psutil.virtual_memory()
        self.mem_label.setText(f'Memory Usage: {mem.percent}%')
        self.mem_progress.setValue(int(mem.percent))

        disk = psutil.disk_usage('/')
        self.disk_label.setText(f'Disk Usage: {disk.percent}%')
        self.disk_progress.setValue(int(disk.percent))

        # Check for high resource usage and present a warning if necessary
        if cpu_percent > 90 or mem.percent > 80 or disk.percent > 80:
            self.statusbar.showMessage('Warning: High resource usage detected')
        else:
            self.statusbar.showMessage('Resources usage is normal')

    def updateProcessList(self):
        for process in psutil.process_iter(['pid', 'name', 'status']):
            self.list_widget.addItem(f"PID: {process.info['pid']}, Name: {process.info['name']}, Status: {process.info['status']}")
    
    def killProcess(self):
        currentItem = self.list_widget.currentItem()
        if currentItem:
            pid = int(currentItem.text().split()[1][:-1]) # Extracting PID from string
            process = psutil.Process(pid)
            process.kill()
            self.update_process_list() # Refreshint processed list
