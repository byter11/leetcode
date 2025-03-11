public class Solution {
    public IList<string> RestoreIpAddresses(string s) 
    {
        List<string> results = new();

        if(s.Length > 12) return results;
        
        foreach (List<int> indices in ValidIndices(s)) {
            string[] bytes = new string[4];
            bytes[0] = s.Substring(0, indices[0]);
            bytes[1] = s.Substring(indices[0], indices[1] - indices[0]);
            bytes[2] = s.Substring(indices[1], indices[2] - indices[1]);
            bytes[3] = s.Substring(indices[2]);

            bool ok = true;
            for (int i=0; i<=3; i++) {
                if (int.Parse(bytes[i]) > 255 || 
                    (bytes[i].Length > 1 && bytes[i][0] == '0')
                )
                ok = false;
            }
            if (!ok) continue;
            results.Add($"{bytes[0]}.{bytes[1]}.{bytes[2]}.{bytes[3]}");
        }

        return results;
    }

    private IEnumerable<List<int>> ValidIndices(string s) {
        for (int i = 1; i <= s.Length - 3; i++) {
            for (int j = i + 1; j <= s.Length - 2; j++) {
                for (int k = j + 1; k <= s.Length - 1; k++) {
                    yield return new List<int>([i,j,k]);
                }
            }
        }
    }
}