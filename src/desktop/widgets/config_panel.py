from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QFormLayout, QSpinBox
from PyQt6.QtCore import Qt

class ConfigPanelWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # 标题
        title_label = QLabel("配置面板")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title_label)
        
        # 配置表单
        form_layout = QFormLayout()
        form_layout.setContentsMargins(10, 10, 10, 10)
        form_layout.setSpacing(10)
        
        # URL配置
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("请输入目标网址")
        form_layout.addRow("目标URL:", self.url_input)
        
        # 爬取频率设置
        self.frequency_spin = QSpinBox()
        self.frequency_spin.setRange(1, 60)
        self.frequency_spin.setValue(5)
        self.frequency_spin.setSuffix(" 秒")
        form_layout.addRow("爬取间隔:", self.frequency_spin)
        
        # 并发数控制
        self.concurrent_spin = QSpinBox()
        self.concurrent_spin.setRange(1, 10)
        self.concurrent_spin.setValue(3)
        form_layout.addRow("并发数量:", self.concurrent_spin)
        
        # 数据保存路径
        self.save_path = QLineEdit()
        self.save_path.setPlaceholderText("选择数据保存路径")
        form_layout.addRow("保存路径:", self.save_path)
        
        # 代理设置
        self.proxy_input = QLineEdit()
        self.proxy_input.setPlaceholderText("http://proxy:port")
        form_layout.addRow("代理设置:", self.proxy_input)
        
        # 请求头设置
        self.headers_input = QLineEdit()
        self.headers_input.setPlaceholderText("User-Agent, Cookie等")
        form_layout.addRow("请求头:", self.headers_input)
        
        # 数据格式选择
        self.format_combo = QComboBox()
        self.format_combo.addItems(["CSV", "JSON", "Excel"])
        form_layout.addRow("导出格式:", self.format_combo)
        
        layout.addLayout(form_layout)
        
        # 保存按钮
        save_btn = QPushButton("保存配置")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #1890ff;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #40a9ff;
            }
        """)
        layout.addWidget(save_btn)
        
        # 添加弹性空间
        layout.addStretch()