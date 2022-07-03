from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from qt_material import apply_stylesheet
from time import sleep
from threading import Thread
from playsound import playsound
from settings import TSettings

class Tomato():
    m_focustime = 0
    m_resttime = 5
    status_flag = False
    ts = TSettings()
    
    def __init__(self):
        self.BindEvents()

    def BindEvents(self):
        
        self.window = QUiLoader().load(self.ts.dir_ui)
        self.window.setFixedSize(self.window.width(),self.window.height())
        self.window.start.clicked.connect(self.StartFocus)
        self.window.reset.clicked.connect(self.ResetTime)
        self.window.reset.setProperty('class','warning')
        self.window.timedial.valueChanged.connect(self.SetTime)
              
    def ClockThread(self):
            while self.status_flag == True:
                self.isZero() 
                for i in range(self.m_focustime):
                    if self.status_flag:
                        sleep(1)    #休眠时长
                        self.CountDown()
                    else:
                        pass

    def isZero(self):
        if self.window.timedial.value() == 0:
            self.status_flag = False
            self.window.start.setText(self.ts.button_text[1])
            self.StopFocus()
            
            
    def CountDown(self):
        if self.window.timedial.value() >= 0 and self.window.timedial.value() < 10:
            self.window.timelabel.setText(self.ts.time[1].format(int(self.window.timelabel.text()[-1]) - 1))
            self.window.timedial.setValue(self.window.timedial.value() - 1)
        elif self.window.timedial.value() < 60:
            self.window.timelabel.setText(self.ts.time[2].format(int(self.window.timelabel.text()[-2:]) - 1))
            self.window.timedial.setValue(self.window.timedial.value() - 1)
        elif self.window.timedial.value() == 60:
            self.window.timelabel.setText(self.ts.time[4])
            self.window.timelabel.setText(self.ts.time[2].format(int(self.window.timelabel.text()[-2:]) - 1))
            self.window.timedial.setValue(self.window.timedial.value() - 1)

    def StartFocus(self):
        if self.status_flag == False:
            self.status_flag = True
            self.window.start.setText(self.ts.button_text[0])
            thread_clock = Thread(target = self.ClockThread)
            thread_clock.start()
            
        else:
            self.StopThread()
            self.window.start.setText(self.ts.button_text[1])
            self.isZero() 
        
    def StopFocus(self):
        thread_music = Thread(target=self.Music)
        thread_music.start()
    
    def StopThread(self):
        self.status_flag = False

    def ResetTime(self): 
        self.StopThread()
        self.window.timedial.setValue(0)
        self.window.timelabel.setText(self.ts.time[0])
    
    def SetTime(self):
        if self.window.timedial.value() < 10:
            self.window.timelabel.setText(self.ts.time[1].format(self.window.timedial.value()))
            self.m_focustime = self.window.timedial.value()
                    
        elif self.window.timedial.value() <60:
            self.window.timelabel.setText(self.ts.time[2].format(self.window.timedial.value()))
            self.m_focustime = self.window.timedial.value()
            
        elif self.window.timedial.value() == 60:
            self.window.timelabel.setText(self.ts.time[3])
            self.m_focustime = self.window.timedial.value()
     
    def Music(self):
        playsound(self.ts.dir_music)       


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon('./ui/logo.png'))
    
    tomato = Tomato()
    ts = TSettings()
    apply_stylesheet(app,
                     theme=ts.theme,invert_secondary=False,
                     extra=ts.style_extra)
    
    tomato.window.show()
    app.exec()
    
    
if __name__ == '__main__':
    main()        