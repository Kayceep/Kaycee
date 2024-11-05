# print('prime numbers between 1 to n*/')
# int main()
# (
#   int num, count, i, prime;

#   printf("prime numbers from 1 to 300 are\n");

#   for(num = 1; num <= 300; num++)
#   {
#      printf("%d\t", num);
#   }

#     return 0;
# )


# printing prime number in a given 
# range using python
low=int(input("enter first number : "))
high=int(input("enter last number : "))
for num in range(low,high+1):
  if num>1:
    for i in range(2,num):
      if (num%i)==0:
         break
    else:
        print(num,end=' ')