class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        planet_sum = [0] * (len(asteroids) + 1)
        for i in range(len(asteroids)):
            planet_sum[i + 1] = planet_sum[i] + asteroids[i]
        for i in range(len(asteroids)):
            if mass + planet_sum[i] < asteroids[i]:
                return False

        return True
