'''

'''
import os,sys,time,numpy,pygame,random
from pygame.locals import *
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Image
import tkinter as tk
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

title = "Order"
size = (800, 600)
red=(255,0,0)
black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
yellow = (255, 255, 0)
aqua = (0, 255, 255)
KEY_REPEAT_SETTING = (200, 70)
screen = pygame.display.set_mode(size, 0, 32)

#  目錄
def menu(screen):

    font = pygame.font.SysFont("arial", 40)
    prompt1 = "Input Order"
    prompt2 = "Search"
    prompt3 = "Exit"
    time.sleep(0.2)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        text1 = font.render(prompt1, True, white)
        text1_1 = font.render(prompt1, True, aqua)
        text2 = font.render(prompt2, True, white)
        text2_1 = font.render(prompt2, True, aqua)
        text3 = font.render(prompt3, True, white)
        text3_1 = font.render(prompt3, True, aqua)

        x, y = pygame.mouse.get_pos()

        screen.fill(black)

        if 310 <= x <= 310 + text1.get_width() and 250 <= y <= 250 + text1.get_height():
            screen.blit(text1_1, (310, 250))
            screen.blit(text2, (330, 290))
            screen.blit(text3, (360, 330))
            if pygame.mouse.get_pressed()[0]:
                key_in()
        elif 330 <= x <= 330 + text2.get_width() and 290 <= y <= 290 + text1.get_height():
            screen.blit(text1, (310, 250))
            screen.blit(text2_1, (330, 290))
            screen.blit(text3, (360, 330))
            if pygame.mouse.get_pressed()[0]:
                search()
        elif 365 <= x <= 365 + text3.get_width() and 330 <= y <= 330 + text1.get_height():
            screen.blit(text1, (310, 250))
            screen.blit(text2, (330, 290))
            screen.blit(text3_1, (360, 330))
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            screen.blit(text1, (310, 250))
            screen.blit(text2, (330, 290))
            screen.blit(text3, (360, 330))

        pygame.display.update()


#=======================================================================
#key in info
master = tk.Tk()
master.title("Input Order")
master.resizable(0,0)
QU1=["No:","Date:","To (company):","Attn(person):","TEL:","ext.","FAX:"]
QU2=["payment(days):","Validity:","Delivery:","Remark:"]
QU3=["No.","Item","Q'ty","Unit","Unit Price","Sub-Price"]
def show_entry_fields():
    global e0,e1,e2,e3,e4,e5,e6
    prpdf([e0.get(),e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),
    e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),
    e14.get(),e15.get(),e16.get(),e17.get(),e18.get(),e19.get(),e20.get(),
    e21.get(),e22.get(),e23.get(),e24.get(),e25.get(),e26.get(),e27.get(),
    e28.get(),e29.get(),e30.get(),e31.get(),e32.get(),e33.get(),e34.get(),
    e35.get(),e36.get(),e37.get(),e38.get(),e39.get(),e40.get(),e41.get(),
    e42.get(),e43.get(),e44.get(),e45.get(),e46.get(),e47.get(),e48.get(),
    e49.get(),e50.get(),e51.get(),e52.get(),e53.get(),e54.get()])
def cls_info():
    global e0,e1,e2,e3,e4,e5,e6
    e0.delete(0, 'end');e1.delete(0, 'end');e2.delete(0, 'end');e3.delete(0, 'end');e4.delete(0, 'end');e5.delete(0, 'end');e6.delete(0, 'end')
def cls_item():
    global e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46
    e7.delete(0, 'end');e8.delete(0, 'end');e9.delete(0, 'end');e10.delete(0, 'end');
    e11.delete(0, 'end');e12.delete(0, 'end');e13.delete(0, 'end');e14.delete(0, 'end');e15.delete(0, 'end');
    e16.delete(0, 'end');e17.delete(0, 'end');e18.delete(0, 'end');e19.delete(0, 'end');e20.delete(0, 'end');
    e21.delete(0, 'end');e22.delete(0, 'end');e23.delete(0, 'end');e24.delete(0, 'end');e25.delete(0, 'end');
    e26.delete(0, 'end');e27.delete(0, 'end');e28.delete(0, 'end');e29.delete(0, 'end');e30.delete(0, 'end');
    e31.delete(0, 'end');e32.delete(0, 'end');e33.delete(0, 'end');e34.delete(0, 'end');e35.delete(0, 'end');
    e36.delete(0, 'end');e37.delete(0, 'end');e38.delete(0, 'end');e39.delete(0, 'end');e40.delete(0, 'end');
    e41.delete(0, 'end');e42.delete(0, 'end');e43.delete(0, 'end');e44.delete(0, 'end');e45.delete(0, 'end');
    e46.delete(0, 'end');
