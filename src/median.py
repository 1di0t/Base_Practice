def solution(array):
    len_of_array = len(array)
    for i in range(len_of_array):
        for j in range(i+1, len_of_array):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    answer = array[len//2+1]
    return answer