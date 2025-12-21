class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(l,r,arr):
            pivot = arr[r][0]
            i = l-1
            for j in range(l,r):
                if arr[j][0] <=pivot:
                    i+=1
                    arr[i],arr[j] = arr[j],arr[i]
            arr[i+1],arr[r] = arr[r],arr[i+1]
            return i+1
        freq = Counter(nums)
        freq_arr = []
        for ki in freq:
            freq_arr.append([freq[ki],ki])
        l=0
        r=len(freq_arr)-1
        target = len(freq_arr) - k
        while(l<r):
            pivot = partition(l,r,freq_arr)
            if pivot==target:
                break
            if pivot>target:
                r = pivot-1
            else:
                l = pivot +1
        
        ret = []
        print(freq_arr)
        for p,q in freq_arr[target:]:
            ret.append(q)
        return ret

