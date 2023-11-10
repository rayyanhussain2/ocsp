/*
LIFO
All operations are O(1) Time Complexity
*/
#include <stdio.h>

int topS = 0, n = 12;
int S[12];

_Bool isstackEmpty();

int push(int x);

int pop();

int main()
{
    push(1);
    push(2);
    push(3);
    push(4);
    pop();
    push(5);

    for(int i = 0; i < topS; i++)
        printf("%d ", S[i]);
    printf("\n");
    printf("%d\n", isstackEmpty());

    return 0;
}   

_Bool isstackEmpty()
{
    if(topS == 0)
        return 1;
    else
        return 0;
}

int push(int x)
{
    if (topS == n)
    {
        printf("Stack Overflow\n");
        return -1;
    }
    else
    {
        S[topS++] = x;
    }
}

int pop()
{
    if(topS == 0)
    {
        printf("Stack Underflow\n");
        return -1;
    }
    else
    {
        topS -= 1;
        return S[topS];
    }
}