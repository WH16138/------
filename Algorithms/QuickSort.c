#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int partition(char **arr, int left,int right)
{
    char *pivot, *temp;
    int low, high;

    pivot = arr[left];
    low = left+1;
    high = right;
    while (low<=high)
    {
        while (low<=high && strcmp(arr[low], pivot) < 0)
            low++;
        while (low<=high && strcmp(arr[high], pivot) > 0)
            high--;
        if (low<=high)
        {
            temp = arr[low];
            arr[low] = arr[high];
            arr[high] = temp;
            low++;
            high--;
        }
    }
    temp = pivot;
    arr[left] = arr[high];
    arr[high] = temp;

    return high;
}

void quickSort(char** arr, int left, int right)
{
    if (left<right)
    {
        int pivot_index = partition(arr, left, right);
        quickSort(arr, left, pivot_index-1);
        quickSort(arr, pivot_index+1, right);
    }
}

int main()
{
    FILE *file = fopen("name.txt", "r");
    if (file == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    char **names_ptr[1000];
    int count = 0;
    char temp[1000];
    while (fgets(temp, 1000, file) != NULL)
    {
        char *name = (char *)malloc(strlen(temp) + 1);
        strcpy(name, temp);
        names_ptr[count++] = name;
    }
    fclose(file);

    quickSort(names_ptr, 0, count-1);
    
    printf("Sorted names:\n");
    for (int i=0; i<count; i++)
    {
        printf("%s\n", names_ptr[i]);
        free(names_ptr[i]);
    }

    return 0;   
}