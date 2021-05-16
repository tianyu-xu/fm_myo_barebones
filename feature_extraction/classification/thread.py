#coding=utf-8
import time
# from selenium import webdriver
import threading
import os


def maze():
    os.system('python D:/FinalProject/codes/fm_myo_barebones/game/maze_main.py')

def cursor():
    os.system('python D:/FinalProject/codes/fm_myo_barebones/feature_extraction/classification/3_cursor.py')

threads = []
threads.append(threading.Thread(target=maze))
threads.append(threading.Thread(target=cursor))

print(threads)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        # 我拿来做selenium自动化模拟多个用户使用浏览器的时候，加了这个就启动不了，要去掉，原因找到了:
        # 加了这个是说明 主线程 执行完了 子线程也停止(无论是否执行完毕)
        t.start()

    t.join()
    # print("all over %s" %ctime())
