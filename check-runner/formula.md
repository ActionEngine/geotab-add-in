Signed deviation formula
=================================================================

Computes how much the target value deviates from the baseline value,
with sign indicating direction: positive means target grew,
negative means target dropped.

All values are assumed to be non-negative.

Definition (x = target, y = baseline):

```
f(x, y) :=
    | (x = 0) ∧ (y = 0)     => 0
    | y = 0                 => 1      (target has value, baseline doesn't)
    | x = 0                 => -1     (target is zero, baseline has value)
    | otherwise             => (x - y) / max(x, y)
```

Range: [-1, 1]

Properties:
- f(x, y) = -f(y, x)  (antisymmetric)
- f(x, x) = 0          (no deviation when equal)
- f(x, y) > 0          when target > baseline
- f(x, y) < 0          when target < baseline

Examples:

```
f(42, 42)         = (42 - 42) / max(42, 42)             = 0 / 42         = 0.0
f(100, 99)        = (100 - 99) / max(100, 99)           = 1 / 100        = 0.01
f(99, 100)        = (99 - 100) / max(99, 100)           = -1 / 100       = -0.01
f(1, 10000000)    = (1 - 10000000) / max(1, 10000000)   = -9999999 / 10000000 ≈ -0.9999
f(10000000, 1)    = (10000000 - 1) / max(10000000, 1)   = 9999999 / 10000000 ≈  0.9999
```

NULL handling (NULL is treated as 0):

```
    x       y       result
    NULL    NULL    => 0
    NULL    0       => 0
    0       NULL    => 0
    0       0       => 0
    x       NULL    => 1
    x       0       => 1
    NULL    y       => -1
    0       y       => -1
```
