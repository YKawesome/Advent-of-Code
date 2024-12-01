from collections import namedtuple


Hand = namedtuple('Hand', ['labelsstr', 'labels', 'bid', 'type'])

_FIVE_OF_A_KIND = 6
_FOUR_OF_A_KIND = 5
_FULL_HOUSE = 4
_THREE_OF_A_KIND = 3
_TWO_PAIR = 2
_ONE_PAIR = 1
_HIGH_CARD = 0


def make_hand(line: str) -> Hand:
    '''Makes a hand from a line of text'''
    labels_string, bid = line.split(' ')
    bid = int(bid)

    labels = dict()
    labels_string_new = ''
    for label in labels_string:
        real_label = _convert_letter_to_number(label)
        labels_string_new += label
        if real_label in labels.keys():
            labels[real_label] += 1
        else:
            labels[real_label] = 1

    type = _get_hand_type(labels)

    return Hand(labels_string_new, labels, bid, type)


def _convert_letter_to_number(label: str) -> str:
    '''Converts letter cards to numbers'''
    if label == 'A':
        real_label = '14'
    elif label == 'K':
        real_label = '13'
    elif label == 'Q':
        real_label = '12'
    elif label == 'J':
        real_label = '0'
    elif label == 'T':
        real_label = '10'
    else:
        real_label = label
    return real_label


def _get_hand_type(labels: dict) -> int:
    '''Determines the type of hand'''
    labels_no_zeroes = {key: val for key, val in labels.items() if key != '0'}
    if 5 in labels.values() or '0' in labels.keys() and (labels['0'] + max(labels_no_zeroes.values()) >= 5):
        return _FIVE_OF_A_KIND
    elif 4 in labels.values() or '0' in labels.keys() and (labels['0'] + max(labels_no_zeroes.values()) >= 4):
        return _FOUR_OF_A_KIND
    elif 3 in labels.values() and 2 in labels.values():
        return _FULL_HOUSE
    elif list(labels_no_zeroes.values()).count(2) == 2 and '0' in labels.keys():
        return _FULL_HOUSE
    elif 3 in labels.values() or '0' in labels.keys() and (labels['0'] + max(labels_no_zeroes.values()) >= 3):
        return _THREE_OF_A_KIND
    elif list(labels.values()).count(2) == 2:
        return _TWO_PAIR
    elif 2 in labels_no_zeroes.values() and 1 in labels_no_zeroes.values() and '0' in labels.keys() and labels['0'] >= 1:
        return _TWO_PAIR
    elif list(labels_no_zeroes.values()).count(1) == 2 and '0' in labels.keys() and labels['0'] >= 2:
        return _TWO_PAIR
    elif 2 in labels.values():
        return _ONE_PAIR
    elif '0' in labels.keys():
        return _ONE_PAIR
    else:
        return _HIGH_CARD


def hand_value(hand: Hand) -> tuple[int, int, int, int, int, int]:
    '''Returns the value of a hand as a tuple in sorting order'''
    first_val = int(_convert_letter_to_number(hand.labelsstr[0]))
    second_val = int(_convert_letter_to_number(hand.labelsstr[1]))
    third_val = int(_convert_letter_to_number(hand.labelsstr[2]))
    fourth_val = int(_convert_letter_to_number(hand.labelsstr[3]))
    fifth_val = int(_convert_letter_to_number(hand.labelsstr[4]))
    return (hand.type, first_val, second_val, third_val, fourth_val, fifth_val)


def run() -> None:
    '''Main function'''
    f = open('Day 07/day7input.txt')
    lines = f.readlines()
    f.close()

    hands = [make_hand(line) for line in lines]
    hands.sort(key=lambda x: hand_value(x))

    total = sum([hand.bid * (i) for i, hand in enumerate(hands, start=1)])
    print(total)


if __name__ == '__main__':
    run()