def cls_pay():
    global e47,e48,e49,e50,e51,e52,e53,e54
    e47.delete(0, 'end');e48.delete(0, 'end');e49.delete(0, 'end');e50.delete(0, 'end');
    e51.delete(0, 'end');e52.delete(0, 'end');e53.delete(0, 'end');e54.delete(0, 'end');
for i in range(len(QU1)):
    tk.Label(master,
             text=QU1[i]).grid(row=i)
    locals()["e%s"%i] = tk.Entry(master)
    locals()["e%s"%i].grid(row=i, column=1)

for i in range(len(QU3)):
    tk.Label(master,
             text=QU3[i]).grid(row=8, column=i)

a=9
z=7
for j in range(5):
    for i in range(len(QU3)):
        if i==1:
            locals()["e%s"%(z)] = tk.Entry(master,width=60)
            locals()["e%s"%(z)].grid(row=a+3*j, column=i);z+=1
            locals()["e%s"%(z)] = tk.Entry(master,width=60)
            locals()["e%s"%(z)].grid(row=a+3*j+1, column=i);z+=1
            locals()["e%s"%(z)] = tk.Entry(master,width=60)
            locals()["e%s"%(z)].grid(row=a+3*j+2, column=i);z+=1
        elif i==0:
            locals()["e%s"%(z)] = tk.Entry(master,width=5)
            locals()["e%s"%(z)].grid(row=a+3*j, column=i);z+=1
        else:
            locals()["e%s"%(z)] = tk.Entry(master,width=12)
            locals()["e%s"%(z)].grid(row=a+3*j, column=i);z+=1


for i in range(len(QU2)):
    tk.Label(master,
             text=QU2[i]).grid(row=i+24)

    if i==len(QU2)-1:
        for j in range(5):
            v = tk.StringVar(master, value='%s.'%(j+1))
            locals()["e%s"%(z)] = tk.Entry(master,textvariable = v,width=60)
            locals()["e%s"%(z)].grid(row=i+24+j+1, column=1);z+=1
    else:
        locals()["e%s"%(z)] = tk.Entry(master)
        locals()["e%s"%(z)].grid(row=i+24, column=1);z+=1



tk.Button(master,
          text='Clear Cust-info',
          command=cls_info).grid(row=50,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Clear Item',
          command=cls_item).grid(row=50,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Clear Trans-info',
          command=cls_pay).grid(row=50,
                                    column=2,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Export', command=show_entry_fields).grid(row=50,
                                                       column=3,
                                                       sticky=tk.W,
                                                       pady=4)
def key_in():
    tk.mainloop()
#===================================================================================
# print pdf
def prpdf(list):
    fn="{}.pdf".format(list[0])
    c = canvas.Canvas(fn)
    format(c,list)
    write_in_csv(list)
    c.showPage()
    c.save()
