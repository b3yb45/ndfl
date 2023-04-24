from math import *

'''
Андреев Игорь - 30
Мурашова Ирина - 
Аронова Александра - 
'''


def income_res():
    inc = input('Получали ли Вы доходы от источников в РФ и за её пределами? ').lower()
    if inc == 'нет':
        print('НДФЛ: 0 рублей')
    else:
        percent = input('Получали ли Вы дивиденты или проценты от российских или иностранных организаций? ').lower()
        insurance = input('Получали ли Вы страховые выплаты? ').lower()

        if insurance == 'да':
            insurance_1 = float(input('Укажите величину страховых выплат: '))
            sum_insurance = (insurance_1 * 0.13)
        else:
            sum_insurance = 0

        if percent == 'да':
            percent_1 = float(input('Укажите сумму дивидентов в денежном эквиваленте: '))
            sum_percent = (percent_1 * 0.13)
        else:
            sum_percent = 0

        stock = input('Получали ли Вы дивиденды от иностранной организации по акциям росийской? ').lower()
        if stock == 'да':
            stock_1 = float(input('Укажите сумму дивидентов в денежном эквиваленте: '))
            sum_stock = (stock_1 * 0.09)
        else:
            sum_stock = 0

        copy_right = input('Получали ли Вы доходы от использования авторских или смежных прав в РФ? ').lower()
        if copy_right == 'да':
            copyright_1 = float(input('Укажите величину доходов: '))
            sum_copyright = (copyright_1 * 0.13)
        else:
            sum_copyright = 0

        rent = input('Получали ли Вы доходы от сдачи в аренду или иного использования имущества в РФ? ').lower()
        if rent == 'да':
            rent_1 = float(input('Укажите величину доходов: '))
            sum_rent = (rent_1 * 0.13)
        else:
            sum_rent = 0

        benefit = input('Получали ли Вы пенсии, стипендии, пособия или аналогичные выплаты? ').lower()
        if benefit == 'да':
            benefit_1 = float(input('Укажите суммарную величину выплат: '))
            sum_benefit = (benefit_1 * 0.13)
        else:
            sum_benefit = 0

        gift = input('Получали ли Вы в дар имущество от физических лиц, не являющимися близкими родственниками? ').lower()
        if gift == 'да':
            gift_1 = float(input('Укажите имущество в денежном эквиваленте: '))
            sum_gift = (gift_1 * 0.13)
        else:
            sum_gift = 0

        grant = input('Получали ли Вы выигрыш от операторов лотерей в сумме до 15000 рублей? ').lower()
        if grant == 'да':
            grant_1 = float(input('Укажите величину выигрыша: '))
            sum_grant = (grant_1 * 0.13)
        else:
            sum_grant = 0

    if inc == 'да':
        base = (sum_insurance + sum_percent + sum_stock + sum_copyright + sum_rent + sum_benefit + sum_gift + sum_grant)
        if base < (5 * (10 ** 6)):
            ndfl = base * 0.13
            print('НДФЛ:', ndfl, ' рублей')
            print('Сумма вычета: ', tax_deduct() * 0.13, ' рублей')
        else:
            ndfl = 650 * (10 ** 3) + base * 0.15
            print('НДФЛ:', ndfl, ' рублей')
            print('Сумма вычета: ', tax_deduct() * 0.15, ' рублей')


