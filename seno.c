#include <stdio.h>

int main() {
   FILE *pipe = popen("gnuplot -persist", "w");
   if (pipe) {
      fprintf(pipe, "plot sin(x)\n");
      fflush(pipe);
      printf("Presione enter para continuar...");
      getchar();
      pclose(pipe);
   }
   return 0;
}