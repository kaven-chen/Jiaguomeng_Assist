# Jaiguomeng Assistor

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

演示时终端的输出（只运行了一个 cycle）：

```
C:\Users\Yu\Documents\GitHub\Jiaguomeng_Assist>python main.py
/sdcard/building.png: 1 file pulled. 3.3 MB/s (2348628 bytes in 0.685s)
/sdcard/shop.png: 1 file pulled. 3.2 MB/s (1020512 bytes in 0.305s)
/sdcard/current.png: 1 file pulled. 3.0 MB/s (2354959 bytes in 0.759s)
current.png and building.png similarity 0.959490981867284
/sdcard/temp_not_pressed.png: 1 file pulled. 2.4 MB/s (2349754 bytes in 0.939s)
/sdcard/temp_pressed.png: 1 file pulled. 2.3 MB/s (2385693 bytes in 0.999s)
Original green channel:  [152, 131, 160, 135, 141, 144, 155, 135, 146]
Current green channel:   [154, 129, 161, 178, 145, 146, 158, 139, 147]
Building 4 is the target. Begin transporting...

/sdcard/temp_pressed.png: 1 file pulled. 3.4 MB/s (2367288 bytes in 0.662s)
Original green channel:  [152, 131, 160, 135, 141, 144, 155, 135, 146]
Current green channel:   [194, 132, 162, 138, 148, 145, 158, 136, 148]
Building 1 is the target. Begin transporting...

/sdcard/temp_pressed.png: 1 file pulled. 3.4 MB/s (2330202 bytes in 0.659s)
Original green channel:  [152, 131, 160, 135, 141, 144, 155, 135, 146]
Current green channel:   [153, 131, 160, 132, 143, 144, 156, 134, 145]
No available target found for cargo 3.

/sdcard/temp.png: 1 file pulled. 3.6 MB/s (2338479 bytes in 0.620s)
Found new hongbao or album.
/sdcard/current.png: 1 file pulled. 3.2 MB/s (1041396 bytes in 0.306s)
current.png and shop.png similarity 0.884136043595679
/sdcard/current_shop.png: 1 file pulled. 3.3 MB/s (1028167 bytes in 0.293s)
Hongbao 1 BGR:  [144, 194, 125]
Hongbao 1 is available.

Hongbao 2 BGR:  [137, 190, 117]
Hongbao 2 is available.

Hongbao 3 BGR:  [157, 196, 223]
Hongbao 3 is not available.

Album BGR:  [188, 207, 177]
Album is not available.
Cycle finished. Sleep for some time to start new cycle.
```

**加速版**

![](img/accelerated.gif)

**常速版**

由于文件过大，故用了外链，点击下载。

https://yusanshi.com/jgm.gif
