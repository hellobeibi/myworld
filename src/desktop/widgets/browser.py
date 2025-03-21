from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QToolBar
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt

class BrowserWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # 工具栏
        toolbar = QToolBar()
        toolbar.setStyleSheet("""
            QToolBar {
                background: white;
                border-bottom: 1px solid #e8e8e8;
                padding: 5px;
            }
        """)
        
        # 导航按钮
        self.back_btn = QPushButton("←")
        self.forward_btn = QPushButton("→")
        self.refresh_btn = QPushButton("⟳")
        for btn in [self.back_btn, self.forward_btn, self.refresh_btn]:
            btn.setFixedSize(30, 30)
            btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    border-radius: 4px;
                    background: transparent;
                }
                QPushButton:hover {
                    background: #f0f0f0;
                }
            """)
            toolbar.addWidget(btn)
        
        # URL输入框
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("请输入网址")
        self.url_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #e8e8e8;
                border-radius: 4px;
                padding: 5px;
                margin: 0 10px;
            }
            QLineEdit:focus {
                border-color: #1890ff;
            }
        """)
        toolbar.addWidget(self.url_input)
        
        # 开发者工具按钮
        self.dev_tools_btn = QPushButton("开发者工具")
        self.dev_tools_btn.setStyleSheet("""
            QPushButton {
                background-color: #1890ff;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #40a9ff;
            }
        """)
        toolbar.addWidget(self.dev_tools_btn)
        
        layout.addWidget(toolbar)
        
        # 浏览器视图
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("about:blank"))
        layout.addWidget(self.web_view)
        
        # 连接信号
        self.back_btn.clicked.connect(self.web_view.back)
        self.forward_btn.clicked.connect(self.web_view.forward)
        self.refresh_btn.clicked.connect(self.web_view.reload)
        self.url_input.returnPressed.connect(self.navigate_to_url)
        self.web_view.urlChanged.connect(self.update_url)
    
    def navigate_to_url(self):
        url = self.url_input.text()
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.web_view.setUrl(QUrl(url))
    
    def update_url(self, url):
        self.url_input.setText(url.toString())