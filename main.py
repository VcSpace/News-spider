from wangyi_fiance import WangYi
from TongHuaShun import TongHua
import os, shutil
import time

def filemove():
    filename = "C:\\Users\\Vcvc\\Desktop\\News_Finance.xlsx"

    path = "C:\\Users\\Vcvc\\Desktop\\Finance\\"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) #year-month-day-hour-minute
    path2 = path + "闻讯__" + filetime + ".xlsx"
    shutil.move(filename, path2)


def Wy():
    Wy = WangYi()
    Wy.main()

def THS():
    Th = TongHua()
    Th.main()

if __name__ == '__main__':
    Wy() #网易财经
    THS() #同花顺财经
    filemove()
    print("操作完成")
