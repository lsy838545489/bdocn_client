# 黑色沙漠汉化工具客户端

汉化目标群体是Steam的黑色沙漠美服/欧服，但按理其他区域（比如：韩服，日服，大洋，俄服等）应该都能用，但并未测试过。如果有测试过可行的同学可以发个issue。

![image](./images/cn1.PNG)

# 使用方法
## 1. 使用客户端安装汉化补丁
1. 下载最新版本(Latest release)的[`bdocn_client.exe`](https://github.com/BDO-CnHope/bdocn_client/releases)
2. 正确的选择黑沙的游戏目录
3. 按指示完成汉化补丁的安装
## 2. 手动安装汉化补丁
1. 前往[黑沙汉化语言包](https://github.com/BDO-CnHope/bdocn)
2. 打包下载`ads`和`prestringtable`这两个文件夹
3. 找到你本地的黑沙的游戏根目录
4. 将下载的两个文件夹覆盖到目录
## 3. 手动编译客户端安装汉化补丁
1. 安装`python`环境
2. 安装`pyinstaller`
3. 下载`https://github.com/BDO-CnHope/bdocn_client/tree/main/src/py`里的文件包
4. 通过终端执行命令`pyinstaller.exe --clean -F -p .\ -i .\logo_og_han.ico .\run.py`
5. 在`dist`下能找到打包好的执行文件
## 4. 使用旧版的客户端
1. 旧版的客户端是使用`powershell`写的，然后打包成exe可执行文件
2. 已不再维护，但应该还能用
3. https://github.com/BDO-CnHope/bdocn_client/tree/main/src/ps

# Update
### 20210317
更新版本: 2021031403
- 详细请看 [#7](https://github.com/BDO-CnHope/bdocn_client/issues/7)

### 20210206
- 添加新功能: 不覆盖现有字体文件. [issue #2](https://github.com/BDO-CnHope/bdocn_client/issues/2)

# issue
- 如有问题请开issue提问，比如发现有乱码或者显示不正确等问题。
- 或者加Q群(不定时回复): 104039903

# 声明
- 本软件和代码仅供学习交流，如作他用所承受的法律责任一概与作者无关！

# 相关链接
- [bdocn](https://github.com/BDO-CnHope/bdocn)
- [bdocn_client](https://github.com/BDO-CnHope/bdocn_client)
- [黑沙汉化语言包](https://gitee.com/bdo-cnhope/bdocn)
- [黑沙汉化工具客户端](https://gitee.com/bdo-cnhope/bdocn_client)