def income_not_res():
    inc = input('Получали ли Вы доходы от источников в РФ и за её пределами? ').lower()
    if inc == 'нет':
        print('НДФЛ: 0')
    else:

        insurance = input('Получали ли Вы страховые выплаты? ').lower()
        if insurance == 'да':
            insurance_1 = float(input('Укажите величину страховых выплат: '))
            sum_insurance = (insurance_1 * 0.3)
        else:
            sum_insurance = 0

        percent = input('Получали ли Вы дивиденты или проценты от российских или иностранных организаций? ').lower()
        if percent == 'да':
            percent_1 = float(input('Укажите сумму дивидентов в денежном эквиваленте: '))
            sum_percent = (percent_1 * 0.15)
        else:
            sum_percent = 0

        stock = input('Получали ли Вы дивиденды от иностранной организации по акциям росийской? ').lower()
        if stock == 'да':
            stock_1 = float(input('Укажите сумму дивидентов в денежном эквиваленте: '))
            sum_stock = (stock_1 * 0.09)
        else:
            sum_stock = 0

        copy_right = input('Получали ли Вы доходы от использования авторских или смежных прав в РФ? ').lower()
        if copy_right == 'да':
            copyright_1 = float(input('Укажите величину доходов: '))
            sum_copyright = (copyright_1 * 0.3)
        else:
            sum_copyright = 0

        rent = input('Получали ли Вы доходы от сдачи в аренду или иного использования имущества в РФ? ').lower()
        if rent == 'да':
            rent_1 = float(input('Укажите величину доходов: '))
            sum_rent = (rent_1 * 0.15)
        else:
            sum_rent = 0

        benefit = input('Получали ли Вы пенсии, стипендии, пособия или аналогичные выплаты? ').lower()
        if benefit == 'да':
            benefit_1 = float(input('Укажите суммарную величину выплат: '))
            sum_benefit = (benefit_1 * 0.3)
        else:
            sum_benefit = 0

        gift = input('Получали ли Вы в дар имущество от физических лиц, не являющимися близкими родственниками? ').lower()
        if gift == 'да':
            gift_1 = float(input('Укажите имущество в денежном эквиваленте: '))
            sum_gift = (gift_1 * 0.3)
        else:
            sum_gift = 0

        grant = input('Получали ли Вы выигрыш от операторов лотерей в сумме до 15000 рублей? ').lower()
        if grant == 'да':
            grant_1 = float(input('Укажите величину выигрыша: '))
            sum_grant = (grant_1 * 0.15)
        else:
            sum_grant = 0

    if inc == 'да':
        base = (sum_insurance + sum_percent + sum_stock + sum_copyright + sum_rent + sum_benefit + sum_gift + sum_grant)
        if base < (5 * (10 ** 6)):
            ndfl = (base * 0.3)
            print('НДФЛ:', ndfl, ' рублей')
        else:
            ndfl = (650 * (10 ** 3) + base * 0.15)
        print('НДФЛ:', ndfl, ' рублей')


