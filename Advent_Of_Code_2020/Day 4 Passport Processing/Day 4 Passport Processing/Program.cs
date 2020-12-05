using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
 
namespace Day_4_Passport_Processing
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = File.ReadAllLines("day4.txt");

            // PART 1

            List<Dictionary<string, string>> passport_dictionary_list = new List<Dictionary<string, string>>();
            Dictionary<string, string> passport_dictionary = new Dictionary<string, string>();

            string[] string_key_val;

            for (int i = 0; i < data.Length; i++)
            {
                if (data[i] != "")
                {
                    string[] data_splited;
                    data_splited = data[i].Split(' ');
                    foreach (string key_val in data_splited)
                    {
                        string_key_val = key_val.Split(':');
                        passport_dictionary.Add(string_key_val[0], string_key_val[1]);
                    }
                }
                else
                {
                    passport_dictionary_list.Add(passport_dictionary);
                    passport_dictionary = new Dictionary<string, string>();
                }
            }
            passport_dictionary_list.Add(passport_dictionary);

            int output_1 = 0;
            for (int i = 0; i < passport_dictionary_list.Count; i++)
            {
                if (passport_dictionary_list[i].ContainsKey("cid"))
                {
                    if (passport_dictionary_list[i].Count == 8)
                    {
                        output_1++;
                    }
                }
                else
                {
                    if (passport_dictionary_list[i].Count == 7)
                    {
                        output_1++;
                    }
                }
            }
            System.Console.WriteLine(output_1);

            // PART 2

            int output_2 = 0;
            for (int i = 0; i < passport_dictionary_list.Count; i++)
            {
                passport_dictionary = passport_dictionary_list[i];
                if (passport_dictionary.ContainsKey("byr"))
                {
                    int byr = int.Parse(passport_dictionary["byr"]);

                    if (byr >= 1920 & byr <= 2002)
                    {
                        if (passport_dictionary.ContainsKey("iyr"))
                        {
                            int iyr = int.Parse(passport_dictionary["iyr"]);

                            if (iyr >= 2010 & iyr <= 2020)
                            {
                                if (passport_dictionary.ContainsKey("eyr"))
                                {
                                    int eyr = int.Parse(passport_dictionary["eyr"]);

                                    if (eyr >= 2020 & eyr <= 2030)
                                    {
                                        if (passport_dictionary.TryGetValue("hgt", out string hgt))
                                        {
                                            bool cm = false;
                                            bool im = false;
                                            bool conntinue = false;
                                            int cm_val = 0;
                                            int im_val = 0;
                                            for (int j = 0; j < hgt.Length; j++)
                                            {
                                                if (hgt[j] == 'c')
                                                {
                                                    cm = true;
                                                    cm_val = int.Parse(hgt.Substring(0, j));
                                                }
                                                if (hgt[j] == 'i')
                                                {
                                                    im = true;
                                                    im_val = int.Parse(hgt.Substring(0, j));
                                                }
                                            }
                                            if (cm == true)
                                            {
                                                if (cm_val >= 150 & cm_val <= 193)
                                                {
                                                    conntinue = true;
                                                }
                                            }
                                            if (im == true)
                                            {
                                                if (im_val >= 59 & im_val <= 76)
                                                {
                                                    conntinue = true;
                                                }
                                            }
                                            if (conntinue)
                                            {
                                                if (passport_dictionary.TryGetValue("hcl", out string hcl))
                                                {
                                                    Regex rx = new Regex("[#]{1}[0-9a-f]{6}");
                                                    if (rx.IsMatch(hcl) & hcl.Length == 7)
                                                    {
                                                        if (passport_dictionary.TryGetValue("ecl", out string ecl))
                                                        {
                                                            if (ecl == "amb" | ecl == "blu" | ecl == "brn" | ecl == "gry" | ecl == "grn" | ecl == "hzl" | ecl == "oth")
                                                            {
                                                                if (passport_dictionary.TryGetValue("pid", out string pid))
                                                                {
                                                                    rx = new Regex("[0-9]{9}");
                                                                    if (rx.IsMatch(pid) & pid.Length == 9)
                                                                    {
                                                                        output_2++;
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            System.Console.WriteLine(output_2);
        }
    }
}
