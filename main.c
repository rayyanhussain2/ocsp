#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

#define MAX 3
#define VALUE 272
#define NUM_THREADS 8
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

typedef struct {
    char name[40];
    int key;
    int weight;
} state;

struct ThreadParams {
    int size;
};

void *thread_function(void *arg);
void priority(state array[]);
void heapPermutation(int size, state *states);

state states[MAX] = {
    {"Andhra Pradesh", 0, 25},
    {"Arunachal Pradesh", 0, 2},
    {"Assam", 0, 14},
    // {"Bihar", 0, 40},
    // {"Chhattisgarh", 0, 11},
    // {"Goa", 0, 2},
    // {"Gujarat", 0, 26},
    // {"Haryana", 0, 20},
};

pthread_t threads[NUM_THREADS];

void priority(state array[]) {
    int sum = 0;
    for (int i = 0; i < MAX; i++) {
        sum += array[i].weight;
        if (sum > VALUE){
            for (int j = 0; j < MAX; j++) {
                if (strcmp(states[j].name, array[i].name) == 0) {
                    states[j].key += 1;
                }
            }
        }
    }
}

void heapPermutation(int size, state *states) {
    if (size == 1) {
        pthread_mutex_lock(&mutex);
        priority(states);
        pthread_mutex_unlock(&mutex);
        return;
    }

 pthread_t local_threads[NUM_THREADS];
    struct ThreadParams *threadParamsArray = malloc(sizeof(struct ThreadParams) * size);

    if (threadParamsArray == NULL) {
        // Handle memory allocation failure
        return;
    }

    for (int i = 0; i < size; i++) {
        threadParamsArray[i].size = size - 1;

        state tmp = states[i];
        states[i] = states[size - 1];
        states[size - 1] = tmp;

        pthread_create(&local_threads[i], NULL, thread_function, (void *)&threadParamsArray[i]);
    }

    for (int j = 0; j < size; j++) {
        pthread_join(local_threads[j], NULL);
    }

    free(threadParamsArray);
}

void *thread_function(void *arg) {
    struct ThreadParams *params = (struct ThreadParams *)arg;
    heapPermutation(params->size, states);
    return NULL;
}

int main() {
    heapPermutation(MAX, states);
    for (int i = 0; i < MAX; i++) {
        printf("%s %d\n", states[i].name, states[i].key);
    }

    // No need to free(states) or free(threads) since they were not dynamically allocated

    return 0;
}