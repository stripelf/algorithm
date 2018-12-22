#include <stdio.h>

void insert_sort(int array[], const int size) {
    int i=0;
    int j=0; 
    int key=0;
    for (j = 1; j < size; j++) {
        key = array[j];
        for (i = j - 1; i >= 0 && array[i] > key; i--) {
            array[i + 1] = array[i];
        }
        array[i + 1] = key; 
    }
}

void printArray(int A[], const unsigned int size)
{
        int i = 0;
        for (; i<size; i++)
                printf("%d ", A[i]);
        printf("\n");
}


int main() {
    int input[] = {23,4,56,12,13,11,19,7,5,6,3,7,32,27};
    int size=sizeof(input)/sizeof(int);
    insert_sort(input,size); 
    printArray(input,size);
}