def tax_deduct():
    get_deduct = input('Рассчитать налоговый вычет? (да/нет) ').lower()

    if get_deduct != "да":
        return 0

    else:
        deduct_sum = 0

        stndrt_ddct_sum = 0
        get_stndrt_ddct = input('Родители до 18 лет (или до 24, если получаете высшее образование на очной форме'
                                ' обучения)? (да/нет) ').lower()

        if get_stndrt_ddct == 'да':
            children = int(input('Укажите число детей: '))
            disability = int(input('Есть ли среди них инвалиды? Укажите число: '))
            income_350 = int(input('Введите число месяцев, в течение которых ваш доход с начала года был менее 350000'
                                   ' рублей: '))

            stndrt_ddct_sum = (min(children, 2) * 1400 + max(children - 2, 0) * 3000 + disability * 12000) * income_350

        get_benefit = input('Принадлежите ли вы к льготным категориям граждан'
                            ' (инвалиды, герои войны, чернобыльцы и т. д.)? (да/нет) ').lower()

        if get_benefit == 'да':
            benefit_deduct = int(input('Введите сумму вычета, предоставленного по льготам'
                                       ' (500 или 3000 рублей в месяц): '))

            if benefit_deduct == 500 or 3000:
                stndrt_ddct_sum += benefit_deduct * 12

        print('Сумма стандартного вычета: ', stndrt_ddct_sum)

        social_ddct_sum = 0

        get_social_ddct = input('Имели ли вы в течение отчетного года расходы на расходы на благотворительность,'
                                ' а также расходы в пользу себя или близких родственников на лечение, обучение,'
                                ' страхование и пенсионное страхование (посредством организаций, получивших'
                                ' соответствующие лицензии в РФ)? (да/нет) ').lower()

        if get_social_ddct == 'да':
            charity = float(input('Укажите расходы на благотворительность: '))
            income = float(input('Укажите годовой доход: '))
            charity = min(charity, income / 4)

            education = float(input('Укажите расходы на образование: '))

            med_expenses = float(input('Укажите расходы на лечение (не более 120000 рублей в год): '))

            costly_med_expenses = float(input('Укажите расходы на дорогостоящее лечение: '))

            insurance = float(input('Укажите расходы на страхование жизни или негосударственное пенсионное '
                                    'обеспечение на срок от пяти лет: '))

            social_ddct_sum += min(charity + education + med_expenses + insurance, 120_000) + costly_med_expenses

            print('Сумма социального вычета: ', social_ddct_sum)

        property_deduct_sum = 0

        get_property_ddct = input('Имели ли вы расходы на покупку или строительство жилья? (да/нет) ').lower()
        get_sale_deduct = input('Продавали ли вы имущество? (да/нет) ').lower()

        if get_property_ddct == 'да':
            mortgage = input('При покупке или строителсьтве жилья вы использовали ипотечный кредит? (да/нет)? ')

            if mortgage == 'да':
                property_deduct_sum += min(float(input('Введите сумму процентов по кердиту в рублях: ')), 3_000_000)

            property_deduct_sum += min(float(input('Введите сумму расходов на покупку или строительство'
                                                   ' (без использования ипотечного кредита): ')), 2_000_000)

        if get_sale_deduct == 'да':
            property_gift = input('Проданное имущество было получено путем наследования, дарения или'
                                  ' приватизации? (да/нет) ').lower()

            if property_gift == 'да':
                term = input('Проданное имущество находилось в вашей собственности менее 3 лет? (да/нет) ').lower()
                if term == 'да':
                    confirm = input('У вас есть документы подтверждающие расходы на покупку? (да/нет) ').lower()
                    real_estate = input('Имущество недвижимое? (да/нет) ').lower()

                    if confirm == 'да':
                        property_deduct_sum += float(input('Введите расходы на приобретение собственности: '))

                    elif real_estate == 'да':
                        property_deduct_sum += 1_000_000

                    elif real_estate == 'нет':
                        property_deduct_sum += 250_000

            property_bought = input('Проданное имущество было получено путем кроме наследования, дарения или'
                                    ' приватизации? (да/нет) ').lower()

            if property_bought == 'да':
                term = input('Проданное имущество находилось в вашей собственности менее 5 лет? (да/нет) ').lower()
                if term == 'да':
                    confirm = input('У вас есть документы подтверждающие расходы на покупку? (да/нет) ').lower()
                    real_estate = input('Имущество недвижимое? (да/нет) ').lower()

                    if confirm == 'да':
                        property_deduct_sum += float(input('Введите расходы на приобретение собственности: '))

                    elif real_estate == 'да':
                        property_deduct_sum += 1_000_000

                    elif real_estate == 'нет':
                        property_deduct_sum += 250_000

        print('Сумма имущественного вычета: ', property_deduct_sum)

        invest_deduct_sum = 0

        broker_acc = input('Имеете ли вы обычный брокерский счет? (да/нет) ').lower()

        if broker_acc == 'да':
            broker_years = int(input('Введите число лет, прошедшее с покупки ценых бумаг: '))
            if broker_years > 2:
                invest_deduct_sum += broker_years * 3_000_000

        elif input('Вы являетесь владельцем ИИС типа А? (да/нет) ').lower() == 'да':
            annual_invest = float(input('Введите размер годового взноса на счет: '))
            invest_deduct_sum += min(annual_invest, 400_000)

        elif input('Вы являетесь владельцем ИИС типа Б? (да/нет) ').lower() == 'да':
            acc_profit = float(input('Введите полученную по счету прибыль, кроме дивидендов: '))
            invest_deduct_sum += acc_profit

        invest_profit = float(input('Введите прибыль от инвестиций: '))
        invest_deduct_sum = min(invest_deduct_sum, invest_profit)
        print('Сумма инвестиционного вычета: ', invest_deduct_sum)

        prof_deduct_sum = 0

    deduct_sum += stndrt_ddct_sum + social_ddct_sum + property_deduct_sum + invest_deduct_sum + prof_deduct_sum
    return deduct_sum


terr = input('Находились ли Вы на территории РФ не менее 183 календарных дней в течение 12 месяцев подряд? ').lower()
if terr == 'нет':
    print('Вы не являетесь резидентом РФ.')
    resident = 'нет'
else:
    leave = input('Выезжали ли вы за пределы территории РФ дольше, чем на 6 месяцев? ').lower()
    if leave == 'да':
        print('Вы не являетесь резидентом РФ.')
        resident = 'нет'
    else:
        print('Вы являетесь резидентом РФ.')
        resident = 'да'

if resident == 'да':
    restriction = input('Применялись ли к Вам меры ограничительного характера? ').lower()

    taxes = input('Являлись ли Вы налоговым резидентом иностранного государства? ').lower()
    if restriction and taxes == 'да':
        print('Вы не являетесь налоговым резидентом РФ, если подали заявление.')
    else:
        print('Вы являетесь налоговым резидентом РФ.')
        income_res()

else:
    soldier = input('Являетесь ли Вы российским военнослужащим, проходящим службу за границей? ').lower()

    gov = input('Являетесь ли Вы сотрудником органов государственной власти, коммандированных за границу? ').lower()
    if soldier or gov == 'да':
        print('Вы являетесь налогоплательщиком.')
        income_res()
    else:
        income_not_res()

