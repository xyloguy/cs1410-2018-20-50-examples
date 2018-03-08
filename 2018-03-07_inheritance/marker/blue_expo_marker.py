import expomarker


class BlueExpoMarker(expomarker.ExpoMarker):
    def __init__(self):
        expomarker.ExpoMarker.__init__(self, (0, 0, 255))
