import utm


def metres_to_degrees(metres):
    # 1 degree = 111 km
    return metres / 111000


def trilaterate(p1, p2, p3, r1, r2, r3):
    """2D coordinate trilateration"""

    # Thanks to 101computing for doing all the maths for me :D
    # https://www.101computing.net/cell-phone-trilateration-algorithm/

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    A = -2 * x1 + 2 * x2
    B = -2 * y1 + 2 * y2
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2

    D = -2 * x2 + 2 * x3
    E = -2 * y2 + 2 * y3
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

    x = (C * E - F * B) / (E * A - B * D)

    y = (C * D - A * F) / (B * D - A * E)

    return (x,y)


def earth_trilaterate(p1, p2, p3, r1, r2, r3, utm_zone=30, utm_letter='U'):
    # cause the earth is round we need to map it to flat
    # coordinates using the UTM projection

    x1, y1, _, _ = utm.from_latlon(*p1)
    x2, y2, _, _ = utm.from_latlon(*p2)
    x3, y3, _, _ = utm.from_latlon(*p3)

    # convert metres to degrees
    r1 = metres_to_degrees(r1)
    r2 = metres_to_degrees(r2)
    r3 = metres_to_degrees(r3)

    return utm.to_latlon(*trilaterate((x1, y1), (x2, y2), (x3, y3), r1, r2, r3), utm_zone, utm_letter)
