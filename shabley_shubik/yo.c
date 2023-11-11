#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>

#define MAJORITY 272
#define STATES 36
#define MAX_SIMULATIONS 1000
#define CONFIDENCE_INTERVAL 0.05 // 95% confidence interval
#define SAMPLE_SIZE 10

typedef struct {
    char name[40];
    unsigned long long key;
    int weight;
} state;

void swap(state* pState1, state* pState2) {
    state temp = *pState1;
    *pState1 = *pState2;
    *pState2 = temp;
}

int returnPivotIndex(state* pStates, int size, int value) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += (pStates + i)->weight;
        if (sum >= value) {
            return i;
        }
    }
    return size - 1; // Return the last index if the loop doesn't break early
}

void heapAlgorithm(state* pStates, int size, unsigned long long* pSimulations, double* pResults, int* pCount) {
    int i = 0;
    int simulations = 0;

    while (i < size && simulations < MAX_SIMULATIONS) {
        if (pCount[i] < i) {
            if (i % 2 == 0) {
                swap(pStates + 0, pStates + i);
            } else {
                swap(pStates + pCount[i], pStates + i);
            }

            (pStates + returnPivotIndex(pStates, size, MAJORITY))->key += 1;
            pResults[*pCount] = (double)pStates[0].key / *pSimulations;
            *pSimulations += 1;
            simulations += 1;
            pCount[i] += 1;

            // Check for early stopping with confidence interval
            if (simulations % SAMPLE_SIZE == 0 && simulations > SAMPLE_SIZE) {
                double mean = 0.0;
                for (int j = 0; j < SAMPLE_SIZE; j++) {
                    mean += pResults[simulations - SAMPLE_SIZE + j];
                }
                mean /= SAMPLE_SIZE;

                double variance = 0.0;
                for (int j = 0; j < SAMPLE_SIZE; j++) {
                    variance += pow(pResults[simulations - SAMPLE_SIZE + j] - mean, 2);
                }
                variance /= SAMPLE_SIZE;

                double standardDeviation = sqrt(variance);
                double marginOfError = 1.96 * standardDeviation / sqrt(SAMPLE_SIZE);

                if (marginOfError < CONFIDENCE_INTERVAL) {
                    printf("Simulation stopped early based on confidence interval\n");
                    return;
                }
            }

            i = 0;
        } else {
            pCount[i] = 0;
            i += 1;
        }
    }
}

int main() {
    state states[] = {
        // ... (your state data remains unchanged)
    };

    FILE* pFile = fopen("output.txt", "w");
    unsigned long long simulations = 0;
    double results[MAX_SIMULATIONS];
    int count[STATES];

    for (int i = 0; i < STATES; i++) {
        count[i] = 0;
    }

    fputs("Starting simulation...\n", stdout);

    unsigned long startTime = time(NULL);

    heapAlgorithm(states, STATES, &simulations, results, count);

    unsigned long endTime = time(NULL);
    unsigned long totalTime = (endTime - startTime) / 1000;

    // ... (rest of your code remains unchanged)

    return 0;
}
