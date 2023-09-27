#include <stdio.h>

void move(char a, char b) {
	printf("%c -> %c\n", a, b);
}

void hanoi(int numOfDisks, char a, char b, char c) {
	if (numOfDisks != 0) {
		hanoi(numOfDisks-1, a, c, b);
		move(a, b);
		hanoi(numOfDisks-1, c, b, a);
	}
}

int main(int argc, char const *argv[]) {
	int numOfDisks;
	printf("Ingrese el numero de discos: ");
	scanf("%d", &numOfDisks);

	hanoi(numOfDisks, 'A', 'C', 'B');

	return 0;
}
