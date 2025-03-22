using System;
using System.Text;
    
internal class B
{
    static void Main(string[] args)
    {
        var t = Console.ReadLine();
        var q = int.Parse(Console.ReadLine());
        for (int i = 0; i < q; i++)
        {
            var s = Console.ReadLine();
            var (cnt, result) = zFunction(s, t);
            if (cnt == 0) Console.WriteLine(cnt);
            else Console.WriteLine($"{cnt} {result}");
        }
    }

    private static (int, string) zFunction(string s, string t)
    {
        var cnt = 0;
        var str = $"{s}${t}";
        var result = new StringBuilder();
        var zf = new int[str.Length];
        int l = 0, r = 0;
        for (int i = 1; i < str.Length; i++)
        {
            zf[i] = Math.Max(0, Math.Min(r - i, zf[i - l]));
            while (i + zf[i] < str.Length && str[zf[i]] == str[zf[i] + i])
            {
                zf[i]++;
            }

            if (zf[i] + i > r)
            {
                l = i;
                r = i + zf[i];
            }

            if (zf[i] == s.Length)
            {
                result.Append((i - s.Length - 1).ToString() + " ");
                cnt++;
            }
        }

        return (cnt, result.ToString());
    }
}