class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))
        s = set()
        for f in folder:
            ok = False
            for p in self.subpaths(f):
                if p in s:
                    ok = True
                    break
            
            if not ok:
                s.add(f)
        
        return list(s)
    
    def subpaths(self, path):
        names = path.split('/')
        paths = ['/' + names[1]]
        for i in range(2, len(names)):
            paths.append(paths[i-2] + '/' + names[i])
        return paths