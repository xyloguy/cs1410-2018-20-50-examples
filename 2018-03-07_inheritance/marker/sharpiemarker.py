from marker import Marker


class SharpieMarker(Marker):
    def __init__(self, color):
        Marker.__init__(self, color, 3, 0.005, False)


if __name__ == '__main__':
    red_sharpie = SharpieMarker((255, 0, 0))
    red_sharpie.set_owner('Bob')
    print(red_sharpie.write(), red_sharpie.color, red_sharpie.tip, red_sharpie.owner)
