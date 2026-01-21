#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date

if __name__ == '__main__':
    poezda = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            punkt = input("Пункт назначения? ")
            nomer = input("Номер поезда? ")
            vremya = input("Время отправления (ЧЧ:ММ)? ")
            year_otpr = input("Год отправления? ")

            poezd = {
                'punkt': punkt,
                'nomer': nomer,
                'vremya': vremya,
                'year_otpr': int(year_otpr),
            }

            poezda.append(poezd)

            if len(poezda) > 1:
                poezda.sort(key=lambda item: item.get('punkt', ''))

        elif command == 'list':
            line = '+{}+{}+{}+{}+'.format(
                '-' * 30,
                '-' * 15,
                '-' * 10,
                '-' * 12
            )
            print(line)
            print(
                '| {:^30} | {:^15} | {:^10} | {:^12} |'.format(
                    "Пункт назначения",
                    "Номер поезда",
                    "Время",
                    "Год отпр."
                )
            )
            print(line)

            for poezd in poezda:
                Sprint(
                    '| {:<30} | {:^15} | {:^10} | {:^12} |'.format(
                        poezd.get('punkt', ''),
                        poezd.get('nomer', ''),
                        poezd.get('vremya', ''),
                        poezd.get('year_otpr', '')
                    )
                )
            print(line)

        elif command.startswith('select '):
            today = date.today()

            parts = command.split(' ', maxsplit=1)
            period = int(parts[1])S

            count = 0

            for poezd in poezda:
                if today.year - poezd.get('year_otpr', today.year) >= period:
                    count += 1
                    print(
                        '{:>4}: {} - №{} - {} (год: {})'.format(
                            count,
                            poezd.get('punkt', ''),
                            poezd.get('nomer', ''),
                            poezd.get('vremya', ''),
                            poezd.get('year_otpr', '')
                        )
                    )

            if count == 0:
                print("Поездов, добавленных более указанного периода, не найдено.")

        else:
            print("Неизвестная команда {}".format(command))