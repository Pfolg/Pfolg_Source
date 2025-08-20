# -*- coding: UTF-8 -*-
"""
PROJECT_NAME mines_cleaner
PRODUCT_NAME PyCharm
NAME mainWindow
AUTHOR Pfolg
TIME 2025/8/16 22:42
"""
import os.path
import random
import time
from dataclasses import dataclass
from PIL.ImageQt import QPixmap
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QMouseEvent, QFont
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QFrame,
    QApplication,
    QSpinBox,
    QPushButton,
)
from enum import Enum, auto


class GameStatus(Enum):
    RUNNING = auto()  # 游戏进行中
    WIN = auto()  # 游戏胜利
    DEFEAT = auto()  # 游戏失败
    READY = auto()  # 游戏准备中


available_flag = 0
flags = 0
mines_num = 0
right_num = 0
used_squares = 0
total = 0
gameStatus = GameStatus.READY
LOGFILE = "log\\log.txt"

if not os.path.exists("log"):
    os.mkdir("log")


def get_screen_info() -> tuple:
    """读取屏幕长宽，用于窗口定位"""
    # 获取现有的 QApplication 实例
    _app = QApplication.instance()
    if _app is not None:
        # 获取显示器数据
        screen = _app.primaryScreen().geometry()
        # 返回长宽
        return screen.width(), screen.height()
    else:
        return 800, 600


level = {
    "1": [9, 9, 10],
    "2": [16, 16, 30],
    "3": [30, 16, 57],
    "4": [40, 16, 76],
}


@dataclass
class GameLabel:
    mine: str = "💣"
    flag: str = "🚩"
    bang: str = "💥"
    mine_pic: str = ""
    flag_pic: str = ""
    bang_pic: str = ""
    default_color: str = "background-color:lightblue;"
    clicked_color0: str = "background-color:#ffffff;"
    clicked_color1: str = "background-color:#ffffff;color:#0000ff"
    clicked_color2: str = "background-color:#ffffff;color:#008000"
    clicked_color3: str = "background-color:#ffffff;color:#ff0000"
    clicked_color4: str = "background-color:#ffffff;color:#000080"
    clicked_color5: str = "background-color:#ffffff;color:#800000"
    clicked_color6: str = "background-color:#ffffff;color:#008080"
    clicked_color7: str = "background-color:#ffffff;color:#000000"
    clicked_color8: str = "background-color:#ffffff;color:#808080"
    bang_color: str = "background-color:#ffffff"


