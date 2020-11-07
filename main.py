from wangyi_fiance import WangYi
from TongHuaShun import TongHua
import os, shutil
import time
import platform

"""
def pip_install(platform):
    file_name = "library.txt"
    if platform:
        import os
        os.system("pip install" + )
        import requests
"""

def get_platform():
    sys = platform.system()
    if sys == "Windows":
        return True
    elif sys == "Linux":
        return False

def file_move(platform):
    if platform:
        win_filemove()
    else:
        linux_filemove()

def linux_filemove():
    path = "./Finance"
    filename = "./News_Finance.xlsx"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
    path2 = path + "/" +"闻讯__" + filetime + ".xlsx"
    shutil.move(filename, path2)


def win_filemove():
    desktop_path = os.path.join(os.path.expanduser('~'),"Desktop") #获取桌面路径
    filename = desktop_path + "\\News_Finance.xlsx"
    path = desktop_path +"\\Finance\\"

    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) #year-month-day-hour-minute
    path2 = path + "闻讯__" + filetime + ".xlsx"
    shutil.move(filename, path2)


def Wy(filename):
    Wy = WangYi(filename)
    Wy.main(filename)

def THS(filename):
    Th = TongHua(filename)
    Th.main(filename)

def get_News(platform, win_file, lin_file):
    if platform:
        Wy(win_file)
        THS(win_file)
    else:
        Wy(lin_file)
        THS(lin_file)


if __name__ == '__main__':
    desktop_path = os.path.join(os.path.expanduser('~'),"Desktop") #获取桌面路径
    win_file = desktop_path + "\\News_Finance.xlsx"
    linux_file = "./News_Finance.xlsx"

    m_platform = get_platform() #判断系统 win/linux 设置配置
    #pip_install(m_platform) 以后添加
    get_News(m_platform, win_file, linux_file)
    file_move(m_platform)

    print("操作完成")
