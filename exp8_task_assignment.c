#include <stdio.h>

int main() {
    int tasks, processors;
    int cost[10][10];
    int i, j;

    printf("Enter number of tasks: ");
    scanf("%d", &tasks);

    printf("Enter number of processors: ");
    scanf("%d", &processors);

    printf("Enter cost matrix:\n");

    for (i = 0; i < tasks; i++) {
        for (j = 0; j < processors; j++) {
            scanf("%d", &cost[i][j]);
        }
    }

    printf("\nTask Assignment:\n");

    for (i = 0; i < tasks; i++) {
        int min = cost[i][0];
        int processor = 0;

        for (j = 1; j < processors; j++) {
            if (cost[i][j] < min) {
                min = cost[i][j];
                processor = j;
            }
        }

        printf("Task %d assigned to Processor %d with cost %d\n", i + 1, processor + 1, min);
    }

    return 0;
}

/*
Pip command for this file:
python -m pip install --upgrade pip
Note: This is a C program and does not require Python libraries.
*/
