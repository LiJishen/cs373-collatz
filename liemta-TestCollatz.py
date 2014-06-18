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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, determine_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ---------
    # Own tests
    # ---------

    def test_read_2 (self) :
        r    = StringIO("100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3 (self) :
        r    = StringIO("201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  201)
        self.assertEqual(j, 210)

    def test_read_4 (self) :
        r    = StringIO("1 2\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 2)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # ---------
    # Own tests
    # ---------
    def test_eval_5 (self) :
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    def test_eval_6 (self) :
        v = collatz_eval(1, 3)
        self.assertEqual(v, 8)

    def test_eval_7 (self) :
        v = collatz_eval(1, 4)
        self.assertEqual(v, 8)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # ---------
    # Own tests
    # ---------
    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 10, 10, 7)
        self.assertEqual(w.getvalue(), "10 10 7\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # ---------
    # Own tests
    # ---------
    def test_solve_2 (self) :
        r = StringIO("79 56\n73 81\n49 53\n78 53\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "79 56 116\n73 81 116\n49 53 25\n78 53 116\n")

    def test_solve_3 (self) :
        r = StringIO("88 30\n69 99\n54 52\n18 3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "88 30 116\n69 99 119\n54 52 113\n18 3 21\n")

    def test_solve_4 (self) :
        r = StringIO("12 45\n83 72\n34 37\n57 82\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "12 45 112\n83 72 116\n34 37 22\n57 82 116\n")

"""
    # ----------------------
    # determine cycle length
    # ----------------------

    # ---------
    # Own tests
    # ---------
    def test_determine_cycle_length_1 (self) :
        self.assertEqual(determine_cycle_length( 1), 1)

    def test_determine_cycle_length_2 (self) :
        self.assertEqual(determine_cycle_length( 5), 6)

    def test_determine_cycle_length_3 (self) :
        self.assertEqual(determine_cycle_length(10), 7)

    def test_determine_cycle_length_4 (self) :
        self.assertEqual(determine_cycle_length(2), 2)

"""

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
