package main

import (
	"fmt"
	"math"
	"strconv"
)

// ２つの素数を入力する
func input_number() (int) {
  var n int;
  fmt.Println("素数を入力してください");
  fmt.Scanln(&n);

  // 入力された数字が素数であるか確認する
  if !is_prime(n) {
    fmt.Println("入力された数字は素数ではありません");
    return input_number();
  }

  return n;
}

// 素数判定
func is_prime(n int) bool {
  if n < 2 {
    return false;
  }
  for i := 2; i * i <= n; i++ {
    if n % i == 0 {
      return false;
    }
  }
  return true;
}

// pとqの積を求める
func calc_n(p, q int) int {
  return p * q;
}

// p-1とq-1の積を求める
func calc_r(p, q int) int {
  return (p - 1) * (q - 1);
}

// 最大公約数を求める
func gcd(a, b int) int {
  if b == 0 {
    return a;
  }
  return gcd(b, a % b);
}

// 最小公倍数を求める
func lcm(a, b int) int {
  return a * b / gcd(a, b);
}

// l未満でpとqの互いに素であるeを求める
func calc_e(r int) int {
  for i := 2; i < r; i++ {
    if gcd(i, r) == 1 {
      return i;
    }
  }
  return 0;
}

// edを(p-1)(q-1)で割った余りがあまり1となる自然数dを求める
func calc_d(e, r int) int {
  for i := 1; i < r; i++ {
    if (e * i) % r == 1 {
      return i;
    }
  }
  return 0;
}

func encrypt(m int, e int, n int) int {
  return int(math.Pow(float64(m), float64(e))) % n;
}

func decrypt(c int, d int, n int) int {
  return int(math.Pow(float64(c), float64(d))) % n;
}

func main() {
  var p, q int;
  p = input_number(); // 17
  q = input_number(); // 19

  fmt.Println("p = ", p);
  fmt.Println("q = ", q);

  // pとqの積を求める
  n := calc_n(p, q); // 17 * 19 = 323
  fmt.Println("n = ", n);

  // p-1とq-1の積を求める
  r := calc_r(p, q); // 16 * 18 = 288
  fmt.Println("r = ", r);

  // pとqの互いに素な自然数eを求める
  // 公開鍵
  e := calc_e(r); // 5
  fmt.Println("e = ", e);

  // edを(p-1)(q-1)で割った余りがあまり1となる自然数dを求める
  // 秘密鍵
  d := calc_d(e, r); // 173
  fmt.Println("d = ", d);

  // メッセージを入力する
  var m int;
  fmt.Printf("mを入力して下さい(%s)以下の自然数) : ", strconv.Itoa(d));
  fmt.Scanln(&m);

  // 公開鍵を使って暗号化する
  c := encrypt(m, e, n); // m ^ e % n
  fmt.Println("c = ", c);

  // 秘密鍵を使って復号する
  m2 := decrypt(c, d, n); // c ^ d % n
  fmt.Println("m2 = ", m2);
}
