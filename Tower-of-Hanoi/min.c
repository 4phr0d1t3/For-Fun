#include <stdio.h>

void hanoi(int n, char a, char b, char c) {
	if (n != 0) {
		hanoi(n-1, a, c, b);
		printf("%c -> %c\n", a, b); // move
		hanoi(n-1, c, b, a);
	}
}

int main(int argc, char const *argv[]) {
	int n;
	printf("Ingrese el numero de discos: ");
	scanf("%d", &n);

	hanoi(n, 'A', 'C', 'B');

	return 0;
}
