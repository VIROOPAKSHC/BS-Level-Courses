class Scheduling:
    def __init__(self,timings=None):
        self.timings=timings
    
    def get_input(self):
        N = int(input())
        self.timings = []
        while N:
            self.timings.append(list(map(int,input().split())))
            N-=1
    
    def ShortestClassFirst(self):
        len_Added = [(s,t,t-s) for s,t in self.timings]    
        SubOpt = sorted(len_Added,key=lambda x:x[-1])
        selected = []
        while SubOpt:
            if not selected:
                selected.append(SubOpt[0][:2])
                SubOpt.pop(0)
            s, t = selected[-1]
            while ((SubOpt)):
                s1, t1, _ = SubOpt[0]
                if ((s1<t) and (s < s1)) or ((s>s1) and (s<t1)):
                    SubOpt.pop(0)
                    continue
                selected.append(SubOpt[0][:2])
                SubOpt.pop(0)
                break
        return selected

    def FewestConflictFirst(self):
        # Yet to modify
        conflicts = []
        for i in range(len(self.timings)):
            t = self.timings[i]
            c=[]
            for j in range(len(self.timings)):
                t2 = self.timings[j]
                if j==i:
                    continue
                if ((t[0]<t2[0]) and (t2[0]<t[1])) or ((t2[0]<t[0]) and (t[0]<t2[1])):
                    c.append(t2)
            conflicts.append(t+[c]+[len(c)])
        conflicts = sorted(conflicts,key=lambda x:x[-1])
        selected = []
        
        return selected

            

    def EarlyEndingFirst(self):
        ordered = sorted(self.timings,key=lambda x:x[1])
        selected = []
        while ordered:
            if not selected:
                selected.append(ordered[0])
                ordered.pop(0)
            s, t = selected[-1]
            while ((ordered)):
                s1, t1 = ordered[0]
                if ((s1<t) and (s < s1)) or ((s>s1) and (s<t1)):
                    ordered.pop(0)
                    continue
                selected.append(ordered[0])
                ordered.pop(0)
                break
        return selected

    def EarlyStartingFirst(self):
        ordered = sorted(self.timings,key=lambda x:x[0])
        selected = []
        while ordered:
            if not selected:
                selected.append(ordered[0])
                ordered.pop(0)
            s, t = selected[-1]
            while ((ordered)):
                s1, t1 = ordered[0]
                if ((s1<t) and (s < s1)) or ((s>s1) and (s<t1)):
                    ordered.pop(0)
                    continue
                selected.append(ordered[0])
                ordered.pop(0)
                break
        return selected

scheduling = Scheduling()
scheduling.get_input()
# print("Sub Optimal :",scheduling.ShortestClassFirst())
# print("Sub Optimal :",scheduling.EarlyStartingFirst())
# print("Sub Optimal :",scheduling.FewestConflictFirst())
print("Optimal :",scheduling.EarlyEndingFirst())
