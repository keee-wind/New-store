# 先在相同文件夹内新建一个空白文件

fp = open("text.txt", "w")      # 打开并运用修改模式， "r"是阅读模式
print("学习Python",file = fp)
fp.close()                      # 关闭文件，此时text里就会有这句话