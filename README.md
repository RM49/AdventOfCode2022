# AdventOfCode2022
Annoying bug log:

Day 6 part 2:  
  For a list "d" of 4095 length:
   using the loop "for l in d" to iterate through each value, popping values in d in the loop caused the loop to end prematurely resulting in wrong value  
   Issue was fixed after(what feels like) an hour by using a while loop, only then to realise that popping d[0] caused an issue  
   popping the values was part of an unfinished idea before the counter solution, as the idea was to index the final wanted value of the list meaning all duplicates of the wanted letter needed to be removed before. However count was used instead of index.  
  
Day 7:  
  Difficult puzzle. used recursion to total the file sizes. Represented directories in lists and sublists rather than a tree  
Day 8:  
good puzzle, required a lot of thought, created a visibility matrix similar to adjacency matrices in descision maths  
Day 9:  
part 1 took a long time as i unnessessarily overcomplicated the puzzle by trying to simulate the rope moving using expanding 2d arrays(lists of lists). Eventually gave up on that and used a coordinate based solution which was much easier, took around 20 minutes compared to several hours over two seperate weekends.  
