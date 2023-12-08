#include <stdio.h>

int main(int argc, char **argv)
{
    FILE *fp = fopen("./input.txt", "r");
    if (!fp) {
        fprintf(stderr, "Failed to open input\n");
        return 1;
    }

    char c;
    int first = -1;
    int last = -1;
    int ans = 0;

    while ((c = fgetc(fp)) != EOF) {
        if (c == '\n') {
            //printf("\t f=%i,l=%i\n", first, last);
            if (first > -1 && last > -1) {
                ans += first * 10 + last;
            }

            first = last = -1;

            continue;
        }

        //printf("%c", c);
        if (c >= '0' && c <= '9') {
            c -= '0';
            if (first == -1) {
                first = c;
            }

            last = c;
        }
    }

    printf("%i\n", ans);

    return 0;
}
