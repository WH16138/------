#include <stdio.h>
#include <stdlib.h>

int main() {

    int t;
    scanf("%d", &t);

    for (int test = 0; test < t; test++) {

        int n, m;
        scanf("%d %d", &n, &m);

        int *array = (int*)malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &array[i]);
        }

        char command[300000];
        scanf("%s", command);

        int multi = 1;
        for (int i = 0; i < n; i++) {
            multi *= array[i];
        }

        char result[300000] = "";
        sprintf(result, "%d", multi % m);


        for (int i = 0; command[i] != '\0'; i++) {
            if (command[i] == 'L') {
                multi = multi / array[0];
                for (int j = 0; j < n-1; j++) {
                    array[j] = array[j+1];
                }
            }
            if (command[i] == 'R') {
                multi = multi / array[n-1];
                n--;
            }
            sprintf(result + strlen(result), " %d", multi % m);
        }
        printf("%s\n", result);
        free(array);
    }
    return 0;
}