import sys
import psutil
from PyQt5.QtWidgets import QDesktopWidget, QTabWidget, QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QListWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QTimer

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hardware Failure Monitor")
        self.resize(1080, 800) # resizing our window to be larger

        # Aligning the window to open up the center of our screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        self.tabWidget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabWidget.addTab(self.tab1, "Diagnostics")
        self.tabWidget.addTab(self.tab2, "Tasks")
        self.sidebar = QWidget()

        # Where we store all our layouts
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.tabWidget)


        # Chart related UI setup
        self.chartLayout = QVBoxLayout()
        self.cpu_series = QLineSeries()
        self.mem_series = QLineSeries()
        self.disk_series = QLineSeries()

        self.chart = QChart()

        # Coordinates Axis
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        # These are setting the chart data squares at the top
        self.chart.addSeries(self.cpu_series)
        self.chart.addSeries(self.mem_series)
        self.chart.addSeries(self.disk_series)

        self.chart.setAxisX(self.axisX, self.cpu_series)
        self.chart.setAxisY(self.axisY, self.cpu_series)
        self.chart.setAxisX(self.axisX, self.mem_series)
        self.chart.setAxisY(self.axisY, self.mem_series)
        self.chart.setAxisX(self.axisX, self.disk_series)
        self.chart.setAxisY(self.axisY, self.disk_series)

        self.chart_view = QChartView(self.chart)
        self.chartLayout.addWidget(self.chart_view)
        self.tab1.setLayout(self.chartLayout)

        # Will contain a list of widgets
        self.tasksLayout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.tasksLayout.addWidget(self.list_widget)

        # Adding Killing Process button
        self.killProcessButton = QPushButton('Kill Process')
        self.tasksLayout.addWidget(self.killProcessButton)
        self.killProcessButton.clicked.connect(self.killProcess)
        self.tasksLayout.addWidget(self.killProcessButton)
        self.tab2.setLayout(self.tasksLayout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.hardwareUsage)
        self.timer.start(1000)  # Refresh every second

        self.data_count = 0

        self.showCurrentRunningTaskProcess()

    # 
    def hardwareUsage(self):
        cpu_percent = psutil.cpu_percent()
        mem_info = psutil.virtual_memory()
        mem_percent = mem_info.percent
        disk_info = psutil.disk_usage('/')
        disk_percent = disk_info.percent

        self.cpu_series.append(self.data_count, cpu_percent)
        self.mem_series.append(self.data_count, mem_percent)
        self.disk_series.append(self.data_count, disk_percent)

        #  Update rendering out axis's
        self.axisX.setRange(0, self.data_count)
        self.axisY.setRange(0, 100)

        self.cpu_series.setName(f'CPU Usage: {cpu_percent}%')
        self.mem_series.setName(f'Memory Usage: {mem_percent}%')
        self.disk_series.setName(f'Disk Usage: {disk_percent}%')

        self.data_count += 1

    def showCurrentRunningTaskProcess(self):
        for process in psutil.process_iter(['pid', 'name', 'status']):
            self.list_widget.addItem(f"[PID={process.info['pid']}, Status={process.info['status']}] --- {process.info['name']} is currently running")

    def killProcess(self):
        currentItem = self.list_widget.currentItem()

        if currentItem:
            # Parsing text
            text = currentItem.text()
            parsed_pid1 = text.split('=') # Splitting on = char
            string = parsed_pid1[1].split(',') # Splitting string on , char
            pid = int(string[0])
            self.list_widget.takeItem(text)
            process = psutil.Process(pid)
            process.kill()
            self.showCurrentRunningTaskProcess() # Refreshing processed list