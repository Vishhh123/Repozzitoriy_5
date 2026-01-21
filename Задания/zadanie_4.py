#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    slovar1 = {1: 'one', 2: 'two', 3: 'three'}
    print(slovar1)

    items_object = slovar1.items()
    print(items_object)

    slovar2 = {v: k for k, v in items_object}
    print(slovar2)

    