class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 1 划分n步骤
        amount_array = [0] * (amount + 1)
        amount_Mehthod = [[]] * (amount + 1)
        for i in range(amount + 1):
            amount_array[i] = i
            amount_Mehthod[i] = []
            # 2 每步m种选择:
            for select in coins:
                ##3 状态转移方程:
                if select <= i and i - select >= 0:
                    new_count = amount_array[i - select] + 1
                    if new_count < amount_array[i]:
                        amount_array[i] = new_count
                        amount_Mehthod[i].clear()
                        amount_Mehthod[i].append(select)
        ii = amount
        while ii > 0:
            select = amount_Mehthod[ii][0]
            print(select, end=",")
            ii = ii - select
        print()
        return amount_array[amount]


if __name__ == '__main__':
    base_coins = [1, 2, 5, 10]
    print(Solution().coinChange(base_coins, 23))
    for  i in range(1,11,2):
        print(i)
