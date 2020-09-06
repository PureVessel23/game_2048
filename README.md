2048游戏规则：
    游戏运行，在 4 * 4 的方格中出现两个随机的数字
    产生随机数的策略：10% 的概率是 4，90% 的概率是 2
    用户移动方格（wasd），方格内数字按照相应的规则进行合并
    如果地图有变化（数字移动/数字合并），再产生 1 个随机数
    游戏结束：数字不能合并，也没有空白位置

架构：
    逻辑处理模块
    界面视图模块（控制台/pygame/...）
    数据模型模块
    程序入口模块

步骤：
    逻辑处理模块
        创建游戏核心类 GameCoreController
            核心算法
            在空白位置产生新数字
    界面视图模块
        创建游戏核心类对象
        调用核心类对象的生成数字方法
        while True:
            呈现界面
            获取用户输入，调用核心类对象的移动方法
            产生随机数
