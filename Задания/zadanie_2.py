#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    stroka_1 = input("Введите первую строку: ")
    stroka_2 = input("Введите вторую строку: ")
    mnojestvo_1 = set(stroka_1)
    mnojestvo_2 = set(stroka_2)
    obshchie = mnojestvo_1.intersection(mnojestvo_2)

    print(f"Общие символы в двух строках: {obshchie}")
    print(f"Количество общих символов: {len(obshchie)}")


