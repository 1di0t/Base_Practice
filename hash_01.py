def solution(nums):
    pokemon = set(nums)

    if len(pokemon) > len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(pokemon)
    return answer


