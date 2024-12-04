import random
def make_list():
    nums = []
    for _ in range(10):
        num = random.randint(1, 100)
        nums.append(num)
    return nums
def print_min_max(nums):
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    print("Минимальное значение:", min_num)
    print("Максимальное значение:", max_num)
def print_sum(nums):
    total = 0
    for num in nums:
        total += num
    print("Сумма всех чисел в списке:", total)
def main():
    nums = make_list()
    print("Сгенерированный список:", nums)
    print_min_max(nums)
    print_sum(nums)
main()
