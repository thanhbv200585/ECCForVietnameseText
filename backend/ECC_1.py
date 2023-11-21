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

        if x1 == x2 and y1 != y2:
            return -1, -1
        if p1 != p2:
            m = ((y2 - y1) * pow(x2 - x1, -1, self.p)) % self.p
        if p1 == p2 and 2*y1 % self.p != 0:
            m = ((3 * x1**2 + self.a) * pow(2 * y1, -1, self.p)) % self.p
        else:
            return -1, -1
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

    def find_generator_point(self):
        for x in range(self.p):
            for y in range(self.p):
                if (y**2 - x**3 - self.a*x - self.b) % self.p == 0:
                    return (x, y)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(curve):
    list_char = "aàãảáạăằẵẳắặâầẫẩấậbcdđeèẽẻéẹêềễểếệfghiìĩỉíịklmnoòõỏóọôồỗổốộơờỡởớợpqrstuùũủúụưừữửứựvxyỳỹỷýỵzAÀÃẢÁẠĂẰẴẲẮẶÂẦẪẨẤẬBCDĐEÈẼẺÉẸÊỀỄỂẾỆFGHIÌĨỈÍỊKLMNOÒÕỎÓỌÔỒỖỔỐỘƠỜỠỞỚỢPQRSTUÙŨỦÚỤƯỪỮỬỨỰVXYỲỸỶÝỴZ 0123456789 .,;?!@$%^&-+()[]{}=|<>‘:"
    list_point = []
    G = curve.find_generator_point()
    current_point = G
    i = 1
    list_point.append(G)
    while i < len(list_char):
        temp = curve.point_add(current_point, G)
        current_point = temp
        if current_point == (-1, -1):
            break
        i = i + 1
        list_point.append(current_point)
    if len(list_point) >= 218:
        result_str = f"The number of points on the elliptic curve of ({curve.a}, {curve.b}, {curve.p}) is approximately: {len(list_point)}\n"
        print(result_str)

def main():
    count = 0
    prime_number = [num for num in range(1, 251) if is_prime(num)]
    list_point = []
    # with open('output.txt', 'w') as file:
    for a in range(1,100):
        for b in range(1,100):
            for p in prime_number:
                if p>a and p>b:
                    curve = EllipticCurve(a, b, p)
                    check(curve)
                            # file.write(result_str)  # Write to file
    print("Total case is : ", count)

if __name__ == "__main__":
    main()