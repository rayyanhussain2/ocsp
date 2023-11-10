#include <stdio.h>
#include <math.h>
#define STATE 36

void addBinaryCompare(int* pArray, int n){
    int binary[n];
    for(int i = 0; i < n; i++){
        binary[i] = 0;
    }
    
    //Addition loops keeps adding on for 2^n 
    for(unsigned long long i = 0; i < (unsigned long long) pow(2, n); i++){
        //add one to the binary
        int j = n;
        while(j > 0){
            //if the binary is 0
            if(binary[j] == 0){
                binary[j] = 1;
                for(int k = 0; k < n; k++){
                    printf("%d ", binary[k]);
                }
                printf("\n");
                break;
            }else{
                //if its one
                binary[j] = 0;
            }
            j -= 1;
        }
    }
}

int main(){
    int states[] = {25, 2, 14, 40, 11, 2, 26, 10, 4, 14, 28, 20, 29, 48, 2, 2, 1, 1, 21, 13, 25, 1, 39 , 17, 2, 80, 5, 42, 1, 1, 2, 5, 1, 1, 7, 1};
    
    addBinaryCompare(states, STATE);

    return 0;
}