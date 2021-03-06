import tkinter as tk
# from tkinter import ttk 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from cr import *

class window(tk.Frame) :
    def __init__(self, selected_course) :
        tk.Frame.__init__(self)
        self.status = tk.StringVar()
        self.status.set('')
        self.master.title('已選課程')
        self.master.configure(bg='#FFFFE0')
        w, h = self.master.maxsize()
        self.master.geometry("{}x{}".format(w, h))
        # self.course = selected_course
        self.pack()     
        self.deliver_btn()
        self.text_title()
        self.print_course()
        self.account = tk.StringVar()
        self.password = tk.StringVar()
        self.lab_account = tk.Label(text='帳號',font='微軟正黑體 10',fg='#8B814C',bg='#FFFFE0')
        self.entry_account = tk.Entry(textvariable=self.account)
        self.lab_password = tk.Label(text='密碼',font='微軟正黑體 10',fg='#8B814C',bg='#FFFFE0')
        self.entry_password = tk.Entry(textvariable=self.password,show='*')
        self.entry_password.pack(side='bottom')
        self.lab_password.pack(side='bottom')
        self.entry_account.pack(side='bottom')
        self.lab_account.pack(side='bottom')

    def text_title(self) :
        self.title = tk.Label(text='已選課程',fg='#8B814C',bg='#FFFFE0',font='微軟正黑體 15')
        self.title.pack()
    def deliver_btn(self) :
        self.btn = tk.Button(text='送出表單',bg= '#CDBA96',command=self.import_course)
        self.img = tk.PhotoImage(file=r"./3.png")
        self.status_label = tk.Label(textvariable=self.status,fg='#8B814C',bg='#FFFFE0')
        self.btn.config(image=self.img)
        self.btn.pack(side='bottom')
        self.status_label.pack(side='bottom')
    def print_course(self) :
        self.course = get_selected_course(target)
        # self.lab = tk.Label(text='111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111  22222222222')
        # self.lab.pack()
        
        # target_idx = [97001, 97002, 97003]
        flag = True
        for value in self.course:    
            self.lab = tk.Label(text=value,font='微軟正黑體 10',width ='160',height='3',bg=('#FFFACD' if flag else '#EEE8CD'))
            self.lab.pack()
            flag = not flag

    def import_course(self) :
        driver = webdriver.Chrome(r'..\chromedriver.exe')
        url = 'https://nol2.aca.ntu.edu.tw/nol/guest/index.php'
        driver.get(url)
        time.sleep(2)

        #進入登入畫面
        driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frameset/frame[1]"))
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/input").click()
        #輸入帳號密碼（請自行輸入）
        try:
            driver.find_element_by_name('user').clear()
            driver.find_element_by_name('user').send_keys(self.account.get())
            driver.find_element_by_name('pass').clear()
            driver.find_element_by_name('pass').send_keys(self.password.get())
            driver.find_element_by_name('Submit').click()
        except Exception:
            print(Exception)
        # self.status.set('成功登入課程網')
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_name('main'))  # 進入各式課程選欄
        driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/map/area[1]').click()
        driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/a').click()  # 進入課程篩選頁面

        select_button = Select(driver.find_element_by_id('cstype')) 
        select_button.select_by_visible_text('流水號')

        
        for number in target :
            driver.find_element_by_id('csname').clear()
            driver.find_element_by_id('csname').send_keys(number)
            driver.find_element_by_name("Submit22").click()
            # driver.switch_to.frame(driver.find_element_by_name('main'))
            driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[2]/td[18]").click()


root = window(target) 
root.mainloop()
