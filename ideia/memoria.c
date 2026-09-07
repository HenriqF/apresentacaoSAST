#include <stdio.h>
#include <stdlib.h>

int main(){

    int* numeros = malloc(10 * sizeof(int));
    free(numeros);
    numeros[0] = 1;

    return 0;
}





