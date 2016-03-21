# FnIBoard
A basic visual aide for music theory Intervals on fretted instruments.

##### Use case:

` python3 FnIBoard.py -n=24 -t=EADGBE`: Standard Tuning (Guitar)
```
E  || F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# | E  | F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# |
B  || C  | C# | D  | D# | E  | F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# | E  | F  | F# | G  | G# | A  | A# |
G  || G# | A  | A# | B  | C  | C# | D  | D# | E  | F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# | E  | F  | F# |
D  || D# | E  | F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# | E  | F  | F# | G  | G# | A  | A# | B  | C  | C# |
A  || A# | B  | C  | C# | D  | D# | E  | F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# | E  | F  | F# | G  | G# |
E  || F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# | E  | F  | F# | G  | G# | A  | A# | B  | C  | C# | D  | D# |
```

`python3 FnIBoard.py -n=24 -t=EADGBE -s=Natural_Minor -r=E`: E Natural Minor Intervals in Standard Tuning (Guitar)
```
1  || F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# |
5  || 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# | 4  | A# |
3  || G# | 4  | A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  |
7  || D# | 1  | F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# |
4  || A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# |
1  || F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# | 1  | F  | 2  | 3  | G# | 4  | A# | 5  | 6  | C# | 7  | D# |
```

##### Flags:
Flags `-n` and `-t` are required:
* `-n`: Number of frets on instrument
* `-t`: Tuning of strings

Flags `-s` and `-r` are optional, and are used to retrieve the interval:
* `-s`: The mode of scale
* `-r`: The root note
