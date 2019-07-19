#coding=utf-8
import itchat
from tuling import get_response
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import random
import time

def return_img(Ask_text,user_name):
    current_ask_Y = 517;current_ans_Y = 635
    num = random.randint(1, 5) 
    img_PIL = Image.open(str(num)+'.png')
    Ans_text = get_response(Ask_text)
    font = ImageFont.truetype('C:\WINDOWS\FONTS\HANYINUOMITUAN-W-2.TTF', 48)
    draw = ImageDraw.Draw(img_PIL)
    while len(Ask_text):
        draw.text((120,current_ask_Y), Ask_text[:8], font=font, fill=(255,255,255))
        Ask_text=Ask_text[8:]
        current_ask_Y += 40
    while len(Ans_text):  
        draw.text((120,current_ans_Y), Ans_text[:8], font=font, fill=(255,255,255))
        Ans_text=Ans_text[8:]
        current_ans_Y += 40
    draw.text((282.5-22.5*len(user_name),420), user_name, font=font, fill=(255,255,255))
    save_file_name = str(int(time.time()))+'_'+str(random.randint(1, 10000))+'.jpg'
    plt.imsave('./tmp/'+save_file_name,img_PIL)
    return './tmp/'+save_file_name

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        print(msg['User']['UserName'])
        print('\n')
        if len(msg['Content'])<=5:
            return msg['ActualNickName']+', 请在@后添加聊天内容'
        f = return_img(msg['Content'][5:],msg['ActualNickName'])
        print(msg['Content'][5:])
        return itchat.send_image(f,toUserName=msg['User']['UserName'])

itchat.auto_login(True, enableCmdQR=True)
itchat.run()