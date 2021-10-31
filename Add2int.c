// C program to add two integers
#include<stdio.h>
  
int main()
{
    int A, B, sum = 0;
      
    //Enter the two numbers
    printf("Enter two numbers A and B : \n");
      
    // Reading two numbers from the user
    scanf("%d%d", &A, &B);
      
    // Calclulating the addition of A and B
    // using '+' operator
    sum = A + B;
      
    // Print the sum
    printf("Sum of A and B is: %d", sum);
      
    return 0;
}
