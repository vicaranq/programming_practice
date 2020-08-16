'''
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

'''
one_digit_map = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

two_digit_special_map = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen"
}

two_digit_map = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}
BILLION  = 1000000000
MILLION  = 1000000
THOUSAND = 1000
HUNDRED = 100

class Solution:

    def numberToWords(self, num: int) -> str:


        if num == 0: return "Zero"

        num_word = []

        # CHECK BILLION
        if num // BILLION >= 1:
            num_word += getBillionWord(num)
            num = num % BILLION

        # CHECK MILLION
        if num // MILLION >= 1:
            num_word += getMillionWord(num)
            num = num % MILLION

        # CHECK THOUSAND
        if num // THOUSAND >= 1:
            num_word += getThousandWord(num)
            num = num % THOUSAND

        # CHECK HUNDRED
        if num // HUNDRED >= 1:
            num_word += getHundredWord(num)
            num = num % HUNDRED

        # TWO DIGITS
        # num = num % HUNDRED
        if num >= 10:
            num_word += twoDigit(num)
        else:
            # ONE DIGIT
            num = num % 10
            if num:
                num_word += oneDigit(num)

        return " ".join(num_word)

def oneDigit(num):
    assert num < 10 and num > 0, "Incorrect input argument"
    return [one_digit_map[num]]

def twoDigit(num):
    assert num >= 10 and num <= 99, "Unexpected input argument"

    if num >= 10 and num < 20:
        return [two_digit_special_map[num]]
    if num >= 20:
        temp = []
        temp.append(two_digit_map[num//10])
        if num%10 > 0:
            temp.append(one_digit_map[num%10])
        return temp

def getHundredWord(num):
    assert num >= HUNDRED and num <  THOUSAND, "Unexpected input argument"
    # convert to 1 digit and append "Hundred"
    num = num // 100
    hundreds = []
    hundreds += oneDigit(num)
    hundreds.append("Hundred")
    return hundreds

def getThousandWord(num):
    assert num >= THOUSAND and num < MILLION, "Unexpected input"
    # convert to hundreds and append "Thousand"
    thousands = []
    num = num // THOUSAND
    if num >= 100:
        thousands += getHundredWord(num)
        num = num % 100
    if num > 0:
        if num >= 10:
            thousands += twoDigit(num)
        else:
            thousands += oneDigit(num)

    thousands.append("Thousand")
    return thousands

def getMillionWord(num):
    assert num >= MILLION and num < BILLION, "Unexpected input"
    millions = []
    num = num // MILLION
    if num >= 100:
        millions += getHundredWord(num)
        num = num % 100
    if num > 0:
        if num >= 10:
            millions += twoDigit(num)
        else:
            millions += oneDigit(num)

    millions.append("Million")
    return millions

def getBillionWord(num):
    assert num >= BILLION, "Unexpected input"
    billions = []
    num = num // BILLION
    billions += oneDigit(num)
    billions.append("Billion")
    return billions



