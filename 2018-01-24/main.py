import random

from marker import Marker
from battery import Battery

# bluemarker = Marker('blue')
# greenmarker = Marker('green')
# blackmarker = Marker('black')
# bluemarker2 = Marker('blue')
#
#
# bluemarker.ink = 5
# bluemarker.print()
# bluemarker.write(25)
# bluemarker.print()
#
# blackmarker.write(999)
# blackmarker.print()

ankerPowerBank = Battery(10000, True)
n18650 = Battery(2200, True)
AA = Battery(1200, False)

batteries = [ankerPowerBank, n18650, AA]
for b in batteries:
    amount = random.randrange(0, 10000)
    print(amount)
    b.discharge(amount)
    print(b.capacity)
    b.charge(amount//2)
    print(b.capacity)
    print()
