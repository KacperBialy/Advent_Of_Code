using System.IO;
using System.Text.RegularExpressions;
namespace day18
{
    class Program
    {
        static void Main(string[] args)
        {
            long sum = 0;
            Regex regx = new Regex(@"\([^\(\)]*\)");
            Regex regxNumber = new Regex(@"[0-9]+");
            string[] inputLines = File.ReadAllLines("day18.txt");
            foreach (string input_line in inputLines)
            {
                string input = input_line;
                int index = 0;
                while (true)
                {
                    Match match = regx.Match(input);
                    string line = match.Value;
                    long leftValue;
                    if (match.Success)
                    {
                        MatchCollection matches = regxNumber.Matches(line);
                        leftValue = long.Parse(matches[0].Value);
                        for (int i = 1; i < matches.Count; i++)
                        {
                            long rightValue = long.Parse(matches[i].Value);
                            char sign = line[matches[i].Index - 2];
                            if (sign == '+')
                                leftValue += rightValue;
                            else
                                leftValue *= rightValue;
                        }
                        input = input.Substring(0, match.Index) + leftValue + input.Substring(match.Index + match.Length);
                        index++;
                    }
                    else
                    {
                        MatchCollection matches = regxNumber.Matches(input);
                        leftValue = long.Parse(matches[0].Value);
                        for (int i = 1; i < matches.Count; i++)
                        {
                            int rightValue = int.Parse(matches[i].Value);
                            char sign = input[matches[i].Index - 2];
                            if (sign == '+')
                                leftValue += rightValue;
                            else
                                leftValue *= rightValue;
                        }
                        sum += leftValue;
                        break;
                    }
                }
            }

            System.Console.WriteLine(sum);
        }
    }
}
