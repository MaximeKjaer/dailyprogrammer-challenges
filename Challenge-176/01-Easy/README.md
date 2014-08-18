#[Challenge #176 Easy - Spreadsheet Cell Selection Formulas]

**Python 3.4**

This solution supports letters bigger than Z (that means that AA, AB, AC, and even AAA, ZZZ, HELLO... all those columns work).

#Input/Ouput

Given a selection string that fits the following syntax, it returns the number of matching cells along with the coordinates of each of those cells:

1. A formula may have one or more :s (colons) in it. If so, a rectangle of cells is selected. This behaves the same way in Excel. Such a selection is called a range

2. A formula may have one or more &s (ampersands) in it. If so, both the cell/range specified to the left and right are selected. This is just a concatenation.

3. A formula may have one ~ (tilde) symbol in it. If so, any cells specified before the tilde are added to the final selection, and any cells after the tilde are removed from the final selection of cells


**Input**

    Enter your selection string: A3:C6&D1~B4&B5

**Ouput**

    11
    (0, 2)
    (0, 3)
    (0, 4)
    (0, 5)
    (1, 2)
    (1, 5)
    (2, 2)
    (2, 3)
    (2, 4)
    (2, 5)
    (3, 0)

***

**Input**

    Enter your selection string: B1:B3&B4:E10&F1:G1&F4~C5:C8&B2

**Ouput**

    29
    (1, 0)
    (1, 2)
    (1, 3)
    (1, 4)
    (1, 5)
    (1, 6)
    (1, 7)
    (1, 8)
    (1, 9)
    (2, 3)
    (2, 8)
    (2, 9)
    (3, 3)
    (3, 4)
    (3, 5)
    (3, 6)
    (3, 7)
    (3, 8)
    (3, 9)
    (4, 3)
    (4, 4)
    (4, 5)
    (4, 6)
    (4, 7)
    (4, 8)
    (4, 9)
    (5, 0)
    (6, 0)
    (5, 3)
