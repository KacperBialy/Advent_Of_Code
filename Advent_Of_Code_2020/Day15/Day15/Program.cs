using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day15
{
    class Program
    {
        static int Game(int nth, params int[] startNums)
        {
            int position = 0;
            int lastNumber = startNums.Last();
            var positions = new int[nth];
            foreach (var number in startNums)
                positions[number] = ++position;

            while (position < nth)
            {
                int lastPosition = positions[lastNumber];
                int nextNumber = lastPosition != 0 ? position - lastPosition : 0;
                positions[lastNumber] = position++;
                lastNumber = nextNumber;
            }

            return lastNumber;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Part 1: " + Game(2020, 1, 3, 2));
            Console.WriteLine("Part 2: " + Game(30000000, 0, 13, 16, 17, 1, 10, 6));
        }
    }
}
