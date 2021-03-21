def set_new_tree(tree):
    new_tree = []
    for i in range(len(tree)):
        left, center, right = get_bits(tree, i)
        new_tree.append(rule30(left, center, right))
    return new_tree


def parse_bit(bit):
    if bit:
        return "█"
    else:
        return " "


def display_tree(tree):
    result = "".join(map(parse_bit, tree))
    print(result, end="")


def rule30(left: int, center: int, right: int):
    result = left ^ (center | right)
    return result


def get_bits(tree, index):
    left = get_bit(tree, index - 1)
    center = get_bit(tree, index)
    right = get_bit(tree, index + 1)

    return left, center, right


def get_bit(tree, index):
    try:
        result = tree[index]
    except:
        result = 0

    return result


def main(size):
    half_size = size // 2
    tree = [0] * half_size
    tree.extend([1])
    tree.extend([0] * half_size)
    while True:
        display_tree(tree)
        tree = set_new_tree(tree)
        input()


main(160)
