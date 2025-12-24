#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    alfavit_glasn = set("aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ")

    text = input("Введите строку: ")

    chars = set(text)

    peresechenie = chars.intersection(alfavit_glasn)

    count = 0

    for char in text:
        if char in alfavit_glasn:
            count += 1

    print(f"Найдено гласных букв: {count}")

    print(f"Уникальные гласные в строке: {peresechenie}")









