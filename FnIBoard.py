#!/usr/bin/python3
''' This script aims to help visualize Intervals on fretted multi-stringed
 instruments in any tuning, up to the 23rd fret.
'''
from itertools import islice, cycle

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def FretBoard(*args):
  ''' Returns a list of lists, each of those being a list of notes on a
   fretted instrument String up to the 23rd fret.

   Notes:
    - The index at [0] is the Tuning, consider this an open note.
    - Arguments should be passed backward (highest to lowest) for visual
   clarity.

   print(FretBoard('E', 'B', 'G', 'D', 'A', 'E'))
  '''
  stringsList = []
  for arg in args:
    note = notes.index(arg)
    string = (list(islice(notes,note,None)) + list(islice(notes,note)))*2
    stringsList.append(string)
  return(stringsList)

def IntervalBoard(*args, Scale, Root):
  ''' Returns a list of lists. Similar to the output of FretBoard, but
   replaces matching notes with their corresponding interval number based on
   the mode of Scale and Root note.

   Notes:
    - The index at [0] is the Tuning, consider this an open note.
    - Arguments should be passed backward (highest to lowest) for visual
   clarity.

   #print(IntervalBoard('E', 'B', 'G', 'D', 'A', 'E', Scale='Major', Root='D'))
  '''
  stringsList = FretBoard(*args)
  intervalsList = Key(Scale, Root)
  stringToInterval = []

  for string in stringsList:
    for note in string:
      for index, interval in enumerate(intervalsList):
        if note == interval:
          string[string.index(note)] = note.replace(note, str(index+1))
    stringToInterval.append(string)
  return(stringToInterval)

def Key(Scale, Root):
  ''' Returns a list of notes based on the mode of Scale (Heptatonic), and the
   Root note.

   #print(Key('Major', 'C#'))
  '''
  theKey = [];
  note = notes.index(Root)
  x = cycle(notes[note:] + notes[:note])
  for i in range(12):
    note = next(x)
    theKey.append(note)

  if Scale == 'Major':
    b = [0, 2, 4, 5, 7, 9, 11]
    c = [ theKey[i] for i in b]
    return(c)

  if Scale == 'Minor':
    b = [0, 2, 3, 5, 7, 8, 10]
    c = [ theKey[i] for i in b]
    return(c)

if __name__ == '__main__':
  #print(FretBoard('D', 'A', 'F', 'C', 'G', 'C')) # Drop C tuning
  #print(Key('Minor', 'D#'))
  #print(IntervalBoard('E', 'B', 'G', 'D', 'A', 'D', Scale='Major', Root='D'))
