
class Solution:
    def __init__(self):
        self.len_row = -1
        self.len_col = -1

    def does_exists(self, index: tuple):
        if 0 <= index[0] <= self.len_row and 0 <= index[1] <= self.len_col:
            return True
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n_row = len(img)
        n_col = len(img[0])
        self.len_row = n_row-1
        self.len_col = n_col-1
        temp = [x[:] for x in img]

        for i in range(n_row):
            for j in range(n_col):
                count = 1
                sums = img[i][j]
                up = (i - 1, j)
                down = (i + 1, j)
                left = (i, j - 1)
                right = (i, j + 1)
                up_left = (i - 1, j - 1)
                up_right = (i - 1, j + 1)
                down_left = (i + 1, j - 1)
                down_right = (i + 1, j + 1)
                if self.does_exists(up):
                    sums += img[up[0]][up[1]]
                    count += 1
                if self.does_exists(down):
                    sums += img[down[0]][down[1]]
                    count += 1
                if self.does_exists(left):
                    sums += img[left[0]][left[1]]
                    count += 1
                if self.does_exists(right):
                    sums += img[right[0]][right[1]]
                    count += 1
                if self.does_exists(up_left):
                    sums += img[up_left[0]][up_left[1]]
                    count += 1
                if self.does_exists(up_right):
                    sums += img[up_right[0]][up_right[1]]
                    count += 1
                if self.does_exists(down_left):
                    sums += img[down_left[0]][down_left[1]]
                    count += 1
                if self.does_exists(down_right):
                    sums += img[down_right[0]][down_right[1]]
                    count += 1
                temp[i][j] = sums//count

        return temp
