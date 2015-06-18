# CMPS 130 - Homework CS Elective Requirement

<img src="http://newsoffice.mit.edu/sites/mit.edu.newsoffice/files/styles/news_article_image_top_slideshow/public/images/2015/MIT-Quad-Genome.jpg?itok=qMwDyhOy" style="float:left; margin-right:1em; width:300px"/>
If you are a Computer Science major wishing to count this course as one of your seven electives, you are required to complete the following additional assignment before the last day of the class.  As a computer science major, you already know C and C++ well (perhaps C++ more than C).  In this assignment you will implement a well known algorithm in computer science commonly used in genetics research in both Python and C++.  You will also evaluate the two, for both runtime efficiency and ease of programming.  The purpose of this assignment is for you to better understand the similarities, differences, and relative strengths of Python and C++ on a common problem.

## The Algorithm
You will implement an algorithm that calculates the *edit distance*, or more specifically, the [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between two strings.  The Levenshtein distance between two strings is the minimum number of single-character edits (i.e. insertions, deletions or substitutions) required to change one string into the other.  This is particularly useful when studying the similarity between genes from different organisms.  DNA sequences conserved (small edit distance) across species are likely to be functionally important, while variations between members of the same species can indicate different susceptibilities to disease.

For example, we might examine the following short DNA sequences:
```
GGAAGGGGCGATCGGAGGGC
GGTAAGGGGCCTGATCGAAGGGCAA
```
We can calculate the edit distance, and record insertions/deletions/substitutions in such a way that we can print a *aligned* set of sequences, with dashes representing misaligned symbols
```
GG-AAGGGG-C-GATCGGAGGGC--
GGTAAGGGGCCTGATCGAAGGGCAA
```

There are several ways of calculating edit distance.  The widely accepted *best* algorithm is the Wagner–Fischer algorithm, which utilizes a 2-dimensional array to calculate the answer in O(N&dot;M) time, and O(N&dot;M) memory space - where N and M are the lengths of the two strings being compared.  When the strings are of similar length, you can think of the algorithm being O(N<sup>2</sup>).  No one has ever said O(N<sup>2</sup>) is fast (or efficient), but since all the other known algorithms are *exponential*, the Wagner-Fischer is widely adopted.  Computer scientists have been debating for decades whether there exists a better (more efficient) algorithm for this type of problem - but it has [recently been proven to be optimal](http://newsoffice.mit.edu/2015/algorithm-genome-best-possible-0610)!

## Calculating Edit Distance
```
* Input:  Two strings, S and T
* Construct an M x N matrix (array) of integers in memory, called D, 
  where M is equal to the length of S + 1, and N is equal to the length of T + 1. 
* Assign the values 0...M to the first row of the array, and 0..N to the first column.
```
### Processing
Starting at element [1,1], proceed down each column, working your way to the right *after* completing each column.  

```
At each cell [i,j]:
* if S[j] is equal to T[i], then assign D[i,j] to be the value D[i-1, j-1].
* Otherwise, assign D[i, j] to be the **minimum** of the following three values:
	* D[i-1, j] + 1  (representing a deletion)
	* D[i, j-1] + 1  (representing an insertion)
	* D[i-1, j-1] + 1 (representing a substitution)
```
### Result
Once you've processed all the cells, the bottom right-most cell contains the (optimal) total number of edits to transform S into T.

## Recording the actual edits
The algorithm above is fairly straightforward, however it only gives us the end result - the edit distance.  When comparing genetic sequences, its usually important to use the edit operations to construct a *sequence alignment*.  To do this, we not only need to create the matrix described above, but we need to record *which* operations would be performed along the way.

To do this, you should make an auxilary array, E, of the same dimensions as D in the description above.  When assigning D[i, j], assign E[i, j] as the following:

```
* if S[j] is equal to T[i], then assign E[i, j] to be 0, 
  (representing the fact that the value is derived from the cell diagnoal from this cell (above and left).
* Otherwise, assign E[i, j] according to which D cell is used to derive the value of D[i, j] as follows:
	* If D[i-1, j] was used, record 1 (derived from cell above)
	* If D[i, j-1] was used, record 2 (derived from cell to the left)
	* If D[i-1, j-1] was used, record 0 (derived from cell diagonal to this one)
```
## Backtracing to obtain sequences with gaps inserted
Once D and E have been constructed, you can now create *aligned* sequences, representing insert/deletes with gaps (-) in the corresponding sequences by *backtracing* E. 

Start with two empty strings, representing the final S and T string.  Lets call them S_RESULT and T_RESULT

Starting at the lower right of E (the same cell you got the edit distance from D), proceed as follows:

```
* if the cell E[i, j] is 0, **prepend** S[j-1] to S_RESULT, **prepend** T[i-1] to T_RESULT, and decrement i and j
* if the cell E[i, j] is 1, **prepend** S_RESULT with a '-', **prepend** T[i-1] to T_RESULT, and decrement i
* if the cell E[i, j] is 2, **prepend** S[j-1] to S_RESULT, **prepend** T_RESULT with a '-', and decrement j.
```
Depending if you are using C++ or Python, this string building exercise might be done slightly different - but the point is that when you see a cell derived from the diagonal, you use characters from both inputs.  On a cell derived from the left, you place a gap in the up/down string, and if you see a cell derived from above, you place a gap in the left/right string.  You are building the string in reverse, and when r or c gets to 0, use the remaining characters from either the left/right or up/down string to finish off the process.

# Your Assignment
For this assignment, you will write two programs that do the exact same thing - one in C++ and one in Python.

Your programs should first accept two strings on the command line (see below for help with command line arguments), which represent the filename of two files.  Each of these files should just contain simple strings, I've provided three sample sets - the first two are very small test files, helpful during debugging.  The third pair represents the NRAS genomic sequence in humans and in cows (these genes are involved in some cancers).

* Sample set 1 - [S](s1.txt), [T](t1.txt)
* Sample set 2 - [S](s2.txt), [T](t2.txt)
* Sample set 3 - [Human NRAS](nras_human.txt), [Cow NRAS](nras_cow.txt)

Your program should open the files based on the command line arguments and read the strings (remove new line characters) into variables.

Next, perform the Wagner-Fischer computation, including the backtracing procedure explained above.  

Your program should print out the resulting aligned sequences/strings, and also print out the number of edits (the edit distance). You should also print the total elapsed run time of the processing.  See below for details on timing in C++, you already know how to do this in Python.

Here is output of the first two samples.  Your program should have the exact same results, except of course for the elapsed time, which will be unique for your machine.  I compiled my C++ solution into a program named `editc`.  The Python version would print the same results (with a different time)

```
> editc s1.txt s2.txt
Input Sequences
----------------------------
Saturday
Sunday
----------------------------
Aligned Sequences
----------------------------
Saturday
S--unday
----------------------------
The minimum edit distance is 3
Completed in 0.000100 seconds.
```
```
> editc s2.txt s2.txt
Input Sequences
----------------------------
GGAAGGGGCGATCGGAGGGC
GGTAAGGGGCCTGATCGAAGGGCAA
----------------------------
Aligned Sequences
----------------------------
GG-AAGGGG-C-GATCGGAGGGC--
GGTAAGGGGCCTGATCGAAGGGCAA
----------------------------
The minimum edit distance is 6
Completed in 0.000129 seconds.
```

## Analysis Report
As part of this assignment, I also ask that you turn in a short (1 page) writeup on your findings regarding efficiency and programming experience of C++ relative to Python.

### Runtime and memory efficiency
It will likely come as no surprise which language is faster once you run them, but I'd like you to explain the performance difference - why is one faster than the other?  Is there any way to mitigate these problems in the slower language?

### Programming experience
Please comment on which language you found more convenient to write the program in. Which parts of the program were easier to write with a particular language?

## Testing
Unless you have *unusually* impressive skills, you might not get this to work the first time your run your program.   Below is the actual matrix that would be generated for Samples 1 and 2.  You might want to print yours out, so you can compare to see what could be going wrong..

Sample 1
```
	   S  a  t  u  r  d  a  y
=============================
  | 0  1  2  3  4  5  6  7  8  
S | 1  0  1  2  3  4  5  6  7  
u | 2  1  1  2  2  3  4  5  6  
n | 3  2  2  2  3  3  4  5  6  
d | 4  3  3  3  3  4  3  4  5  
a | 5  4  3  4  4  4  4  3  4  
y | 6  5  4  4  5  5  5  4  3  
```
Sample 2
```

	     G   G   A   A   G   G   G   G  C    G   A   T   C   G   G   A   G   G   G   C
======================================================================================
  | 0    1   2   3   4   5   6   7   8  9   10  11  12  13  14  15  16  17  18  19  20
G | 1    0   1   2   3   4   5   6   7  8    9  10  11  12  13  14  15  16  17  18  19    
G | 2    1   0   1   2   3   4   5   6  7    8   9  10  11  12  13  14  15  16  17  18
T | 3    2   1   1   2   3   4   5   6  7    8   9   9  10  11  12  13  14  15  16  17    
A | 4    3   2   1   1   2   3   4   5  6    7   8   9  10  11  12  12  13  14  15  16  
A | 5    4   3   2   1   2   3   4   5  6    7   7   8   9  10  11  12  13  14  15  16  
G | 6    5   4   3   2   1   2   3   4  5    6   7   8   9   9  10  11  12  13  14  15  
G | 7    6   5   4   3   2   1   2   3  4    5   6   7   8   9   9  10  11  12  13  14  
G | 8    7   6   5   4   3   2   1   2  3    4   5   6   7   8   9  10  10  11  12  13  
G | 9    8   7   6   5   4   3   2   1  2    3   4   5   6   7   8   9  10  10  11  12  
C | 10   9   8   7   6   5   4   3   2  1    2   3   4   5   6   7   8   9  10  11  11  
C | 11  10   9   8   7   6   5   4   3  2    2   3   4   4   5   6   7   8   9  10  11  
T | 12  11  10   9   8   7   6   5   4  3    3   3   3   4   5   6   7   8   9  10  11  
G | 13  12  11  10   9   8   7   6   5  4    3   4   4   4   4   5   6   7   8   9  10  
A | 14  13  12  11  10   9   8   7   6  5    4   3   4   5   5   5   5   6   7   8   9  
T | 15  14  13  12  11  10   9   8   7  6    5   4   3   4   5   6   6   6   7   8   9  
C | 16  15  14  13  12  11  10   9   8  7    6   5   4   3   4   5   6   7   7   8   8  
G | 17  16  15  14  13  12  11  10   9  8    7   6   5   4   3   4   5   6   7   7   8  
A | 18  17  16  15  14  13  12  11  10  9    8   7   6   5   4   4   4   5   6   7   8  
A | 19  18  17  16  15  14  13  12  11  10   9   8   7   6   5   5   4   5   6   7   8  
G | 20  19  18  17  16  15  14  13  12  11  10   9   8   7   6   5   5   4   5   6   7  
G | 21  20  19  18  17  16  15  14  13  12  11  10   9   8   7   6   6   5   4   5   6  
G | 22  21  20  19  18  17  16  15  14  13  12  11  10   9   8   7   7   6   5   4   5  
C | 23  22  21  20  19  18  17  16  15  14  13  12  11  10   9   8   8   7   6   5   4  
A | 24  23  22  21  20  19  18  17  16  15  14  13  12  11  10   9   8   8   7   6   5  
A | 25  24  23  22  21  20  19  18  17  16  15  14  13  12  11  10   9   9   8   7   6  
```

## Implementation in C++

If you haven't used command line arguments before in C++, here's a code snippet to help you:
```
#include <iostream>
using namespace std;

int main(int argv, char ** argc) {
	if ( argv >= 3 ) {
		cout << argc[1] << endl;
		cout << argc[2] << endl;
	}
}
```

If you run your program from the command line (lets say you compile it to be named `test`), you can enter two arguments and they will print to the screen.  These would be the filenames in your actual program...

```
> test hello world
hello
world
>
```

You may use and valid C or C++ to open the text files and read them into strings.  You can use any method of keeping track of time that you find convenient - here is a sample of how to do this with the standard C library.

```
#include <ctime>
#include <iostream>
using namespace std;

int main() {
	int start = clock();

	for ( int i = 0; i < 10000; i++ ) {
		cout << ".";
	}
	cout << endl;
	
	int t = clock() - start;
	cout << "Completed in " <<((float)t)/CLOCKS_PER_SEC << " seconds." << endl;;
}

```
## Implementation in Python
We haven't used command line arguments in python yet - but its really easy:

```
import sys

for i in sys.argv[1:]:
	print(i)
```

Again, if you run your program (test.py), and enter command line arguments, they'll print to the screen

```
> python3 test.py hello world
hello
world
>
```

I will assume you know all about two-dimensional arrays in C++, but we haven't discussed them in Python.  There is no real concept for N-dimensional arrays built into Python (although [numpy](http://www.numpy.org/) adds them).  Instead, you must use a *list of lists*.

For example, you can create a 5x5 matrix in Python using the following syntax (all initialized to 0's)
```
rows = 5
cols = 5
matrix = [[0 for x in range(cols)] for x in range(rows)] 
```

You can then access each element using standard bracket notation:

```
matrix[3][2] = 1
print(matrix)
```
The code above prints `[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]`

## Grading
| | | 
|--|--|
|C++ Edit Distance | 30%|
|Python Edit Distance | 30%|
|C++ Backtrace/Alignment Printout|15%|
|Python Backtrace/Alignment Printout|15%|
|Overall Code Quality|10%|


