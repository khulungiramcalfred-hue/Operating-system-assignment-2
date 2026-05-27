#include "../include/eduos.h"

void log_message(const char *message) {

    FILE *fp = fopen("../logs/eduos.log", "a");

    if (fp == NULL) {
        printf("Error opening log file\n");
        return;
    }

    fprintf(fp, "[%ld] %s\n", time(NULL), message);

    fclose(fp);
}