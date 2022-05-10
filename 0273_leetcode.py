class Solution:
    def numberToWords(self, num: int) -> str:
        def parser(list_strings):
            list_strings.reverse()
            converted = ''.join(list_strings)
            parsed = []
            left, right = 0, 1

            while right < len(converted):
                if converted[right].isupper():
                    parsed.append(converted[left : right])
                    left = right
                right += 1

            parsed.append(converted[left : right])

            return ' '.join(parsed)

        def first(n):
            map_digits = {
                0: '',
                1: 'OneHundred',
                2: 'TwoHundred',
                3: 'ThreeHundred',
                4: 'FourHundred',
                5: 'FiveHundred',
                6: 'SixHundred',
                7: 'SevenHundred',
                8: 'EightHundred',
                9: 'NineHundred'
            }
            return map_digits[n]

        def second_twenties(n):
            map_digits = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return map_digits[n]

        def second_tens(n):
            map_digits = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return map_digits[n]

        def third(n):
            map_digits = {
                0: '',
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return map_digits[n]

        def get_blocks():
            blocks = []
            for i, n in enumerate(reversed(str(num))):
                if i % 3 == 0:
                    blocks.append([n])
                else:
                    blocks[-1].append(n)
            return blocks

        if not num:
            return 'Zero'

        output = []
        blocks = get_blocks()

        for i, block in enumerate(blocks):
            n = int(''.join(reversed(block)))
            if n == 0:
                continue
    
            if i == 1:
                output.append('Thousand')
            elif i == 2:
                   output.append('Million')
            elif i == 3:
                   output.append('Billion')

            if len(block) == 1:
                output.append(third(n))
            elif len(block) == 2:
                if 10 <= n < 20:
                    output.append(second_tens(n))
                else:
                    output.append(third(int(block[0])))
                    output.append(second_twenties(int(block[1])))
            else:
                if int(block[1]) >= 2:
                    output.append(third(int(block[0])))
                    output.append(second_twenties(int(block[1])))
                else:
                    n = int(''.join(reversed(block[0:2])))
                    if n >= 10:
                        output.append(second_tens(n))
                    else:
                        output.append(third(n))
                output.append(first(int(block[2])))

        return parser(output)
