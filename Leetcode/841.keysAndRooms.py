class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locked = [True] * len(rooms)
        locked[0] = False

        q = deque()
        q.append(0)

        while q:
            next_room = q.popleft()
            # print(next_room)
            for key in rooms[next_room]:
                if locked[key] == True:
                    locked[key] = False
                    q.append(key)

        return all(lock == False for lock in locked)
