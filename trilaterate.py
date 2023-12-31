
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
