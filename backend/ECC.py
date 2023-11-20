import time

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_point_on_curve(self, point):
        if point is None:
            return True  # Point at infinity
        x, y = point
        return (y**2) % self.p == (x**3 + self.a * x + self.b) % self.p

    def point_add(self, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        if p1 != p2:
            m = ((y2 - y1) * pow(x2 - x1, -1, self.p)) % self.p
        else:
            m = ((3 * x1**2 + self.a) * pow(2 * y1, -1, self.p)) % self.p

        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p

        return x3, y3

    def point_double(self, p):
        return self.point_add(p, p)

    def scalar_multiply(self, k, point):
        if k == 0 or point is None:
            return None

        result = None
        for bit in bin(k)[2:]:
            result = self.point_double(result)
            if bit == '1':
                result = self.point_add(result, point)
        return result
    
    def count_points(self):
        count = 0
        for x in range(self.p):
            for y in range(self.p):
                if (y**2 - x**3 - self.a*x - self.b) % self.p == 0:
                    count += 1
        return count

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    start = time.time()
    count = 0
    prime_number = [num for num in range(1, 251) if is_prime(num)]
    with open('output.txt', 'w') as file:
        for a in range(1,5):
            for b in range(1,101):
                for p in prime_number:
                    if p>a and p>b:
                        curve = EllipticCurve(a, b, p)
                        num_points = curve.count_points()
                        if num_points >= 221 and is_prime(num_points):
                            count += 1
                            result_str = f"The number of points on the elliptic curve of ({a}, {b}, {p}) is approximately: {num_points}\n"
                            #print(result_str, end='')  # Print to console
                            file.write(result_str)  # Write to file
    print("Total case is : ", count)
    end = time.time()
    print(f"Eclapsed time: {end-start}")

if __name__ == "__main__":
    main()