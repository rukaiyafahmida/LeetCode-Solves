class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:  # Asteroid moving left and previous asteroid moving right
                if abs(asteroid) > stack[-1]:  # Current asteroid destroys the previous one
                    stack.pop()
                elif abs(asteroid) == stack[-1]:  # Both asteroids destroy each other
                    stack.pop()
                    break
                else:  # Previous asteroid destroys the current one
                    break
            else:
                stack.append(asteroid)
        
        return stack
