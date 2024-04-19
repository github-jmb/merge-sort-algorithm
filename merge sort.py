# Code for the merge sort algorithm comes mostly from https://hackr.io/blog/python-projects#intermediate-python-projects-with-source-code 
# exercise # 12 with minor adjustments by me. 

def merge_sort(a_list):
   print("Dividing ", a_list)
  
   if len(a_list) > 1:
       mid_point = len(a_list)//2
       left_half = a_list[:mid_point]
       right_half = a_list[mid_point:]

       merge_sort(left_half)
       merge_sort(right_half)

       i=0
       j=0
       k=0

       while i < len(left_half) and j < len(right_half):
           if left_half[i] <= right_half[j]:
               a_list[k] = left_half[i]
               i += 1
           else:
               a_list[k] = right_half[j]
               j += 1
           k += 1

       while i < len(left_half):
           a_list[k] = left_half[i]
           i += 1
           k += 1

       while j < len(right_half):
           a_list[k] = right_half[j]
           j += 1
           k += 1
  
   print("Merging ", a_list)

n = int(input("Enter how long you want your list: "))

a_list=[]

for i in range(0, n):
    element = int(input())
    a_list.append(element)  

if __name__ == '__main__':
   merge_sort(a_list)
   print(a_list)