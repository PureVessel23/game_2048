import random
import copy
from model import Location
from model import Direction


class GameCoreController:
    """
        游戏核心控制器
    """
    def __init__(self):
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4,
        ]

        # self.__map = [
        #     [1, 6, 9, 9],
        #     [6, 1, 4, 5],
        #     [3, 5, 3, 8],
        #     [4, 7, 4, 7],
        # ]

        # 用于存储去零合并的列表
        self.__list_merge = []

        # 用于存储空位置的列表
        self.__list_empty_location = []

        # 地图是否发生变化
        self.is_change = False



    @property
    def map(self):
        return self.__map

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def __zero_to_end(self):
        '''
        方法1：
            1.将传入的列表中非零元素拷贝至新列表中
            2.根据零元素数量，在新列表末尾添加零元素
            3.将新列表中的元素赋值给新列表
        方法2：
            删除零元素（最好从后向前删除），在列表末尾添加零元素
            # for i in range(len(list_target)-1, -1, -1):
            #     if list_target[i] == 0:
            #         del list_target[i]
            #         list_target.append(0)
        '''
        new_list = [i for i in self.__list_merge if i]
        new_list += [0] * self.__list_merge.count(0)

        # 错误形式：list_target = new_list
        self.__list_merge[:] = new_list

    def __merge(self):

        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            # 相邻且相同
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.__list_merge[i + 1] = 0

        self.__zero_to_end()

    def __move_left(self):
        for i in self.map:
            self.__list_merge[:] = i
            self.__merge()
            i[:] = self.__list_merge

    def __move_right(self):
        for i in self.map:
            # 从右向左读取元素，并进行合并
            self.__list_merge = i[::-1]
            self.__merge()

            # 从后向前进行赋值，把list_merge中的第一个元素赋值给列表i的最后一个元素，以此类推
            i[::-1] = self.__list_merge

    def __move_up(self):

        for i in range(len(self.map[0])):
            self.__list_merge.clear()

            # 从上向下获取，形成一维列表
            for j in range(len(self.map)):
                self.__list_merge.append(self.map[j][i])
            self.__merge()

            # 将合并后的结果还原给二维列表
            for j in range(len(self.map)):
                self.map[j][i] = self.__list_merge[j]

    def __move_down(self):
        for i in range(len(self.map[0])):
            self.__list_merge.clear()

            for j in range(len(self.map) - 1, -1, -1):
                self.__list_merge.append(self.map[j][i])
            self.__merge()

            for j in range(len(self.map) - 1, -1, -1):
                self.map[j][i] = self.__list_merge[(len(self.map) - 1) - j]
                # map[j][i] = list_merge[abs(j - (len(map)-1))

    def move(self, dir):
        self.is_change = False

        # 移动前记录地图
        original_map = copy.deepcopy(self.map)
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()

        # 移动后对比地图
        self.is_change = self.__equal_map(original_map)

    def __equal_map(self, original):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if original[i][j] != self.map[i][j]:
                    return True
        return False

    def calculate_blank_location(self):
        self.__list_empty_location.clear()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 0:
                    self.__list_empty_location.append(Location(i, j))

    def generate_new_number(self):

        self.calculate_blank_location()

        location = random.choice(self.__list_empty_location)

        self.map[location.x][location.y] = 4 if random.randint(1, 10) == 4 else 2

        self.__list_empty_location.remove(location)


    def is_game_over(self):

        if len(self.__list_empty_location) > 0 :
            return False

        for i in range(len(self.map)):
            for j in range(len(self.map[i]) - 1):
                if self.map[i][j] == self.map[i][j+1]:
                    return False

        for i in range(len(self.map[0])):
            for j in range(len(self.map) - 1):
                if self.map[j][i] == self.map[j + 1][i]:
                    return False

        return True





#     def print_map(self):
#         for i in range(len(self.map)):
#             for j in self.map[i]:
#                 print(j, end=' ')
#             print()
# #
# #
# if __name__ == '__main__':
#
#     a = GameCoreController()
#     if a.game_over():
#         print('a')
#     a.print_map()



