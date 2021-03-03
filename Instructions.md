# PS1

## Deadline: 14.03.2021 23.00 (Sunday)


*StressyMuch* is taking COMP100 course this semester. He is a very hardworking student and wants to get an A+ from this course. Therefore, he needs to study very hard for the midterm and final exams and he needs your help to decide how much time he needs to study.

Like most of us, he feels stressed if he does not study hard enough for the exams. However, it is hard to know how much he needs to study beforehand. Being a good student of math, he comes up with a formula for this. In this formula, we will use his favourite subject, math, and compute the miniumum time `T` he needs to sudy according to a lower bound `B`.

In particular, *StressyMuch* will feel stressed if he does not work at least `T` hours where `T` is the minimum number that satisfies the following equation:

`
(p1^(n-1)) * T + (p2^(n-2)) * T + ... + (pn^0) * T > B
`

Both `n` and `B` will be given as input. `B` is the lower bound and `n` is the number of elements in the sequence `p0, p1, ..., pn` where an element `pi` can be computed by using the formula below:

```
2^i + 1 if i is an even number
3^i + 1 if i is an odd number
```

An example sequence where `n = 10` is:

`4, 5, 28, 17, 244, 65, 2188, 257, 19684, 1025`

**Important:** `i` starts from `1`, not `0`.

**Our goal is to find the minimum T which satisfies the equation above.**


### Example 

For example, for `n = 4` and `B = 222`, the sequence will be:

`
4, 5, 28, 17
`

Then, we need to find the minium value such that

`(4^3) * t + (5^2) * t + (28^1) * t + (17^0) * t > 222`


So, in this case, if he studies only one hour, `T = 1`:

`(2^3) * 1 + (3^2) * 1 + (5^1) * 1 + (7^0) * 1 = 118` 

which is smaller than `B = 222` value. So, we try `T = 2` hours:

`(2^3) * 2 + (3^2) * 2 + (5^1) * 2 + (7^0) * 2 = 236` 

which is the minimum `T` that satisfies the equation.


In this problem set, you will implement two different methods to find the minimum `T` value that satisfies the given formula.

1. Brute force search
2. Bisection search

## Rules

1. The maximum possible value for the number `T` is `10000`.
2. You will calculate the numbers of the sequence by the formula given above. Do not forget that `i` starts from `1`.
4. If there is no value smaller than the maximum value, `10000`, you should output `-1` to signal "not found". 
3. The maximum runtime for this problem set will be **1 minute**. If your code does not end in 1 minute, there is probably something wrong in your code.
5. Please use the template we provided, `template.py`, to take the input and print the output. You can copy it to files "ps1a.py" and "ps1b.py" for your solutions below.

## Part A: Brute-Force Search

In this part, we can simply try different values for `T` starting from `1` and up until the maximum `T` value, which is given as `10000`. 

This solution will be the simplest solution. However, it will not be efficient because we will try all of the values exhaustively.


## Part B: Bisection Search

In this part, we will implement bisection search for finding the `T` value. Note that we know the minimum and maximum values for `T` which define our search range. 

You can think of the bisection search as searching one half of the search region every time. At each time step, we are checking the middle value and according to the comparison, we simply choose one side of the search region and search that half.

**Important note:** In the bisection search, if the middle element is larger than the value we are searching, we ignore that element and look for the left part of search region. However, in this problem, you cannot know if there is a value on the left part of the middle element that satisfies the equation. That is, middle value might be the minimum value that satisfies the equation. So, you **need to** save the minimum value that satisfies the equation before searching the left part because there might not be any value that satisfies the equation on the left part of the middle element.

** Example: **

Assume that `N` and `B` are `4` and `589999`, respectively.
In the bisection search, we have the range between `0` and `10000`. The first middle value we will try is `5000`. 

For the first try, we will calculate the value as `590000` which is greater than `B` and satisfies the equation but we do not know if there are values smaller than `5000` and satisfies the elements. There might be values smaller than `5000` and satisfies the equation, in this case, we will find them. However, there might be cases such that the element we are currently trying is the smallest element that satisfies the equation (like in this case). To handle those cases, you need to remember the minimum value that satisfies the equation before searching the smaller values (i.e. left part of the middle element.). For example, in this case, `5000` is the smallest number we can find.


## Example test cases

We provide some example test cases for you below. Note that there will be additional test cases for grading your homework. It is your responsibility to test your code with different test cases.

**Examples**

`4, 222 -> 2`
`5, 784 -> 1`
`3, 1242 -> 57`
`5, 11223344 -> 9488`
`8 99887766 -> 4` 

