## Problem ##

You’re in a maze where every room emits a tone (a non-negative integer). The softer the tone, the closer you feel to the Exit. Starting at the Start room, you must reach the Exit by always choosing to explore the next most promising room you've discovered, based on its tone.

If multiple rooms are equally promising, choose the one whose name comes first in lexicographic order.

Find a path from Start to Exit following the above selection rule. Once you reach the Exit, reconstruct and print the path from Start to Exit. If no path exists, print -1.


Input format


N M
name_1 name_2 ... name_N
tone_1 tone_2 ... tone_N
M lines: u v                 # undirected edges between room names u and v
Start Exit                    # room names


Output format
If reachable: print the path as room names from Start to Exit, space-separated.
Otherwise: print -1.


Constraints


2 ≤ N ≤ 2⋅10^5, 1 ≤ M ≤ 2⋅10^5
Room names are unique non-empty strings without spaces (may include letters/digits).
0 ≤ tone_i ≤ 10^9
The graph is undirected; there are no weights.
Multiple valid paths may exist; your selection order must follow the policy above to be deterministic.


Sample input


7 8 <br>
A B C D E F G <br>
12 7 6 5 3 9 1 <br>
A B <br>
A C <br>
B D <br>
C D <br>
C E <br>
D F <br>
E G <br>
F G <br>
A G <br>

       B(7)
          /        \
     A(12)     D(5)───F(9)
          \        /      \
           C(6)───E(3)────G(1)  ← Exit

Sample output (one valid)


A C E G
