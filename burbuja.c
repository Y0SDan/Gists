#include <stdio.h>

void burbuja(int arr[], int n);

int main(){
    int i;
    int arr[5];

    for(i = 0; i < 5; i++){
        printf("Ingresa el valor %i:",i);
        scanf("%i",&arr[i]);
    }

    printf("El arreglo original es: \n");
    
    for(i = 0; i < 5; i++){
        printf("%i |",arr[i]);
    }

    burbuja(arr,5);

    printf("\nEl arreglo ordrenado es: \n");

    for(i = 0; i < 5; i++){
        printf("%i |",arr[i]);
    }
}
void burbuja(int arr[], int n) {
   int i, j;
   for (i = 0; i < n-1; i++) {
       for (j = 0; j < n-i-1; j++) {
           if (arr[j] > arr[j+1]) {
              int temp = arr[j];
              arr[j] = arr[j+1];
              arr[j+1] = temp;
           }
       }
   }
}