#PDF FORMAT
def format(c,list):
    #上欄
    pdfmetrics.registerFont (TTFont ('kaiu', 'C:/Windows/Fonts/kaiu.ttf'))
    pdfmetrics.registerFont (TTFont ('kaiub', 'C:/Windows/Fonts/超世纪粗标楷.ttf'))
    c.setFont("Helvetica", 12)

    c.drawString(30,780, "===================Inc.")

    c.setFont("Helvetica", 8)
    c.drawString(30,750, "Add :========================")
    c.setFont("Helvetica", 12)
    c.drawString(30,730, "Tel : ")
    c.drawString(30,715, "Fax : ")

    #中欄
    c.drawInlineImage("image/tit.png", 230, 680, 90, 20)
    c.drawString(30,670, "To : ")
    c.drawString(30,655, "Attn:")
    c.drawString(30,640, "Tel : ")
    c.drawString(150,640, "ext.")
    c.drawString(30,625, "Fax :")
    c.drawString(360,670, "No : ")
    c.drawString(360,655, "Date :")
    c.line(30,615,500,615)
    c.line(30,614,500,614)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40,600, "No.")
    c.drawString(80,600, "Item")
    c.drawString(280,600, "Q'ty")
    c.drawString(330,600, "Unit")
    c.drawString(375,600, "Unit Price")
    c.drawString(445,600, "Sub-Price")

    c.line(30,595,500,595)
    c.line(30,594,500,594)

    #中欄填入資料=============================================
    #c.setFont("Helvetica-Bold", 12)
    c.setFont('kaiub',12)
    c.drawString(70,670, list[2])
    c.drawString(70,655, list[3])
    c.drawString(70,640, list[4])
    c.drawString(70,625,list[6])
    c.drawString(400,670, list[0])
    c.drawString(400,655, list[1])
    c.drawString(170,640, list[5])

    c.setFont('kaiub',12)
    c.drawString(40,570, list[7])
    c.drawString(80,570, list[8])
    c.drawString(280,570, list[11])
    c.drawString(330,570, list[12])
    c.drawRightString(430,570, list[13])
    c.drawRightString(500,570,list[14])
    c.drawString(40,515, list[15])
    c.drawString(80,515, list[16])
    c.drawString(280,515, list[19])
    c.drawString(330,515, list[20])
    c.drawRightString(430,515, list[21])
    c.drawRightString(500,515,list[22])
    c.drawString(40,460, list[23])
    c.drawString(80,460, list[24])
    c.drawString(280,460, list[27])
    c.drawString(330,460, list[28])
    c.drawRightString(430,460, list[29])
    c.drawRightString(500,460,list[30])
    c.drawString(40,405, list[31])
    c.drawString(80,405, list[32])
    c.drawString(280,405, list[35])
    c.drawString(330,405, list[36])
    c.drawRightString(430,405, list[37])
    c.drawRightString(500,405,list[38])
    c.drawString(40,350, list[39])
    c.drawString(80,350, list[40])
    c.drawString(280,350, list[43])
    c.drawString(330,350, list[44])
    c.drawRightString(430,350, list[45])
    c.drawRightString(500,350,list[46])

    #c.setFont("Helvetica", 10)
    c.setFont('kaiu',10)
    c.drawString(80,555, list[9])
    c.drawString(80,540,list[10])
    c.drawString(80,390, list[33])
    c.drawString(80,375,list[34])
    c.drawString(80,445, list[25])
    c.drawString(80,430,list[26])
    c.drawString(80,500, list[17])
    c.drawString(80,485,list[18])
    c.drawString(80,335, list[41])
    c.drawString(80,320,list[42])

    # 分隔線
    c.line(30,300,500,300)
    c.line(30,299,500,299)
    c.line(30,298,500,298)
    c.line(30,297,500,297)
    # 下欄
    c.setFont("Helvetica", 10)
    c.drawString(30,280, "Payment :")
    c.drawString(30,260, "Validity :")
    c.drawString(30,240, "Delivery :")
    c.drawString(30,220, "Remark :")
    c.drawString(30,100, "If the quotation is accepted, please re confirm with signature.")
    c.drawString(80,70, "Seller :")
    c.setFont("Times-Bold", 16)

    c.setFont("Helvetica", 10)
    c.drawString(320,70, "Accepted by :")
    c.line(115,55,215,55)
    c.line(115,56,215,56)
    c.line(385,55,485,55)
    c.line(385,56,485,56)

    #下欄填入資料=============================================
    c.setFont('kaiu',10)
    c.drawString(80,280, "{} Days".format(list[47]))
    c.drawString(80,260, list[48])
    c.drawString(80,240, list[49])
    c.drawString(80,220, list[50])
    c.drawString(80,200, list[51])
    c.drawString(80,180, list[52])
    c.drawString(80,160, list[53])
    c.drawString(80,140, list[54])
#write in csv file==========================================================
def write_in_csv(list):
    print(list)
    if len(list[8]) != 0 :
        li=[list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[11],list[12],list[13],list[14],list[9],list[10],list[47],list[48],list[49],list[50],list[51],list[52],list[53],list[54]]
        df = pd.DataFrame(li).T
        df.to_csv('Quotation.csv',  mode='a',header=False,index=False,encoding="utf_8_sig")
    if len(list[16]) != 0:
        li=[list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[15],list[16],list[19],list[20],list[21],list[22],list[17],list[18],list[47],list[48],list[49],list[50],list[51],list[52],list[53],list[54]]
        df = pd.DataFrame(li).T
        df.to_csv('Quotation.csv',  mode='a',header=False,index=False,encoding="utf_8_sig")
    if len(list[24]) != 0:
        li=[list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[23],list[24],list[27],list[28],list[29],list[30],list[25],list[26],list[47],list[48],list[49],list[50],list[51],list[52],list[53],list[54]]
        df = pd.DataFrame(li).T
        df.to_csv('Quotation.csv',  mode='a',header=False,index=False,encoding="utf_8_sig")
    if len(list[32]) != 0:
        li=[list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[31],list[32],list[35],list[36],list[37],list[38],list[33],list[34],list[47],list[48],list[49],list[50],list[51],list[52],list[53],list[54]]
        df = pd.DataFrame(li).T
        df.to_csv('Quotation.csv',  mode='a',header=False,index=False,encoding='utf_8_sig')
    if len(list[40]) != 0:
        li=[list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[39],list[40],list[43],list[44],list[45],list[46],list[41],list[42],list[47],list[48],list[49],list[50],list[51],list[52],list[53],list[54]]
        df = pd.DataFrame(li).T
        df.to_csv('Quotation.csv',  mode='a',header=False,index=False,encoding='utf_8_sig')

def search():
    str=('python search_.py')
    p=os.system(str)
    print(p)

    #df[df.colname.isin(['SD','HN'])]
#本體
def run():
    menu(screen)
#=========================================================
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(title)
    run()
