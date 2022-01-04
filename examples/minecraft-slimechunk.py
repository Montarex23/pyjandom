# find seed with slime chunk at 0 0

from pyjandom import Random

def slimechunk(seed, xpos, zpos):
    rand = Random(
        seed + 
        (xpos * xpos * 4987142) +
        (xpos * 5947611) +
        (zpos * zpos) * 4392871 +
        (zpos * 389711) ^ 987234911
    )
    if rand.nextInt(10) == 0:
        return True
    else:
        return False

seed = 0
while True:
    seed += 1
    if slimechunk(seed, 0, 0):
        print(seed)
        break
