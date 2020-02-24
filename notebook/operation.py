
class Matter(object):

    def __init__(self, x_list: List[List[int]]):
        """
        :param x_list: input array in form of List[List[int]] or np.array
        """
        self.value = np.array(x_list)
        self.shape = self.value.shape
        self.placement = [0, 0]
        self.color = -1
        self.background = 0

    def pick_one_color(self, c, background_new=0):
        if self.background == -1:
            self.background = background_new
        x_list_c = np.ones(self.shape, dtype=np.int) * self.background
        x_list_c[self.value == c] = c
        self.color = c
        return Matter(x_list_c)

    def trim_background(self, background_new=0):
        if self.background == -1:
            self.background = background_new
        x_sum = (self.value != self.background).sum(axis=1)
        y_sum = (self.value != self.background).sum(axis=0)
        min_x = min([i for i in range(self.shape[0]) if x_sum[i]])
        max_x = max([i for i in range(self.shape[0]) if x_sum[i]])
        min_y = min([i for i in range(self.shape[1]) if y_sum[i]])
        max_y = max([i for i in range(self.shape[1]) if y_sum[i]])
        self.value = self.value[min_x:max_x + 1, min_y:max_y + 1]
        self.shape = self.value.shape
        self.placement = [min_x, min_y]
        return None

    def fill_background_color(self, c, background_new=0):
        if self.background == -1:
            self.background = background_new
        self.value[self.value == self.background] = c
        return None
