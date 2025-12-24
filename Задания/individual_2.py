#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

            poezd = {
                'punkt': punkt,
                'nomer': nomer,
                'vremya': vremya,
            }

            poezda.append(poezd)

            if len(poezda) > 1:
                poezda.sort(key=lambda item: item.get('punkt', ''))

        elif command == 'list':

            line = '+{}+{}+{}+'.format(
                '-' * 30,
                '-' * 15,
                '-' * 10
            )
            print(line)
            print(
                '| {:^30} | {:^15} | {:^10} |'.format(
                    "Пункт назначения",
                    "Номер поезда",
                    "Время"
                )
            )
            print(line)

            for poezd in poezda:
                print(
                    '| {:<30} | {:^15} | {:^10} |'.format(
                        poezd.get('punkt', ''),
                        poezd.get('nomer', ''),
                        poezd.get('vremya', '')
                    )
                )
            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=1)

            vremya_poiska = parts[1]

            count = 0

            for poezd in poezda:

                vremya_poezda = poezd.get('vremya', '00:00')

                chas_poezda, minuta_poezda = map(int, vremya_poezda.split(':'))
                chas_poiska, minuta_poiska = map(int, vremya_poiska.split(':'))

                if (chas_poezda > chas_poiska) or \
                        (chas_poezda == chas_poiska and minuta_poezda > minuta_poiska):
                    count += 1
                    print(
                        '{:>4}: {} - №{} - {}'.format(
                            count,
                            poezd.get('punkt', ''),
                            poezd.get('nomer', ''),
                            poezd.get('vremya', '')
                        )
                    )

            if count == 0:
                print("Поездов, отправляющихся после указанного времени, не найдено.")

        else:
            print(f"Неизвестная команда {command}")

