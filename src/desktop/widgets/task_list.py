from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton
from PyQt6.QtCore import Qt

class TaskListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 标题区域
        title_label = QLabel("爬虫任务列表")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title_label)
        
        # 新建任务按钮
        new_task_btn = QPushButton("新建任务")
        new_task_btn.setStyleSheet("""
            QPushButton {
                background-color: #1890ff;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #40a9ff;
            }
        """)
        layout.addWidget(new_task_btn)
        
        # 任务列表
        self.task_list = QListWidget()
        self.task_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #e8e8e8;
                border-radius: 4px;
                background-color: white;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f0f0f0;
            }
            QListWidget::item:selected {
                background-color: #e6f7ff;
                color: #1890ff;
            }
        """)
        layout.addWidget(self.task_list)
        
        # 添加一些示例任务
        self.add_sample_tasks()
    
    def add_sample_tasks(self):
        sample_tasks = [
            "示例任务 - 商品数据采集",
            "示例任务 - 新闻内容爬取",
            "示例任务 - 图片批量下载"
        ]
        
        for task in sample_tasks:
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.task_list.addItem(item)