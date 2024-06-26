#include <stdio.h>

void SelectionSort(int* arr, int n)
{
    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] > arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main()
{
    int n;
    scanf("%d", &n);

    int* arr;
    arr = (int*)malloc(sizeof(int)*n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    SelectionSort(arr, n);
    for (int i = 0; i < n; i++)
        printf("%d\n", arr[i]);

    free(arr);
    return 0;
}