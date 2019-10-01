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
Successfully navigated to building windows.

Original green channel:  [153, 132, 153, 140, 132, 147, 145, 143, 154]
Current green channel:   [153, 131, 153, 141, 130, 149, 146, 142, 153]
Zero or multiple available targets found for cargo 1. Abandoned.

Original green channel:  [153, 132, 153, 140, 132, 147, 145, 143, 154]
Current green channel:   [153, 132, 153, 142, 131, 148, 146, 143, 154]
Zero or multiple available targets found for cargo 2. Abandoned.

Original green channel:  [153, 132, 153, 140, 132, 147, 145, 143, 154]
Current green channel:   [153, 132, 153, 143, 130, 149, 146, 143, 154]
Zero or multiple available targets found for cargo 3. Abandoned.

Policy available. Begin updating policy.
Developing...

No new hongbao or album found.

Cycle 1 finished. Sleep for some time to start new cycle.

Successfully navigated to building windows.

Original green channel:  [153, 132, 153, 143, 132, 149, 145, 143, 155]
Current green channel:   [154, 132, 154, 145, 133, 148, 147, 146, 191]
Building 9 is the target. Begin transporting...

Original green channel:  [153, 132, 153, 143, 132, 149, 145, 143, 155]
Current green channel:   [155, 133, 155, 184, 135, 149, 148, 147, 154]
Building 4 is the target. Begin transporting...

Original green channel:  [153, 132, 153, 143, 132, 149, 145, 143, 155]
Current green channel:   [154, 135, 187, 144, 134, 152, 149, 144, 156]
Building 3 is the target. Begin transporting...

Policy available. Begin updating policy.
Developing...

No new hongbao or album found.

Cycle 2 finished. Sleep for some time to start new cycle.

Successfully navigated to building windows.

Original green channel:  [153, 131, 153, 142, 132, 149, 145, 143, 155]
Current green channel:   [155, 133, 155, 145, 134, 150, 184, 144, 155]
Building 7 is the target. Begin transporting...

Original green channel:  [153, 131, 153, 142, 132, 149, 145, 143, 155]
Current green channel:   [155, 134, 154, 146, 176, 150, 147, 146, 159]
Building 5 is the target. Begin transporting...

Original green channel:  [153, 131, 153, 142, 132, 149, 145, 143, 155]
Current green channel:   [153, 132, 153, 143, 132, 147, 146, 144, 155]
Zero or multiple available targets found for cargo 3. Abandoned.

Policy available. Begin updating policy.
Developing...

No new hongbao or album found.

Cycle 3 finished. Sleep for some time to start new cycle.

......
```

**加速版**

![](img/accelerated.gif)

**常速版**

由于文件过大，故用了外链，点击下载。

https://yusanshi.com/jgm.gif
