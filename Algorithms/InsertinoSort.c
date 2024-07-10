#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void quickSort(char** arr, int size)
{
    for (int i=0; i<size; i++)
    {
        char *cur = arr[i];
        int j = i-1;
        while (j >= 0 && strcmp(arr[j], cur) > 0)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = cur;
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

    quickSort(names_ptr, count);
    
    printf("Sorted names:\n");
    for (int i=0; i<count; i++)
    {
        printf("%s\n", names_ptr[i]);
        free(names_ptr[i]);
    }

    return 0;   
}