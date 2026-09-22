"""Tutorial 5 program: the two greatest and the two smallest of a list."""


def two_extremes(nums):
    if len(nums) <= 4:
        raise ValueError("input list must contain more than 4 integers")

    g1 = g2 = float("-inf")
    s1 = s2 = float("inf")
    for x in nums:
        if x > g1:
            g2, g1 = g1, x
        elif x > g2:
            g2 = x
        if x < s1:
            s2, s1 = s1, x
        elif x < s2:
            s2 = x
    return (g1, g2, s1, s2)
