import numpy as np

def get_refine_bragg_point(data,point_1,point_2):
    """
    :param data:
    :param point_1:
    :param point_2:
    :return:
    """
    lenx,leny = np.shape(data)
    select_area_1 = get_select_area(data,point_1)
    select_area_2 = get_select_area(data,point_2)
    max_point_1 = max_point(select_area_1.empty_bragg)
    max_point_2 = max_point(select_area_2.empty_bragg)
    return max_point_1.max_point, max_point_2.max_point


class get_select_area:

    def __init__(self, data, point_data):
        self.point_data = point_data
        self.data = data
        self.empty_bragg = np.zeros((np.shape(self.data)), dtype=complex)
        self.get_area()

    def get_area(self):
        self.x0 = self.point_data[0]
        self.y0 = self.point_data[2]
        self.x1 = self.point_data[1]
        self.y1 = self.point_data[3]
        for i in range(self.x0, self.x1 + 1):
            for j in range(self.y0, self.y1 + 1):
                self.empty_bragg[j][i] = self.data[j][i]


class max_point:
    # 传入的值是一个复数，我们比较的时候，通过比较其模长
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.max_point = np.empty(2)
        self.max_point = self.return_max_point()

    def return_max_point(self):
        # point 是我们选取的点。点的规格形式为x1,y1,x2,y2
        self.raw_data = np.abs(self.raw_data)
        len_y, len_x = np.shape(self.raw_data)
        index = np.argmax(self.raw_data)
        index_y = int(index / len_y)
        index_x = index - index_y * len_y
        index_x = int(index_x - len_x / 2)
        index_y = int(index_y - len_y / 2)
        print(index_x, index_y)
        return index_x, index_y


