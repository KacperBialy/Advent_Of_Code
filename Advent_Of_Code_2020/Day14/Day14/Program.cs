using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace Day14
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("day14.txt");
            Dictionary<int, char> maskDict = new Dictionary<int, char>();
            Dictionary<int, long> memDict = new Dictionary<int, long>();

            foreach (string line in lines)
            {
                string[] key_value = line.Replace(" ", "").Split('=');
                if (key_value[0] == "mask")
                {
                    maskDict = new Dictionary<int, char>();
                    for (int i = 0; i < key_value[1].Length; i++)
                    {
                        if (key_value[1][i] != 'X')
                        {
                            maskDict[i] = key_value[1][i];
                        }
                    }
                }
                else
                {
                    int start = key_value[0].IndexOf('[');
                    int stop = key_value[0].IndexOf(']');
                    int index = int.Parse(key_value[0].Substring(start + 1, stop - start - 1));
                    long mem_value = long.Parse(key_value[1]);

                    string binary_value_string = Convert.ToString(mem_value, 2);
                    binary_value_string = binary_value_string.PadLeft(36, '0');

                    StringBuilder binary_value_stringBuilder = new StringBuilder(binary_value_string);
                    foreach (var kvp in maskDict)
                    {
                        binary_value_stringBuilder[kvp.Key] = kvp.Value;
                    }
                    long value_mem = Convert.ToInt64(binary_value_stringBuilder.ToString(),2);
                    memDict[index] = value_mem;
                }
            }
            long sum = 0;

            foreach (var kvp in memDict)
            {
                sum += kvp.Value;
                Console.WriteLine(kvp.Value);
            }
            Console.WriteLine(sum);
        }

    }
}
