# Jiaguomeng Assistor

> 使用 Python 和 Adb 工具编写的《家国梦》辅助脚本，能够自动收集金币、升级建筑、运输货物、点击商店中的红包和相册。本脚本中自带的配置文件仅用于分辨率为 1080P 的设备。


- [x] 自动检测货物的目的地，而不是无脑循环点击；
- [x] 自动检测新的红包或相册，而不是无脑循环点击；
- [x] 点击红包或相册时，自动选择目标，而不是无脑循环点击；
- [ ] 自动升级政策；
- [ ] 升级建筑时，检测升级的反馈信息，若已经没有金钱则立即停止点击。

## 运行

1. 配置 Adb 环境；
2. 若你的设备分辨率不是 1080P，请使用安卓模拟器（推荐夜神模拟器或 Genymotion）直接设定这个分辨率；
3. 连接手机或者打开模拟器，`python main.py`运行主程序。

> 本脚本具有一定的防检测功能。

## 示例

使用了夜神模拟器，设置了竖屏显示、分辨率 1080P。游戏版本 V1.2.3。

终端输出：

```
C:\Users\Yu\Documents\GitHub\Jiaguomeng_Assist>python main.py
Successfully navigated to building window.

Begin collecting money.

Begin upgrading building.

Try transporting goods.

Original green channel:  [145, 119, 151, 143, 136, 141, 130, 138, 152]
Current green channel:   [153, 120, 150, 143, 136, 141, 127, 137, 153]
Zero or multiple available targets found for cargo 1. Abandoned.

Original green channel:  [145, 119, 151, 143, 136, 141, 130, 138, 152]
Current green channel:   [153, 121, 151, 141, 134, 140, 130, 137, 153]
Zero or multiple available targets found for cargo 2. Abandoned.

Original green channel:  [145, 119, 151, 143, 136, 141, 130, 138, 152]
Current green channel:   [145, 117, 151, 141, 136, 141, 130, 138, 153]
Zero or multiple available targets found for cargo 3. Abandoned.

Policy available. Begin updating policy.
In developing...

No new hongbao or album found.

Cycle 1 finished. Sleep for some time to start new cycle.

Successfully navigated to building window.

Begin collecting money.

Begin upgrading building.

Try transporting goods.

Original green channel:  [144, 119, 150, 143, 135, 142, 130, 138, 153]
Current green channel:   [152, 121, 150, 143, 137, 142, 130, 137, 153]
Zero or multiple available targets found for cargo 1. Abandoned.

Original green channel:  [144, 119, 150, 143, 135, 142, 130, 138, 153]
Current green channel:   [145, 119, 150, 142, 137, 142, 127, 136, 152]
Zero or multiple available targets found for cargo 2. Abandoned.

Original green channel:  [144, 119, 150, 143, 135, 142, 130, 138, 153]
Current green channel:   [145, 119, 151, 143, 136, 141, 130, 138, 153]
Zero or multiple available targets found for cargo 3. Abandoned.

Policy available. Begin updating policy.
In developing...

No new hongbao or album found.

Cycle 2 finished. Sleep for some time to start new cycle.

Successfully navigated to building window.

Begin collecting money.

Begin upgrading building.

Try transporting goods.

Original green channel:  [145, 118, 151, 142, 139, 141, 130, 137, 153]
Current green channel:   [152, 121, 151, 142, 137, 141, 130, 136, 152]
Zero or multiple available targets found for cargo 1. Abandoned.

Original green channel:  [145, 118, 151, 142, 139, 141, 130, 137, 153]
Current green channel:   [145, 119, 150, 143, 132, 140, 130, 136, 152]
Zero or multiple available targets found for cargo 2. Abandoned.

Original green channel:  [145, 118, 151, 142, 139, 141, 130, 137, 153]
Current green channel:   [145, 119, 151, 140, 137, 141, 129, 137, 153]
Zero or multiple available targets found for cargo 3. Abandoned.

Policy available. Begin updating policy.
In developing...

No new hongbao or album found.

Cycle 3 finished. Sleep for some time to start new cycle.

......
```

**加速版**

![](img/accelerated.gif)

**常速版**

由于文件过大，故用了外链，点击下载。

https://yusanshi.com/jgm.gif

## 补充

> 也可以只用手机、脱离电脑（即在手机上让该脚本在后台运行、游戏在前台运行）。

基本思路：使用 Termux 运行脚本，在 Termux 中配置好 Python、~~OpenCV~~、Pillow、Adb 等。

### 旧方案

- 安装 Termux；
- 在 Termux 安装配置 NumPy、~~OpenCV~~、Pillow 等包，其中 OpenCV [这样安装](https://wiki.termux.com/wiki/Instructions_for_installing_python_packages#opencv)，而 Pillow 依赖的库在以上安装 OpenCV 的过程已经安装了，因此先安装完 OpenCV，直接 Pip 安装 Pillow 即可；
- 配置 Adb：https://github.com/MasterDevX/Termux-ADB。

> 由于 Termux 上安装 OpenCV 这个过程太艰难，我放弃了。故我把程序简单改了一下，不再使用 OpenCV，而是只用 Pillow。

### 新方案

#### 配置

```
pkg install wget && wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh && bash InstallTools.sh

pkg install clang libjpeg-turbo
pip install Pillow numpy

git clone https://github.com/yusanshi/Jiaguomeng_Assist
```

#### 运行
```
cd Jiaguomeng_Assist

su
sh adb_tcp.sh
exit

adb connect localhost:5555 # Touch "allow" if this is a dialog.
adb devices # Make sure localhost is in list and is the only one.

python main.py --off_PC=True

# after ending manually
su
sh adb_usb.sh
exit
```

