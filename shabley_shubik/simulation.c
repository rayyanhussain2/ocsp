#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

#define MAJORITY 272
#define STATES 36

typedef struct {
    char name[40];
    unsigned long long key;
    int weight;
} state;

void swap(state* pState1, state* pState2) {
    state temp;
    temp.key = pState1 -> key;
    temp.weight = pState1 -> weight;
    strcpy(temp.name, pState1 -> name);

    //Copying state2 to state1
    pState1 -> key = pState2 -> key;
    pState1 -> weight = pState2 -> weight;
    strcpy(pState1 -> name, pState2 -> name);

    //copying temp to state2
    pState2 -> key = temp.key;
    pState2 -> weight = temp.weight;
    strcpy(pState2 -> name, temp.name);
    
    return;
}

int returnPivotIndex(state* pStates, int size, int value){
    int sum = 0;
    for(int i = 0; i < size; i++){
        sum += (pStates + i) -> weight;
        if(sum >= value){
            return i;
        }
    }
}

void heapAlgorithm(state* pStates, int size, unsigned long long* pSimulations){
    int count[size];
    for(int i = 0; i < size; i++){
        count[i] = 0;
    }

    //Call for the check pivot function
    (pStates + returnPivotIndex(pStates, size, MAJORITY)) -> key += 1;
    *pSimulations += 1;
    
    int i = 0;
    while(i < size){
        if(count[i] < i){
            if(i % 2 == 0){
                swap(pStates + 0, pStates + i);
            }else{
                swap(pStates + count[i], pStates + i);
            }

            (pStates + returnPivotIndex(pStates, size, MAJORITY)) -> key += 1;
            *pSimulations += 1;

            //every size simulation, check for confidence interval
            if(*pSimulations % STATES == 0){
                //Calculating the mean
                double mean = 0;
                for(int j = 0; j < STATES; j++){
                    mean += (pStates + j) -> key; 
                }
                mean /= STATES;
                printf("Mean: %f\n", mean);

            }

            count[i] += 1;
            i = 0;
        }else{
            count[i] = 0;
            i += 1;
        }
    }
}

int main() {
    state states[] = {
    {"Andhra Pradesh", 0, 25},
    {"Arunachal Pradesh", 0, 2},
    {"Assam", 0, 14},
    {"Bihar", 0, 40},
    {"Chhattisgarh", 0, 11},
    {"Goa", 0, 2},
    {"Gujarat", 0, 26},
    {"Haryana", 0, 20},
    {"Himachal Pradesh", 0, 4},
    {"Jharkhand", 0, 14},
    {"Jharkhand", 0, 14},
    {"Karnataka", 0, 28},
    {"Kerala", 0, 20},
    {"Madhya Pradesh", 0, 29},
    {"Maharashtra", 0, 48},
    {"Manipur", 0, 2},
    {"Meghalaya", 0, 2},
    {"Mizoram", 0, 1},
    {"Nagaland", 0, 1},
    {"Odisha", 0, 21},
    {"Punjab", 0, 13},
    {"Rajasthan", 0, 25},
    {"Sikkim", 0, 1},
    {"Tamil Nadu", 0, 39},
    {"Telangana", 0, 17},
    {"Tripura", 0, 2},
    {"Uttarakhand", 0, 5},
    {"Uttar Pradesh", 0, 80},
    {"West Bengal", 0, 42},
    {"Andaman and Nicobar Islands", 0, 1},
    {"Chandigarh", 0, 1},
    {"Dadra and Nagar Haveli", 0, 1},
    {"Daman and Diu", 0, 1},
    {"Lakshadweep", 0, 1},
    {"Delhi", 0, 7},
    {"Puducherry", 0, 1}
};
    FILE* pFile = fopen("output.txt", "w");
    unsigned long long simulations = 0;

    fputs("Starting simulation...\n", stdout);

    unsigned long startTime = time(NULL);
    
    heapAlgorithm(states, STATES, &simulations);

    unsigned long endTime =  time(NULL);
    unsigned long totalTime = (endTime - startTime)/1000;

    fputs("Simulation comlpeted!\n", stdout);
    printf("%lli simulations ran in %li seconds\n", simulations, totalTime);
    
    fputs("Simulation Results: \n\n", pFile);
    for(int i = 0; i < STATES; i++){
        fprintf(pFile, "%s: %llu\n", states[i].name, states[i].key);
    }
    fprintf(pFile, "\nTotal simulations: %llu\n", simulations);
    fprintf(pFile, "Runtime: %lu seconds\n", totalTime);
    fputs("Results dumped in output.txt\n", stdout);

    return 0;
}