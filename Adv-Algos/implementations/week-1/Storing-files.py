class FileStorage:
    def __init__(self,N=None,file_lengths=[],frequencies=[]):
        self.N=N
        self.file_lengths = file_lengths
        self.frequencies = frequencies
    
    def get_input(self):
        self.N = int(input())
        self.file_lengths = list(map(int,input().split()))
        freq = input("Entering Frequencies? T/F: ")
        if freq.lower()=="t":
            self.frequencies = list(map(int,input().split()))
    
    def CalculateCost(self,l):
        N = len(l)
        prev = l[0]
        cost = prev
        for i in range(1,N):
            prev = prev + l[i]
            cost += (prev)
        cost = cost/N
        return cost

    def ExpectedCost(self):
        # Mean of costs required to access the files
        if not self.frequencies:
            cost = self.CalculateCost(self.file_lengths)
            self.ExpectedCost = cost
            return cost
        else:
            cost = self.TotalCost(self.file_lengths,self.frequencies)
            self.ExpectedCost = cost
            return cost

    def OptimalExpectedCost(self):
        # If frequencies are not provided, then
        # the files are to be ordered based on file lengths
        if self.frequencies:
            files = sorted([(l,f,l/f) for f,l in zip(self.frequencies,self.file_lengths)],key=lambda x:(x[2]))
            print("Optimal Order :",files)
            lengths_ordered = [v[0] for v in files]
            frequencies_ordered = [v[1] for v in files]
            cost = self.TotalCost(lengths_ordered,frequencies_ordered)/self.N
            self.OptimalExpectedCost = cost
            return cost
    
        else:
            self.Optimal_Ordering = sorted(self.file_lengths)
            cost = self.CalculateCost(self.Optimal_Ordering)
            self.OptimalExpectedCost = cost
            return cost
    
    def TotalCost(self,lengths_ordered,frequencies_ordered=[]):
        if frequencies_ordered:
            # print(lengths_ordered,frequencies_ordered)
            prev = lengths_ordered[0]
            cost = frequencies_ordered[0]*prev
            for i in range(1,len(lengths_ordered)):
                prev = prev+lengths_ordered[i]
                cost+=frequencies_ordered[i]*(prev)
            return cost
        else:
            return self.CalculateCost(lengths_ordered)*len(lengths_ordered)

fileStorage = FileStorage()
fileStorage.get_input()
print(fileStorage.OptimalExpectedCost())