class Square(QLabel):
    def __init__(self, p: QWidget, x: int, y: int, w: int, mark: int):
        super().__init__()
        self.setParent(p)
        self.mark = mark
        self.click_timer = QTimer()
        self.click_timer.setSingleShot(True)
        self.click_timer.timeout.connect(self.leftMouseClick)
        self.click_count = 0
        self.x = x
        self.y = y
        self.w = w
        self.isFlag = False
        self.isClicked = False
        self.isGaming = True
        self.setGeometry(self.x, self.y, self.w, self.w)
        self.setScaledContents(True)
        self.setStyleSheet(GameLabel.default_color)
        self.setFrameShape(QFrame.Shape.Box)
        f = QFont()
        f.setPointSize(18)
        self.setFont(f)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def get_neighbors(self):
        """获取当前方块周围的所有方块"""
        if not hasattr(self, 'parent_widget') or not self.parent_widget:
            return []

        neighbors = []
        # 获取当前方块在网格中的位置
        for i, row in enumerate(self.parent_widget.squares):
            for j, square in enumerate(row):
                if square == self:
                    row_index, col_index = i, j
                    break

        # 检查周围8个方向
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # 跳过自身
                    continue

                new_row = row_index + dx
                new_col = col_index + dy

                # 确保位置在网格范围内
                if (
                    0 <= new_row < self.parent_widget.num_x
                    and 0 <= new_col < self.parent_widget.num_y
                ):
                    neighbor = self.parent_widget.squares[new_row][new_col]
                    neighbors.append(neighbor)

        return neighbors

    def leftMouseClick(self):
        global flags, available_flag, right_num, mines_num, total, gameStatus
        if gameStatus != GameStatus.RUNNING:
            return
        if self.isFlag | self.isClicked:
            return

        sty = [
            GameLabel.clicked_color0,
            GameLabel.clicked_color1,
            GameLabel.clicked_color2,
            GameLabel.clicked_color3,
            GameLabel.clicked_color4,
            GameLabel.clicked_color5,
            GameLabel.clicked_color6,
            GameLabel.clicked_color7,
            GameLabel.clicked_color8,
        ][self.mark]
        if self.mark:
            self.setText(str(self.mark))
        self.setStyleSheet(sty)

        self.isClicked = True
        if isinstance(self, Mines):
            gameStatus = GameStatus.DEFEAT
        else:
            total -= 1
            # 如果是空白方块，自动展开周围
            if self.mark == 0:
                self.expand_blank_area()

        # 判定胜利条件
        if (
            right_num == mines_num
            and flags == mines_num
            and available_flag <= 0
            and total <= 0
        ):
            gameStatus = GameStatus.WIN

    def rightMouseClick(self):
        global flags, available_flag, right_num, mines_num, total, gameStatus
        if gameStatus != GameStatus.RUNNING or self.isClicked:
            return
        if self.isFlag:
            self.setText("")
            if GameLabel.flag_pic:
                self.setPixmap(QPixmap(GameLabel.flag_pic))
            self.isFlag = False
            flags -= 1
            available_flag += 1
            total += 1
            if isinstance(self, Mines):  # 如果是地雷
                right_num -= 1
        else:
            if available_flag <= 0:
                return
            self.setPixmap(QPixmap(""))
            self.setText(GameLabel.flag)
            self.isFlag = True
            if flags < mines_num:  # 确保不超过最大标记数
                flags += 1
                available_flag -= 1
                total -= 1
                if isinstance(self, Mines):  # 如果是地雷
                    right_num += 1
        print(flags, available_flag, right_num, mines_num, total)
        if (
            right_num == mines_num
            and flags == mines_num
            and available_flag <= 0
            and total <= 0
        ):
            gameStatus = GameStatus.WIN

    def double_click(self):
        global gameStatus
        if gameStatus != GameStatus.RUNNING:
            return
        if self.isFlag:
            return
        elif not self.isClicked:
            self.leftMouseClick()
        else:
            # 递归识别逻辑
            if self.mark == 0:  # 空白方块自动展开周围
                self.expand_blank_area()
                return

            # 计算周围标记数量
            flag_count = 0
            neighbors = self.get_neighbors()
            for neighbor in neighbors:
                if neighbor.isFlag:
                    flag_count += 1

            # 只有当周围标记数等于当前方块显示的数字时才执行展开
            if flag_count == self.mark:
                for neighbor in neighbors:
                    # 只展开未标记且未点击的方块
                    if not neighbor.isFlag and not neighbor.isClicked:
                        neighbor.leftMouseClick()

    def expand_blank_area(self):
        """展开空白区域（递归展开周围所有空白方块）"""
        visited = set()
        stack = [self]

        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)

            # 点击当前方块（如果是空白）
            if not current.isClicked and not current.isFlag:
                current.leftMouseClick()

            # 如果当前方块是空白，继续展开周围
            if current.mark == 0:
                for neighbor in current.get_neighbors():
                    if (
                        not neighbor.isClicked
                        and not neighbor.isFlag
                        and neighbor not in visited
                    ):
                        stack.append(neighbor)

    def mousePressEvent(self, event: QMouseEvent):
        # 左键点击处理
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_count += 1
            if self.click_count == 1:
                # 设置双击检测时间（通常250-500ms）
                self.click_timer.start(100)
            elif self.click_count == 2:
                self.click_timer.stop()
                self.double_click()
                self.click_count = 0

        # 右键点击处理
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightMouseClick()

        # 中键点击处理（可选）
        elif event.button() == Qt.MouseButton.MiddleButton:
            pass

        # 传递事件给父类（保持默认行为）
        super().mousePressEvent(event)


# 地雷类
class Mines(Square):
    def __init__(self, p, x, y, w, mark):
        super().__init__(p, x, y, w, mark)

    def leftMouseClick(self):
        global gameStatus
        if gameStatus != GameStatus.RUNNING:
            return
        if self.isFlag | self.isClicked:
            return
        self.setText(GameLabel.bang)
        self.setStyleSheet(GameLabel.bang_color)
        self.isClicked = True
        # 调用游戏结束函数
        gameStatus = GameStatus.DEFEAT

    def double_click(self):
        pass


