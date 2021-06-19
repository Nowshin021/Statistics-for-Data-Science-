#%% Count
def countData(a):
    c=0
    for i in a:
        if(i is not None):
            c+=1
            
    return c

#%% Describe
def descData(a):
    
    count=countData(a)
    mean=calcMean(a)
    std=calcStd(a)
   
    q1=calcQuantile(a,0.25)
    median=calcQuantile(a,0.50)
    q3=calcQuantile(a,0.75)
    minimum=calcMinimum(a)
    maximum=calcMaximum(a)
        
    print('Count'       , count)
    print("Mean     %.6f" %mean)
    print('std      %.6f' %std)
    print('min      %.6f' %minimum)
    print('25%','      %.6f' %q1)
    print('50%','      %.6f' %median)
    print('75%','      %.6f' %q3)
    print('max','      %.6f' %maximum)

#%% Minimum
def calcMinimum(nums):
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
    
#%% Maximum
def calcMaximum(nums):
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum

#%% Arg Minimum
def calcArgMinimum(a):
    min1=100000000000
    for i in range(0,len(a)):
        if(a[i]<min1):
            min1=a[i]
            idx=i
    return idx
    
#%% Arg Maximum
def calcArgMaximum(a):
    max1=-100000000000
    for i in range(0,len(a)):
        if(a[i]>max1):
            max1=a[i]
            idx=i
    return idx

#%% Idx Minimum
def calcIdxMinimum(a):
    mini=a[0]
    min_index =0
    for i in range(len(a)):
        if (a[i] < mini):
            mini=a[i]
            min_index=i
    return min_index
    
#%% Idx Maximum
def calcIdxMaximum(a):
    mx=a[0]
    max_index =0
    for i in range(len(a)):
        if (a[i] > mx):
            mx=a[i]
            max_index=i
    return max_index


#%% Quantile
def calcQuantile(a,q):
    b=a
    b=b.sort_values()
    b=b.reset_index(drop=True)
    n=len(b)
    
    return b[int(n*q)]

#%% Sum
def calcSum(a):
    sum=0
    for i in a :
        sum+=i
    return sum

#%% Mean
def calcMean(a):
    sum=0
    for i in a:
        sum+=i
        
    n=len(a)
    return sum/n

#%% Median
def calcMedian(a):
    median=0
    a= sorted(a)  
    n=len(a)
    if n % 2 == 0:
        median1 = a[n//2]
        median2 = a[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = a[n//2]
    return median

#%% Product
def calcProduct(nums):
    product = 1
    for num in nums:
        product *= num
    return product

#%% Mean Absolute Deviation
def calcMad(nums):
    mean = calcMean(nums)
    n = len(nums)
    result = 0
    for num in nums:
        result += abs(num - mean)
    return result / n

#%% Variance
def calcVariance(a):
    M=calcMean(a)
    var=0
    for i in range(len(a)):
        var = var + (a[i]-M)**2
    result=var/(len(a)-1)
    return result

#%% Standard Deviation
def calcStd(a):
    return (calcVariance(a)**0.5)

#%% Skewness
def calcSkewness(a):
    m=calcMean(a)
    s=calcStd(a)
    n=len(a)
    
    result=[(i-m)**3 for i in a]
    sum1= calcSum(result)
    
    return (sum1/((n-1)*(s**3)))

#%% Kurtosis
def calcKurtosis(nums):
    mean = calcMean(nums)
    std = calcStd(nums)
    n = len(nums)
    
    result = [(num - mean) ** 4 for num in nums]
    numerator = calcSum(result)
    denominator = (n - 1) * (std ** 4)
    
    return numerator / denominator - 3

#%% Cumulative Sum
def calcCumSum(a):
    new_list=[]
    j=0
    for i in range(0,len(a)):
        j=j+a[i]
        new_list.append(j)
    return new_list

#%% Cumulative Minimum
def calcCumMin(nums):
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(nums[i])
        else:
            result.append(min(result[i-1], nums[i]))
    return result

#%% Cumulative Maximum
def calcCumMax(a):
    b=[]
    c=[]
    
    for i in a:
        b.append(i)
        c.append(max(b))

    return c

#%% Cumulative Product
def calcCumProd(a):
    a_list=[]
    j=1
    for i in a:
        j=j * i
        a_list.append(j)
    return a_list

#%% Print Cumulative Data
import time
def printCumulative(nums):
    for i in range(len(nums)):
        print(i, '  ', nums[i])


#%% Arithmatic Difference
def calcDiff(a):
    b=[None]
    for i in range(1,len(a)):
        b.append(a[i]-a[i-1])
        
    return b

#%% Percent Changes
def calcPctChange(nums):
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(None)
        else:
            result.append(round((nums[i] - nums[i-1]) / nums[i-1], 6))
    return result

