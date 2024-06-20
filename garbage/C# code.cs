using System;

class Codeforces
{
    static void Main(string[] args)
    {
        int t = int.Parse(Console.ReadLine());

        for (int test = 0; test < t; test++) {
            string[] input = Console.ReadLine().Split();
            int n = int.Parse(input[0]);
            int m = int.Parse(input[1]);
            int[] array = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            string command = Console.ReadLine();

            int multi = 1;
            foreach (int a in array) {
                multi *= a;
            }

            string result = (multi % m).ToString();

            foreach (char c in command) {
                if (c == 'L') {
                    multi /= array[0];
                    Array.Copy(array, 1, array, 0, array.Length-1);
                    Array.Resize(ref array, array.Length-1);
                } if (c == 'R') {
                    multi /= array[array.Length-1];
                    Array.Resize(ref array, array.Length-1);
                }
                result += " " + (multi % m).ToString();
            }
            Console.WriteLine(result);
        }
    }
}