#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "e", "g", "o", "p"}
    b = {"e", "h", "i", "o", "u"}
    c = {"g", "h", "p", "s", "t", "w"}
    d = {"f", "h", "n", "s", "t", "x", "y"}

    x = (a.difference(c)).intersection(u.difference(b))
    y = (u.difference(a).intersection(u.difference(b))).difference(c.union(d))

    print(f"x = {x}")
    print(f"y = {y}")


