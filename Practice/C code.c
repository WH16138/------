#include <stdio.h>

void SelectionSort(int* arr, int left, int right, int n)
{
    int pivot, i, j, temp;
    for (i = left; i < right; i++)
    {
        pivot = i;
        for (j = i + 1; j < right; j++)
        {
            if (arr[j] < arr[pivot])
                pivot = j;
        }
        temp = arr[pivot];
        arr[pivot] = arr[i];
        arr[i] = temp;
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
}

int main()
{
    int n;
    int* arr;
    arr = (int)malloc(sizeof(int) * n);
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    SelectionSort(arr, 0, n, n);

    free(arr);
    return 0;
}