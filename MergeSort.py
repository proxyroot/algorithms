__author__ = 'Afroze Khan'
__created__ = '11/14/2016'

class MergeSort(object):
    """docstring for MergeSort"""
    def __init__(self, arr):
        super(MergeSort, self).__init__()
        self.arr = arr

    def merge(self, arr1, arr2):
        """
        type arr1: list
        type arr2: list
        rtype: list
        """
        i = 0
        j = 0
        res = []
        while i != len(arr1) and j != len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                res.append(arr2[j])
                i += 1
                j += 1
        res += arr1[i:] + arr2[j:]
        return res

    def sort(self):
        if len(self.arr)<=1:
            return self.arr
        self.arr = [[i] for i in self.arr]
        while len(self.arr) > 1:
            modified_arr = []
            for i in range(0, len(self.arr)-1, 2):
                modified_arr.append(self.merge(self.arr[i], self.arr[i+1]))
            # Check for odd array
            if len(self.arr)%2 != 0:
                modified_arr.append(self.arr[-1])
            self.arr = modified_arr
        return self.arr[0]

arr = [12, 11, 13, 5, 6, 7]
o = MergeSort(arr)
print o.sort()
arr = []
o = MergeSort(arr)
print o.sort()
arr = [12]
o = MergeSort(arr)
print o.sort()

# output:
# [5, 6, 7, 11, 12, 13]
# []
# [12]
