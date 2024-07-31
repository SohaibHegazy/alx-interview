#!/usr/bin/python3
'''
a Module with a method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
  '''
  a method that determines if all the boxes can be opened
  '''

  if not boxes or type(boxes) is not list:
        return False
  
  unlocked = [0]

  for box in unlocked:
      for key in boxes[box]:
          if key not in unlocked and key < len(boxes):
              unlocked.append(key)
  return len(unlocked) == len(boxes)
