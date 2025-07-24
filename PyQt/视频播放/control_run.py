# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME control_run
AUTHOR Pfolg
TIME 2025/6/6 18:03
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton,
    QFileDialog, QSlider, QHBoxLayout, QLabel
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl, Qt, QTime


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

        # 创建进度控制组件
        self.slider_progress = QSlider(Qt.Horizontal)
        self.slider_progress.setRange(0, 0)
        self.slider_progress.sliderMoved.connect(self.set_position)

        # 时间标签
        self.label_time = QLabel("00:00 / 00:00")

        # 音量控制
        self.slider_volume = QSlider(Qt.Horizontal)
        self.slider_volume.setRange(0, 100)
        self.slider_volume.setValue(80)
        self.slider_volume.valueChanged.connect(self.set_volume)
        self.audio_output.setVolume(self.slider_volume.value() / 100)

        # 连接按钮信号
        self.btn_open.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.media_player.play)
        self.btn_pause.clicked.connect(self.media_player.pause)
        self.btn_stop.clicked.connect(self.stop_video)

        # 连接媒体播放器信号
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.playbackStateChanged.connect(self.update_buttons)

        # 设置布局
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # 视频显示区域
        main_layout.addWidget(self.video_widget, 10)

        # 进度控制区域
        progress_layout = QHBoxLayout()
        progress_layout.addWidget(self.label_time)
        progress_layout.addWidget(self.slider_progress)
        main_layout.addLayout(progress_layout)

        # 控制按钮区域
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.btn_open)
        control_layout.addWidget(self.btn_play)
        control_layout.addWidget(self.btn_pause)
        control_layout.addWidget(self.btn_stop)
        control_layout.addWidget(QLabel("音量:"))
        control_layout.addWidget(self.slider_volume)
        main_layout.addLayout(control_layout)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 初始化按钮状态
        self.update_buttons(self.media_player.playbackState())

    def open_file(self):
        """打开视频文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频文件",
            "",
            "视频文件 (*.mp4 *.avi *.mkv *.mov *.flv *.wmv);;所有文件 (*)"
        )

        if file_path:
            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.media_player.play()

    def position_changed(self, position):
        """视频位置改变时更新进度条"""
        if not self.slider_progress.isSliderDown():  # 避免拖动滑块时的冲突
            self.slider_progress.setValue(position)

        # 更新时间显示
        if self.media_player.duration() > 0:
            current_time = QTime(0, 0, 0).addMSecs(position).toString("mm:ss")
            total_time = QTime(0, 0, 0).addMSecs(self.media_player.duration()).toString("mm:ss")
            self.label_time.setText(f"{current_time} / {total_time}")

    def duration_changed(self, duration):
        """视频时长改变时更新进度条范围"""
        self.slider_progress.setRange(0, duration)

    def set_position(self, position):
        """设置视频播放位置"""
        self.media_player.setPosition(position)

    def set_volume(self, volume):
        """设置音量"""
        self.audio_output.setVolume(volume / 100)

    def stop_video(self):
        """停止视频并重置位置"""
        self.media_player.stop()
        self.media_player.setPosition(0)

    def update_buttons(self, state):
        """根据播放状态更新按钮状态"""
        # 播放状态: 0=停止, 1=播放, 2=暂停
        self.btn_play.setEnabled(state != QMediaPlayer.PlayingState)
        self.btn_pause.setEnabled(state == QMediaPlayer.PlayingState)
        self.btn_stop.setEnabled(state != QMediaPlayer.StoppedState)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 尝试使用FFmpeg后端（如果可用）
    import os

    os.environ["QT_MEDIA_BACKEND"] = "ffmpeg"

    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())
