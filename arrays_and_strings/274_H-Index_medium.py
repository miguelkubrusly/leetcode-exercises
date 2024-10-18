# 274. H-Index
# Medium

# Given an array of integers citations where citations[index] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1

# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[index] <= 1000



#PERSONAL NOTES

## number of papers = array.length
## array[index] = citations for this article
## H-index = max(h)
## h = num of papers with >= h citations!
#idea:
## sort desc.
## quantity of valid articles per quantity of citations is equal to index+1 
## the last value in which qty of citations is equal or greater to qty of valid articles will be the max H-index.
## the way I best understood this is thinking that a person with 1000000 articles, with 1 citation each, would have the H-index of one. and the inverse is also true
## so, when sorted desc., the farthest in the list we can secure a qty of citations higher or equal to index+1 (qty of articles) will necessarily be the highest number we can get
## since this will be the point where the other value limits his brother the least (highest acceptable number). we start with the least value of articles and add to it until we can  
######################################################################################
##wrong idea in previous commit, 37c2dbdca71d481c84c245d7f93a80fff1f2d0f5


def hIndex(citations):
  citations.sort(reverse=True)
  n = len(citations)

  h_index = 0
  for index, c in enumerate(citations):
    if c >= index + 1:
      h_index+=1
    else: 
      break

  return h_index

print("Should be 3:")
print(hIndex([3,0,6,1,5]))
print("Should be 1:")
print(hIndex([1,3,1]))
  
