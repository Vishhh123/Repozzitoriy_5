#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    school = {'1a': 25, '1б': 30, '2б': 28, '6а': 32, '7в': 29}

    print(f"Начальный словарь: {school}")

    school['1a'] = 27
    print(f" В классе 1а изменилось кол-во учащихся: {school}")

    school['8г'] = 31
    print(f"Появление нового класса 8г: {school}")

    del school['2б']
    print(f"Был расформирован один класса 2б: {school}")

    obshchee_kolichestvo = sum(school.values())
    print(f"Общее количество учеников в школе: {obshchee_kolichestvo}")


