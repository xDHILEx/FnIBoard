#!/usr/bin/env python3
from itertools import cycle
import re
import argparse

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# Helper Function, orignially part of `FretBoard()`
def fret_len(count, notes=notes):
    string = []
    cy_note = cycle(notes)
    for i, note in enumerate(cy_note):
        if i >= count:
            break
        else:
            string.append(note)
    return string

# Helper Function, originally part of `FretBoard()`
def tuning(note):
    return notes[note:] + notes[:note]

def key(scale, root):
    note = tuning(root)

    if scale == 'Major':
        b = [0, 2, 4, 5, 7, 9, 11]
        c = [note[i] for i in b]
        return(c)
    if scale == 'Natural_Minor':
        b = [0, 2, 3, 5, 7, 8, 10]
        c = [note[i] for i in b]
        return(c)
    if scale == 'Harmonic_Minor':
        b = [0, 2, 3, 5, 7, 8, 11]
        c = [note[i] for i in b]
        return(c)
    if scale == 'Melodic_Minor':
        b = [0, 2, 3, 5, 7, 9, 11]
        c = [note[i] for i in b]
        return(c)

def strings(string):
    return reversed([m.group().upper() for m in re.finditer(r'[a-gA-G]#?', string)])

def interval(string, scale, root):
    for i, v in enumerate(string):
        if v in key(scale, notes.index(root)):
            string[i] = str(key(scale, notes.index(root)).index(v)+1)
    return string

def formatter(string):
    fstring = '{:<2} ||'.format(string[0])
    for x in string[1:]:
        fstring += ' {:<2} |'.format(x)
    return fstring


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fret and Interval Board')
    parser.add_argument('-n','--numFrets', type=int, help='Number of frets your instrument has.', required=True)
    parser.add_argument('-t','--Tuning', type=str, help='Tuning', required=True)
    parser.add_argument('-s','--Scale', type=str, help='Major/Minor', required=False)
    parser.add_argument('-r','--Root', type=str, help='A Note', required=False)
    args = parser.parse_args()

    if args.Scale and args.Root:
        for string in strings(args.Tuning):
            print(formatter(fret_len(args.numFrets, interval(tuning(notes.index(string)), args.Scale, args.Root))))
    else:
        for string in strings(args.Tuning):
            print(formatter(fret_len(args.numFrets, tuning(notes.index(string)))))
