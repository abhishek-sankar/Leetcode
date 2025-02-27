class Solution:
    def candy(self, ratings: List[int]) -> int:
        total_candy = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and total_candy[i] <= total_candy[i - 1]:
                total_candy[i] = total_candy[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and total_candy[i] <= total_candy[i + 1]:
                total_candy[i] = total_candy[i + 1] + 1

        return sum(total_candy)
