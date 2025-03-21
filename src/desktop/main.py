import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSplitter
from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from widgets.task_list import TaskListWidget
from widgets.config_panel import ConfigPanelWidget
from widgets.browser import BrowserWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("爬虫可视化工具")
        self.resize(1200, 800)
        
        # 创建主布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # 创建分割器
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)
        
        # 左侧任务列表面板
        task_panel = TaskListWidget()
        splitter.addWidget(task_panel)
        
        # 中央浏览器区域
        browser_panel = BrowserWidget()
        splitter.addWidget(browser_panel)
        
        # 右侧配置面板
        config_panel = ConfigPanelWidget()
        splitter.addWidget(config_panel)
        
        # 设置分割器比例
        splitter.setStretchFactor(0, 1)  # 任务列表
        splitter.setStretchFactor(1, 3)  # 浏览器
        splitter.setStretchFactor(2, 1)  # 配置面板

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()