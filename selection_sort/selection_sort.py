def selection_sort(unsorted_arr: list) -> list:
    sorted_arr: list = []
    for i in range(len(unsorted_arr)):
        smallest_item_index = get_smallest_item_index(unsorted_arr)
        sorted_arr.append(unsorted_arr.pop(smallest_item_index))
    return sorted_arr


def get_smallest_item_index(unsorted_arr: list) -> int:
    smallest_item_index = 0
    for i in range(len(unsorted_arr)):
        if (unsorted_arr[i] < unsorted_arr[smallest_item_index]):
            smallest_item_index = i
    return smallest_item_index
