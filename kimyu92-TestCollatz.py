#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % coverage3 run --branch TestCollatz.py

To obtain coverage of the test:
    % coverage3 report -m
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        r    = StringIO("1 1\n6236 20461\n16940 23698\n13854 15570\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1)

    def test_read_3 (self) :
        r    = StringIO("9 18\n4738 22528\n19997 23455\n12826 20052\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  9)
        self.assertEqual(j, 18)

    def test_read_4 (self) :
        r    = StringIO("15 25\n4460 23661\n4386 14922\n11008 16112\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  15)
        self.assertEqual(j, 25)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        arr = {}
        arr[1] = 1
        v = collatz_eval(1, 10, arr)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        arr = {}
        arr[1] = 1
        v = collatz_eval(100, 200, arr)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        arr = {}
        arr[1] = 1
        v = collatz_eval(201, 210, arr)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        arr = {}
        arr[1] = 1
        v = collatz_eval(900, 1000, arr)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 2, 4, 6)
        self.assertEqual(w.getvalue(), "2 4 6\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 8, 16, 24)
        self.assertEqual(w.getvalue(), "8 16 24\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 9, 27, 45)
        self.assertEqual(w.getvalue(), "9 27 45\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1 1\n6236 20461\n16940 23698\n13854 15570\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n6236 20461 279\n16940 23698 282\n13854 15570 271\n")

    def test_solve_3 (self) :
        r = StringIO("9 10\n4738 22528\n19997 23455\n12826 20052\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "9 10 20\n4738 22528 279\n19997 23455 269\n12826 20052 279\n")

    def test_solve_4 (self) :
        r = StringIO("6 8\n4460 23661\n4386 14922\n11008 16112\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "6 8 17\n4460 23661 282\n4386 14922 276\n11008 16112 276\n")

# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py
FFFF..F
======================================================================
FAIL: test_eval_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 47, in test_eval_1
    self.assertEqual(v, 20)
AssertionError: 1 != 20

======================================================================
FAIL: test_eval_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 51, in test_eval_2
    self.assertEqual(v, 125)
AssertionError: 1 != 125

======================================================================
FAIL: test_eval_3 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 55, in test_eval_3
    self.assertEqual(v, 89)
AssertionError: 1 != 89

======================================================================
FAIL: test_eval_4 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 59, in test_eval_4
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_solve (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 78, in test_solve
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


----------------------------------------------------------------------
Ran 7 tests in 0.004s

FAILED (failures=5)



% coverage3 report -m
Name           Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      0      0    97%   86
----------------------------------------------------------
TOTAL            51      1      6      0    98%
"""
