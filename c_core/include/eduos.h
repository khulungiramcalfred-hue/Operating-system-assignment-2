#ifndef EDUOS_H
#define EDUOS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

#define MAX_PROCESSES 100

typedef struct {
    int pid;
    char name[50];
    int state;
    int priority;
    int burst_time;
    int arrival_time;
    int remaining_time;
} PCB;

/* process manager */
void create_process(char name[], int priority);
void display_processes();

/* logger */
void log_message(const char *message);

/* utilities */
void print_banner();

/* IPC */
void shared_memory_demo();
void pipe_demo();

#endif