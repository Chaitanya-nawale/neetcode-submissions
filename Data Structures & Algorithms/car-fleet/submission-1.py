class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev_time = -1
        fleet_count = 0
        for pos, speed in sorted(zip(position, speed), reverse=True):
            total_time = (target - pos) / speed
            if prev_time < total_time:
                prev_time = total_time
                fleet_count += 1
        return fleet_count

        