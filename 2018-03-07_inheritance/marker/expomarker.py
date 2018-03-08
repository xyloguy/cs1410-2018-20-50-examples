import marker


class ExpoMarker(marker.Marker):
    def __init__(self, color):
        marker.Marker.__init__(self, color, 4.8, 0.01, True)