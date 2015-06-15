#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define LEFT 1
#define ABOVE 2
#define DIAG 0

int min_of_three(int above, int left, int diag){
	if ( above <= left && above <= diag ) return above;
	if ( left <= above && left <= diag ) return left;
	return diag;
}
int direction_of_three(int above, int left, int diag){
	if ( above <= left && above <= diag ) return ABOVE;
	if ( left <= above && left <= diag ) return LEFT;
	return DIAG;
}


char * read_file(char * filename){
	char * buffer = 0;
	long length;
	FILE * f = fopen (filename, "rb");

	if (f)
	{
	  fseek (f, 0, SEEK_END);
	  length = ftell (f);
	  fseek (f, 0, SEEK_SET);
	  buffer = malloc (length);
	  if (buffer)
	  {
	    fread (buffer, 1, length, f);
	  }
	  fclose (f);
	}
	return buffer;
}
int main()  {
	char * across = 0;
	char * down = 0 ;
	int rows, cols, r, c, i;
	int t;
	
	t = clock();
	across = "GGAAGGGGCGATCGGAGGGC";//read_file("nras_human.txt");//"kitten";
	down = "GGTAAGGGGCCTGATCGAAGGGCAA";//read_file("nras_cow.txt");//"sitting";
	rows = strlen(down) + 1;
	cols = strlen(across) + 1;


	int **D = (int **)malloc(sizeof (int) * rows);
	int **E = (int **)malloc(sizeof (int) * rows);
	for (r = 0; r < rows; r++) {
		D[r] = (int*)malloc(sizeof(int) * cols);
		E[r] = (int*)malloc(sizeof(int) * cols);
	}

	for (r = 0; r < rows; r++) D[r][0] = r;
	for (c = 0; c < cols; c++) D[0][c] = c;

	for (c = 1; c < cols; c++){
		for ( r = 1; r < rows; r++) {
			if ( across[c-1] == down[r-1]) {
				D[r][c] = D[r-1][c-1];
				E[r][c] = DIAG;
			}
			else {
				D[r][c] = min_of_three(D[r-1][c], D[r][c-1], D[r-1][c-1]) + 1;
				E[r][c] = direction_of_three(D[r-1][c], D[r][c-1], D[r-1][c-1]);
			}
		}
	}

	t = clock()-t;

	
	for (r = 0; r < rows; r++) {
		for (c = 0; c < cols; c++ ) {
			printf("%d  ", D[r][c]);
		}
		printf("\n");
	}
	/*
	printf("----------------------------\n");
	for (r = 0; r < rows; r++) {
		for (c = 0; c < cols; c++ ) {
			if (E[r][c] == ABOVE) {
				printf("^  ");
			}
			else if (E[r][c] == LEFT) {
				printf("<  ");
			}
			else {
				printf("@  ");
			}
		}
		printf("\n");
	}
	*/
	char * across_buff = (char *) malloc(rows + cols);
	char * down_buff = (char *) malloc(rows+cols);
	memset(across_buff, rows+cols, 0);
	memset(down_buff, rows+cols, 0);
	int a = rows+cols-1;
	int d = rows+cols-1;

	r = rows-1;
	c = cols-1;
	while (r >= 0 && c >= 0) {
		if (E[r][c] == DIAG) {
			across_buff[a--] = across[c-1]; c--;
			down_buff[d--] = down[r-1]; r--;
		}
		else if (E[r][c] == LEFT){
			across_buff[a--] = across[c-1]; c--;
			down_buff[d--] = '-'; 
		}
		else {
			across_buff[a--] = '-'; 
			down_buff[d--] = down[r-1]; r--;
		}
	}
	while ( r >= 0 ) {
		down_buff[d--] = down[r-1]; r--;
	}
	while ( c >= 0 ) {
		across_buff[a--] = across[c-1]; c--;
	}
	
	printf("Input Sequences\n");
	printf("----------------------------\n");
	printf("%s\n", across);
	printf("%s\n", down);
	printf("----------------------------\n");
	
	printf("Aligned Sequences\n");
	printf("----------------------------\n");
	for (i = 0; i < rows+cols; i++ ) {
		printf("%c", across_buff[i]);
	}
	printf("\n");
	for (i = 0; i < rows+cols; i++ ) {
		printf("%c", down_buff[i]);	
	}
	printf("\n");
	printf("----------------------------\n");

	printf("The minimum edit distance is %d\n", D[rows-1][cols-1]);
	printf ("Completed in %f seconds.\n",((float)t)/CLOCKS_PER_SEC);
}