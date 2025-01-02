class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for asteroid in asteroids:
            # print(asteroid)
            while stack and asteroid < 0 < stack[-1]:
                # print("Inside", asteroid)
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return list(stack)
