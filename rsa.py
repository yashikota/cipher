class RSA:
    def __init__(self):
        self.p = 0 # 7
        self.q = 0 # 5
        self.r = 0
        self.e = 0
        self.d = 0
        self.n = 0

    def is_prime(self, n):
        """素数の判定"""
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def input_p(self):
        """素数pの入力"""
        # 素数でなければ再入力
        while not self.is_prime(self.p):
            self.p = int(input("pを入力して下さい : "))
            if not self.is_prime(self.p):
                print("pは素数でなければなりません")

    def input_q(self):
        """素数qの入力"""
        # 素数でなければ再入力
        while not self.is_prime(self.q):
            self.q = int(input("qを入力して下さい : "))
            if not self.is_prime(self.q):
                print("qは素数でなければなりません")

    def calc_n(self):
        """pとqを乗算してnを求める"""
        self.n = self.p * self.q
        print("n = " + str(self.n))

    def calc_r(self):
        """p-1とq-1を乗算してrを求める"""
        self.r = (self.p - 1) * (self.q - 1)
        print("r = " + str(self.r))

    def calc_e(self):
        """pとqの互いに素な自然数eを求める"""
        # self.rと最大公約数が1の数字を求める
        for i in range(2, self.r):
            if self.gcd(i, self.r) == 1:
                self.e = i
                break
        print("e = " + str(self.e))

    def gcd(self, a, b):
        """ユークリッド互除法"""
        while b != 0:
            a, b = b, a % b
        return a

    def calc_d(self):
        """edを(p-1)(q-1)で割った余りがあまり1となる自然数dを求める"""
        # 拡張ユークリッド互除法
        for i in range(2, self.r):
            if self.gcd(i, self.r) == 1:
                if (self.e * self.r + 1) % i == 0:
                    self.d = (self.e * self.r + 1) // i
                    break
        print("d = " + str(self.d))

    def encrypt(self, m):
        """メッセージを暗号化する"""
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        """メッセージを復元する"""
        return pow(c, self.d) % self.n

    def main(self):
        self.input_p()
        self.input_q()
        self.calc_n()
        self.calc_r()
        self.calc_e()
        self.calc_d()
        m = int(input(f"mを入力して下さい({self.n}以下の自然数) : "))
        c = self.encrypt(m)
        print("c = " + str(c))
        m2 = self.decrypt(c)
        print("m = " + str(m2))


if __name__ == "__main__":
    rsa = RSA()
    rsa.main()
