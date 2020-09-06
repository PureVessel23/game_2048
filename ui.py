from bll import GameCoreController
from model import Direction

class GameView:
    """
        控制台视图
    """


    def __init__(self):
        self.__controller = GameCoreController()

    def __print_map(self):

        for i in range(len(self.__controller.map)):
            for j in self.__controller.map[i]:
                print(j, end='\t')
            print()

    def start(self):
        """
            游戏开始
        """
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def move_map(self):
        dir = input('请输入移动方向（wasd）：')
        if dir == 'w':
            self.__controller.move(Direction.up)
        elif dir == 'a':
            self.__controller.move(Direction.left)
        elif dir == 's':
            self.__controller.move(Direction.down)
        elif dir == 'd':
            self.__controller.move(Direction.right)

    def update(self):
        """
            更新游戏逻辑
        :return:
        """
        while True:


            self.move_map()

            if self.__controller.is_change:
                self.__controller.generate_new_number()
                self.__print_map()

            if self.__controller.is_game_over():
                print('Game Over')
                break



