# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/6/6 17:57
"""
"""
Q:PySide6可以播放视频吗?
DeepSeek：
是的，PySide6 可以播放视频。它通过 QtMultimedia 和 QtMultimediaWidgets 模块提供了视频播放功能。
以下是实现方法和一个完整示例：

核心组件
    QMediaPlayer: 负责媒体文件的加载和控制（播放/暂停/停止）
    
    QVideoWidget: 用于显示视频画面的窗口组件
    
    QAudioOutput (可选)：控制音频输出设备

"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 视频播放器")
        self.resize(800, 600)

        # 创建主组件
        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()

        # 设置媒体播放器
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setAudioOutput(self.audio_output)

        # 创建控制按钮
        self.btn_open = QPushButton("打开视频")
        self.btn_play = QPushButton("播放")
        self.btn_pause = QPushButton("暂停")
        self.btn_stop = QPushButton("停止")

        # 连接按钮信号
        self.btn_open.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.media_player.play)
        self.btn_pause.clicked.connect(self.media_player.pause)
        self.btn_stop.clicked.connect(self.media_player.stop)

        # 设置布局
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_play)
        layout.addWidget(self.btn_pause)
        layout.addWidget(self.btn_stop)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_file(self):
        # 打开文件对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频文件",
            "",
            "视频文件 (*.mp4 *.avi *.mkv *.mov);;所有文件 (*)"
        )

        if file_path:
            # 加载并自动播放
            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.media_player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())
