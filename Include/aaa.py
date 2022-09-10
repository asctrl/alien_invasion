import random
# import platform
# print(platform.architecture())

print('---石头剪刀布游戏开始---')
print('请按下面的提示出拳：')
print('石头【1】剪刀【2】布【3】结束【4】')
while True:
    x = int(input('请输入你的选项：'))
    if x == '4':
        break
    map = {1:'石头', 2:'剪刀', 3:'布'}
    mapp = {1:2, 2:3, 3:1}
    y = random.randint(1, 3)
    print('您的出拳为：'+map.get(x)+', 电脑出拳为：'+ map.get(y), end='   ')
    if mapp.get(x) == y:
        print('您赢了！')
    elif x == y:
         print('平局')
    else:
        print('您输了。')




