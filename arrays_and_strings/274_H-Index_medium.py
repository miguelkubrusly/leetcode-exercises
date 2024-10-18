# 274. H-Index
# Medium

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

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
# 0 <= citations[i] <= 1000



#PERSONAL NOTES

## number of papers = array.length
## array[i] = citations for this article
## H-index = max(h)
## h = num of papers with >= h citations!
#idea:
##1- check numbers, from highest to lowest value, until we find h
###1.1-sort in descendent order
###1.2- check how many papers they have higher than current citation value in iteration
###1.3-if num of papers with citations higher than current == num of citations: there is you h 
##2- since h was found in desc order, h is the max h

######################################################################################


def hIndex( citations: list[int]) -> int:
  citations.sort(reverse=True)
  # possible_hs = []
  max_h = 0
  for i, this_citation in enumerate(citations):
    h = 0
    for next_citation in citations[i+1:]:
      if next_citation >= this_citation:
        h+=1
      if this_citation>=h:
        max_h=max(max_h,this_citation)
      print(f"h: {h}; max_h: {max_h}; citations[i+1:]: {citations[i+1:]}; this_citation: {this_citation}; next_citation: {next_citation}; i: {i}")
  return max_h

print(hIndex([3,0,6,1,5]))