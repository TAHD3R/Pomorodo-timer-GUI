# Pomorodo-timer-GUI 以Pyside6为界面库的图形化番茄钟

This is pomorodo clock using python&amp;pyside6, this is my practise project.
本项目是Python&PySide6构建的番茄钟软件，这是一个练习项目。

## Overview 总览
After learning the introductory and advanced Python tutorials, I think I need to consolidate what I have learned with projects and create practical software that can effectively improve my programming skills
在学习完Python的入门和进阶教程后，我认为我需要用项目来巩固已学内容，制作实用软件能够有效的提高我的编程能力

Before starting the project, I constructed a mind map of the project and intended to use it to implement the functions in steps, the mind map is as follows.
在开始项目前，我构建了该项目的思维导图，打算以此分步骤实现各功能，思维导图如下：

[![j8WxRP.png](https://s1.ax1x.com/2022/07/03/j8WxRP.png)]

The software runs with the following interface:
软件运行时界面如下：
[![j8fZR0.png](https://s1.ax1x.com/2022/07/03/j8fZR0.png)]

## Features not implemented in the current version 当前版本未实现功能
- Read and write software config 读写配置文件
- Nap break length customization 休息时长自定义
- Show tomato count 显示番茄次数

## 各版本反馈
Version 1 completion feedback 第一版完成反馈：
Implemented the most basic timing function, but using the sleep instruction, during which the program has no way to perform other operations, while needing to implement the time countdown, multi-threading, interface, configuration file storage and other functions. Now start learning PyQt to implement the graphical interface.
实现了最基础的定时功能，但是使用的是sleep指令，在这期间程序没办法进行其他操作，同时需要实现时间倒计时、多线程、界面、配置文件储存等功能。现在开始学习PyQt实现图形化界面。

Version 2 completion feedback 第二版完成反馈：
Basically completed the core functions of the tomato clock, the implementation of multi-threaded execution of the countdown, Qt implementation of the GUI, the basic logic vulnerabilities have been fixed. To add features: interface beautification, settings interface, configuration file storage, record the number of tomatoes, nap break function.
基本完成了番茄钟核心功能，实现了多线程执行倒计时，Qt实现GUI，基本逻辑漏洞都已修补完毕。待添加功能：界面美化、设置界面、配置文件储存、记录番茄次数、小憩休息功能。

## 项目依赖
Python 3.7+
Pyside6(pip install pyside6)
Qt material(pip install qt_material)
Playsound(pip install playsound)

## Notice 提示
This is my first independent project, the code may not be so good, if you have guidance or advice can leave a message, thanks for your support!
这是我第一次独立编写项目，代码可能不是那么好，如果你们有指导或者建议可以留言，感谢支持！
