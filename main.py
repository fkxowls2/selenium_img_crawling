from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QProgressBar, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys, time
from crawl import CrawlingManager


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("crawl.ui")[0]

#멀티 쓰레드
class Worker(QThread):
    num_image = pyqtSignal(int)
    num_idx = pyqtSignal(int)
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
    
    def run(self):
        try:
            cm = CrawlingManager()
        except:
            pass
        #     self.parent.txtWindow3.setPlainText('Chrome이 설치되어 있는지 확인해주세요!')
        images = cm.img_crawling(keyword=self.parent.keyword)
        # self.parent.progressBar.setRange(1, len(images))
        self.num_image.emit(len(images))
        idx = 1
        for image in images:
            cm.img_save(idx, image, save_path=self.parent.folder_path)
            # self.parent.progressBar.setValue(idx)
            self.num_idx.emit(idx)
            idx += 1
        # self.parent.txtWindow3.setPlainText('이미지 수집이 완료되었습니다.')
        cm.driver_close()
        self.quit()
        self.wait(1000)


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pathBtn.clicked.connect(self.path_btn_func)
        self.keywordBtn.clicked.connect(self.keyword_btn_func)
        self.startBtn.clicked.connect(self.start_btn_func)
        
        self.folder_path = '.'
        self.keyword = self.txtEdit.toPlainText()
        
        self.w = Worker(self)
        self.w.num_image.connect(self.set_progress_bar)
        self.w.num_idx.connect(self.set_progress_bar_value)
        
    def path_btn_func(self):
        self.folder_path = QFileDialog.getExistingDirectory(self)
        self.txtWindow1.setPlainText(self.folder_path)

    def keyword_btn_func(self):
        self.keyword = self.txtEdit.toPlainText()
        self.txtWindow2.setPlainText(self.keyword)
        
    def start_btn_func(self):
        self.txtWindow2.setPlainText(self.keyword)
        self.txtWindow3.setPlainText('이미지 수집 중입니다. 인터넷 창을 닫지 말아주세요.')
        # self.w = Worker(self)
        self.w.start()
        self.txtWindow3.setPlainText('이미지 수집이 완료되었습니다.')
    
    @pyqtSlot(int)    
    def set_progress_bar(self, num):
        self.progressBar.setRange(1, num)
        
    @pyqtSlot(int)    
    def set_progress_bar_value(self, num):
        self.progressBar.setValue(num)
        


if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()