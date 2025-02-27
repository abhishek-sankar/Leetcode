class Solution:
    def countAndSay(self, n: int) -> str:
        rle = "1"
        if n == 1:
            return rle

        def getRLE(n):
            if n == 1:
                return "1"
            prevRle = getRLE(n - 1)
            count = 1
            rle = ""
            i = 0
            while i < len(prevRle):
                while i + 1 < len(prevRle) and prevRle[i] == prevRle[i + 1]:
                    count += 1
                    i += 1
                # if i == len(prevRle) - 1:
                #     count += 1
                rle += f"{count}{prevRle[i]}"
                count = 1
                i += 1

            # print(n, rle)
            return rle

        return getRLE(n)
