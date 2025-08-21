def first_negative_subarray(arr,k):
    i=0
    j=0
    data_list = []
    ans = []
    n=len(arr)

    while (j<n):
        if arr[j]<0:
            data_list.append(arr[j])
        # data_list.append(arr[j])

        if j-i+1 < k:
            j += 1
            continue

        elif j-i+1==k:
            if len(data_list) > 0:
                ans.append(data_list[0])
                if arr[i]==data_list[0]:
                    data_list.pop(0)

            else:
                ans.append(0)
            
            i+=1
            j+=1

    return ans
print(first_negative_subarray([3,5,9,-1,2,3,9,9],3))