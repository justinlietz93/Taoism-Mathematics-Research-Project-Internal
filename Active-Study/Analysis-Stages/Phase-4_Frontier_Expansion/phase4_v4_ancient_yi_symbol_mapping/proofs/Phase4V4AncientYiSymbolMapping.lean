namespace Phase4V4

inductive LinePos where
  | top | second | third | fourth | fifth | bottom
  deriving DecidableEq, Repr

def bitPlace : LinePos -> Nat
  | .top => 0
  | .second => 1
  | .third => 2
  | .fourth => 3
  | .fifth => 4
  | .bottom => 5

def bitAt (n i : Nat) : Nat := (n / Nat.pow 2 i) % 2

def binaryLsd6 (n : Nat) : List Nat := [bitAt n 0, bitAt n 1, bitAt n 2, bitAt n 3, bitAt n 4, bitAt n 5]

def lowOctalDigit (n : Nat) : Nat := n % 8

def highOctalDigit (n : Nat) : Nat := n / 8

def yiValue2 (d0 d1 : Nat) : Nat := d0 + 8*d1

theorem yi_two_digit_roundtrip (n : Nat) (h : n < 64) :
  yiValue2 (lowOctalDigit n) (highOctalDigit n) = n := by
  unfold yiValue2 lowOctalDigit highOctalDigit
  omega

structure YiRow where
  decimal : Nat
  binary : List Nat
  lowDigit : Nat
  highDigit : Nat
  kingWen : Nat
  unicodeIndex : Nat

structure SymbolMappingPass (r : YiRow) : Prop where
  binary_ok : r.binary = binaryLsd6 r.decimal
  octal_ok : yiValue2 r.lowDigit r.highDigit = r.decimal
  unicode_ok : r.unicodeIndex = r.kingWen

end Phase4V4