class Root(QWidget):
    def __init__(self):
        super().__init__()
        self.w_w = 200
        self.w_h = 200
        self.num_y = 0
        self.num_x = 0
        self.timeTimer = QTimer()
        self.timeTimer.timeout.connect(self.update_time)
        self.timeTimer.timeout.connect(self.setTexts)
        self.timeLabel = QLabel("00:00", self)
        self.start_time = 0
        self.elapsed_time = 0
        self.labelProcess = QLabel(self)
        self.availableFlag = QLabel(self)
        self.usedFlags = QLabel(self)
        self.restartBtn = QPushButton(self)
        self.oldStatus = None

        self.square_w = 30

        self.squares: list[list[Square]] = []
        self.setWindowTitle("Mines Sweeper")
        self.setWindowFlags(
            Qt.WindowType.CustomizeWindowHint
            | Qt.WindowType.WindowCloseButtonHint
            | Qt.WindowType.WindowMinimizeButtonHint
        )
        sw, sh = get_screen_info()
        self.setGeometry(
            int((sw - self.w_w) / 2), int((sh - self.w_h) / 2), self.w_w, self.w_h
        )
        self.chooseLevel()
        self.show()

    def chooseLevel(self):
        if self.timeTimer.isActive():
            self.reset_timer()
        for child in self.children():
            child.deleteLater()
        self.w_w = 200
        self.w_h = 200
        self.num_y = 0
        self.num_x = 0
        sw, sh = get_screen_info()
        self.setGeometry(
            int((sw - self.w_w) / 2), int((sh - self.w_h) / 2), self.w_w, self.w_h
        )

        btn_checkLog = QPushButton("Log", self)
        qsb = QSpinBox(self)
        qsb.setMaximum(4)
        qsb.setMinimum(1)
        qsb.setGeometry(60, 40, 60, 30)
        qlb = QLabel(self)
        qlb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        qlb.setText(
            f"{level.get(str(qsb.value()))[0]} X {level.get(str(qsb.value()))[1]} + {level.get(str(qsb.value()))[2]}"
        )
        qlb.setGeometry(0, 80, 200, 30)
        qpb = QPushButton("Start", self)
        qpb.setGeometry(70, 120, 60, 30)
        btn_checkLog.setGeometry(70, 160, 60, 30)
        qlb.show()
        qsb.show()
        qpb.show()
        btn_checkLog.show()

        def __update():
            qlb.hide()
            qsb.hide()
            qpb.hide()
            btn_checkLog.hide()
            self.setLevel(qsb.value())

        btn_checkLog.clicked.connect(lambda: os.startfile(LOGFILE))
        qsb.valueChanged.connect(
            lambda: qlb.setText(
                f"{level.get(str(qsb.value()))[0]} X {level.get(str(qsb.value()))[1]} + {level.get(str(qsb.value()))[2]}"
            )
        )
        qpb.clicked.connect(__update)

    def get_aroundMines(self, sq_row: int, sq_col: int, selected: list[int]) -> int:
        """计算指定位置周围的地雷数量

        Args:
            :param sq_col: 列
            :param sq_row: 行
            :param selected: 地雷位置列表
        Returns:
            周围地雷的数量

        """
        count = 0
        # 检查周围8个方向
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # 跳过自身
                    continue

                new_row = sq_row + dx
                new_col = sq_col + dy

                # 确保新位置在网格范围内
                if 0 <= new_row < self.num_x and 0 <= new_col < self.num_y:
                    neighbor_index = 10 * new_row + new_col
                    if neighbor_index in selected:
                        count += 1

        return count

    def setLevel(self, lv: int):
        global mines_num, right_num, available_flag, flags, total, gameStatus
        if lv in [1, 2, 3, 4]:
            self.num_y = level.get(str(lv))[0]
            self.num_x = level.get(str(lv))[1]
            mines_num = level.get(str(lv))[2]
        else:
            self.num_x = 0
            self.num_y = 0
            return
        right_num = flags = 0
        available_flag = mines_num
        total = self.num_x * self.num_y
        self.w_h = self.num_x * self.square_w if self.num_x else 200
        self.w_w = self.num_y * self.square_w + 200
        print(f"{self.num_x} X {self.num_y} + {mines_num}")
        self.squares.clear()
        sw, sh = get_screen_info()
        selected_positions = random.sample(
            [10 * i + j for i in range(self.num_x) for j in range(self.num_y)],
            mines_num,
        )
        # print("Mines: ", selected_positions)
        self.setGeometry(
            int((sw - self.w_w) / 2), int((sh - self.w_h) / 2), self.w_w, self.w_h
        )
        if (not self.num_y) | (not self.num_x):
            return

        for i in range(self.num_x):
            x = []
            for j in range(self.num_y):
                flag = 10 * i + j
                if flag in selected_positions:
                    m = Mines(
                        self, j * self.square_w, i * self.square_w, self.square_w, -1
                    )
                else:

                    m = Square(
                        self,
                        j * self.square_w,
                        i * self.square_w,
                        self.square_w,
                        self.get_aroundMines(i, j, selected_positions),
                    )
                m.parent_widget = self
                m.show()
                x.append(m)
            self.squares.append(x)
        self.setSideBar()
        gameStatus = GameStatus.RUNNING

    def update_time(self):
        """更新计时器显示"""
        if self.start_time:
            elapsed = time.time() - self.start_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            self.timeLabel.setText(f"{minutes:02d}:{seconds:02d}")
        if gameStatus != GameStatus.RUNNING:
            self.writeLog()
            self.stop_timer()
            if gameStatus == GameStatus.WIN:
                self.EndWidget()
            else:
                self.EndWidget("DEFEAT")

    def start_timer(self):
        """开始计时"""
        if not self.timeTimer.isActive():
            self.start_time = time.time()
            self.timeTimer.start(200)  # 每秒更新一次

    def stop_timer(self):
        """停止计时"""
        if self.timeTimer.isActive():
            self.timeTimer.stop()
            self.elapsed_time = time.time() - self.start_time

    def reset_timer(self):
        """重置计时器"""
        self.stop_timer()
        self.start_time = None
        self.elapsed_time = 0
        self.timeLabel.setText("00:00")

    def setTexts(self):
        self.labelProcess.setText(
            f"{total}/{(self.num_x * self.num_y)} {(1 - total / (self.num_x * self.num_y)) * 100:.2f}%"
        )
        self.availableFlag.setText(f"Ava : {available_flag}")
        self.usedFlags.setText(f"Use : {flags}")
        if gameStatus != self.oldStatus:
            print(gameStatus)
            self.oldStatus = gameStatus

    def setSideBar(self):
        self.timeLabel = QLabel("00:00", self)
        self.labelProcess = QLabel(self)
        self.availableFlag = QLabel(self)
        self.usedFlags = QLabel(self)
        self.restartBtn = QPushButton("Restart", self)
        btn_end = QPushButton("End", self)
        a, st = 10, 40
        for i in [
            self.timeLabel,
            self.labelProcess,
            self.availableFlag,
            self.usedFlags,
        ]:
            i.setStyleSheet("font-size: 20px; color: black;")
            i.setGeometry(self.w_w - 180, a, 180, 30)
            a += st
            i.show()
        self.restartBtn.setGeometry(self.w_w - 180, 200, 80, 30)
        self.restartBtn.clicked.connect(self.chooseLevel)
        self.restartBtn.show()

        btn_end.setGeometry(self.w_w - 180, 240, 80, 30)
        btn_end.clicked.connect(self.__end)
        btn_end.show()

        self.reset_timer()
        self.start_timer()

    def __end(self):
        self.stop_timer()
        self.writeLog()
        self.destroy()
        _app = QApplication.instance()
        _app.exit()

    def writeLog(self):
        msg = (
            f"({time.strftime('%Y/%m/%d %H:%M:%S')}) "
            f"game: {self.num_x} X {self.num_y} + {mines_num} "
            f"[{gameStatus} {total}/{(self.num_x * self.num_y)} {(1 - total / (self.num_x * self.num_y)) * 100:.2f}% "
            f"Ava : {available_flag} Use : {flags} Time : {self.timeLabel.text()}]\n"
        )
        with open(LOGFILE, "a", encoding="utf-8") as f:
            f.write(msg)

    def EndWidget(self, t="VICTORY") -> None:
        endW = QLabel(self)
        endW.setGeometry(0, 0, self.w_w, self.w_h)
        if t == "VICTORY":
            endW.setStyleSheet(
                "background-color:rgba(0, 0, 0, 150);" "color:rgba(255, 202, 15, 150)"
            )
        else:
            endW.setStyleSheet(
                "background-color:rgba(0, 0, 0, 150);" "color:rgba(237, 28, 36, 150)"
            )
        endW.setText(t)
        a = QFont()
        a.setPointSize(int(self.w_h / 5))
        a.setBold(True)
        endW.setFont(a)
        endW.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn1 = QPushButton("Retry", endW)
        btn2 = QPushButton("Quit", endW)

        btn1.clicked.connect(self.chooseLevel)
        btn2.clicked.connect(lambda: QApplication.instance().exit())
        btn1.setGeometry(
            int(0.2 * self.w_w),
            int(0.8 * self.w_h),
            int(0.2 * self.w_w),
            int(0.1 * self.w_h),
        )
        btn2.setGeometry(
            int(0.6 * self.w_w),
            int(0.8 * self.w_h),
            int(0.2 * self.w_w),
            int(0.1 * self.w_h),
        )
        btn1.show()
        btn2.show()
        endW.show()
