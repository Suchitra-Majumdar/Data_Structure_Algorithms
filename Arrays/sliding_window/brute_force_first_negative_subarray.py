def first_negative_subarray(arr,k):
    n= len(arr)
    ans = []

    for i in range(n-k+1):
        neg_found = False
        for j in range(i,i+k):
            if arr[j]<0:
                ans.append(arr[j])
                neg_found = True
                break
        if neg_found == False:
            ans.append(0)
    return ans
print(first_negative_subarray([3,5,9,-1,2,3,9,9],3))