class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        currentmass = mass
        for asteroidmass in asteroids:
            if asteroidmass > currentmass:
                return False
            currentmass += asteroidmass
        return True
