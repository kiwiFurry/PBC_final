# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Window(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widget()
    def create_widget(self):
        self.fbtn = tk.Button(self, text='確定送出', width=15, height=1, bg="white", fg="black")
        self.fbtn.grid(row=0, column=9)
        self.flb = tk.Label(self, text='選擇系所', bg='white', fg='black')
        self.flb.grid(row=1, column=9)
        all_coll = ['---請選擇系所---','中文所','中文系','中文系國際生','中英翻譯學程','中草藥學程','亞洲藝術學程','人口學程','人類所','人類系','企管碩士專班','保健營養學程','健管所','傳播學程','傳染病學程','光電所','免疫所','全球衛生學程','全電運輸學程','公事所','公衛碩士學程','公衛系','公衛院','共教組','分子比病所','分子科技學程','分子細生所','分子醫學學程','分子醫學所','分子醫藥學程','分子醫藥組','創意創業學程','創新設計學院','創業創新MB','動物福祉學分','動科所','動科系','化學所化學組','化學所化生組','化學系','化工所','化工系','口腔生物所','台大遠距教學','哲學所','哲學系','商研所','國企系','國家理論中心','國發所','國際企業所','國際學程','國際神經學程','園藝所','園藝所作物組','園藝所景觀組','園藝所產品組','園藝系','圖資所','圖資系','土木所','土木所CAE組','土木所交通組','土木所大地組','土木所水利組','土木所測量組','土木所營管組','土木所結構組','土木系','地理所','地理系','地科學程','地質所','地質所地質組','地質系','基因學位學程','基蛋所','外文所','外文系','大氣所','大氣系','大陸研究學程','天文物理所','奈米科技學程','婦女性別學程','學士後護','寫作教學中心','工學院','工業工程所','工科海洋所','工科海洋系','工管系','工管系企管組','工管系科管組','幹細胞學程','建城所','微生所','微生所寄生組','微生所微免組','心理所','心理系','應力所','應數所','應用物理所','戲劇所','戲劇系','政治所','政治系','政治系公行組','政治系國關組','政治系政論組','教育學程','數學所','數學系','數量財務學程','文學院','新聞所','日文所','日文系','日本學程','昆蟲所','昆蟲系','會計所','會計系','材料所','材料系','東亞學分學程','森林環資所','森林環資系','植微所','植微系','植物科學所','植醫碩士學程','機械所','機械系','歐洲暨歐盟學','歷史所','歷史系','毒理所','氣候永續學位','永續資源學程','法律所','法律系','法律系司法組','法律系法學組','法律系財法組','法律院','法醫所','流預所','流預所流病組','流預所生統組','流預所預醫組','海洋所','海洋所化學組','海洋所地物理','海洋所漁業組','海洋所物理組','海洋科學學程','漁業科學所','牙醫所','牙醫系','物治所','物治系','物治系六年制','物理所','物理系','獸醫所','獸醫系','理學院','環工所','環職所','生傳發展所','生傳發展系','生化分生所','生化科學所','生工所','生工系','生態演化所','生技學程','生技所','生技系','生物機電所','生物機電系','生物科技所','生物統計學程','生理所','生科所','生科系','生科院','生資國際學程','生農院','生醫電資所','病理所','知識管理學程','社工所','社工系','社會所','社會系','社科院','神經認知學程','科法所','管理院','統計碩士學位','經典人文學程','經濟所','經濟系','綠色精密學程','網媒所','翻譯碩士學程','老人長照學程','職治所','職治系','職衛所','能源科技學程','腦與心智所','腫瘤醫學所','臨床動醫所','臨床藥學所','臨醫所','臨醫所試驗組','臨醫所醫研組','臺文所','臺灣研究學程','茶與茶業學程','華教碩士學程','藝史所','藝術設計學程','藥學所','藥學系','藥物科技組','藥理所','行社所','解剖所','語言所','課外活動組','護理所','護理系','財金所','財金系','資工所','資工系','資料科學學程','資管系','資訊管理所','轉譯博士學程','農化所','農化系','農經所','農經系','農藝所','農藝所作物組','農藝所生統組','農藝系','運動健康管理','醫學系','醫學院','醫工所','醫工系','醫技所','醫技系','醫教生倫所','醫材影像所','醫衛共同課程','電信所','電子所','電機所','電機系','電資院','音樂學所','領導學程','食品科技學程','食安所','食科所','高分子所']
        self.college= ttk.Combobox(self, values=all_coll)
        self.college.grid(row=2, column=9)
        self.college.current(0)
        '''self.txt = tk.Text(height=1, width=10)'''
        tkFont.Font(size=32, family="Courier New")
        which_date = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        date = dict()
        for i in range(7):
            date[i] = which_date[i]
        time = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D']
        period = dict()
        for i in range(15):
            period[i] = time[i]
        self.lb1 = dict()
        for i in range(7):
            self.lb1[i] = tk.Label(self, text=date[i], bg="green", fg="white")
            self.lb1[i].grid(row=0, column=i + 1)
            '''self.lb[i].pack(side='left')'''
        self.lb2 = dict()
        for i in range(15):
            self.lb2[i] = tk.Label(self, text=period[i], bg="green", fg="white")
            self.lb2[i].grid(row=i + 1, column=0)
        self.btn = dict()
        for i in range(105):
            '''self.btn[i] = tk.Button(self, width=8, height=2, bg="gray", command=lambda f=i: self.change_color(f))'''
            self.btn[i] = tk.Button(self, width=8, height=2, bg="gray", command=lambda f=i: self.click(f))
            self.btn[i].grid(row=i % 15 + 1, column=int(i / 15) + 1, sticky=tk.N + tk.E + tk.S + tk.W)

    '''def change_color(self, index):
        self.btn[index].configure(bg='green')'''
    add = dict()
    for j in range(105):
        add[j] = 0
    information = []

    def click(self, index):
        if self.add[index] % 2 != 0:  # 取消選課
            self.btn[index].configure(bg='gray')
            self.add[index] += 1
            self.information.remove(index)
        else:  # 選課
            self.btn[index].configure(bg='green')
            self.add[index] += 1
            self.information.append(index)
        print(self.information)

        '''self.information[self.lb1[int(index / 7)]] = self.lb2[int(index / 7)]'''


calendar = Window()
'''calendar.master.resizable(0, 0)'''
'''calendar.master.geometry("400x200")'''
calendar.master.grid_rowconfigure(0, weight=1)
calendar.master.grid_columnconfigure(0, weight=1)
w, h = calendar.master.maxsize()
calendar.master.geometry("{}x{}".format(w, h))
calendar.master.title('課表')
calendar.mainloop()