using System;
using System.Collections.Generic;

class CodeForces
{
    static void Main()
    {
        int n, q;
        string[] input = Console.ReadLine().Split();
        n = int.Parse(input[0]);
        q = int.Parse(input[1]);

        List<int> tower1 = new List<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
        List<int> power1 = new List<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
        List<int> pipe1 = new List<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
using System;
using System.Collections.Generic;

class CodeForces
{
    static void Main()
    {
        int n, q;
        string[] input = Console.ReadLine().Split();
        n = int.Parse(input[0]);
        q = int.Parse(input[1]);

        List<int> tower = new List<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
        List<int> power = new List<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
        List<int> pipe = new List<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));

        for (int i = 0; i < q; ++i)
        {
            int[] update = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            UpdateLists(tower, power, pipe, update);
            int wine = CalculateWine(tower, power, pipe, n);
            Console.WriteLine(wine);
        }
    }

    static void UpdateLists(List<int> tower, List<int> power, List<int> pipe, int[] update)
    {
        int index = update[0] - 1;
        tower[index] = update[1];
        power[index] = update[2];

        if (index != tower.Count - 1)
        {
            pipe[index] = update[3];
        }
    }

    static int CalculateWine(List<int> tower, List<int> power, List<int> pipe, int n)
    {
        int wine = 0;

        for (int j = 0; j < n; ++j)
        {
            int convert = Math.Min(tower[j], power[j]);
            tower[j] -= convert;
            wine += convert;

            if (j != n - 1)
            {
                int flow = Math.Min(tower[j], pipe[j]);
                tower[j] -= flow;
                tower[j + 1] += flow;
            }
        }

        return wine;
    }
}

        for (int i = 0; i < q; ++i)
        {
            int[] update = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            tower1[update[0]-1] = update[1];
            power1[update[0]-1] = update[2];
            if (update[0] != n){pipe1[update[0]-1] = update[3];}

            int wine = 0;
            List<int> tower = new List<int>(tower1);
            List<int> power = new List<int>(power1);
            List<int> pipe = new List<int>(pipe1);

            for (int j = 0; j < n; ++j)
            {
                int convert = Math.Min(tower[j], power[j]);
                tower[j] -= convert;
                wine += convert;
                if (j != n - 1)
                {
                    int flow = Math.Min(tower[j], pipe[j]);
                    tower[j] -= flow;
                    tower[j + 1] += flow;
                }
            }

            Console.WriteLine(wine);
        }
    }
}
