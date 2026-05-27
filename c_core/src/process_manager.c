#include "../include/eduos.h"

PCB process_table[MAX_PROCESSES];

int process_count = 0;

void create_process(char name[], int priority) {

    PCB p;

    p.pid = process_count + 1;

    strcpy(p.name, name);

    p.state = 1;

    p.priority = priority;

    p.burst_time = rand() % 10 + 1;

    p.arrival_time = process_count;

    p.remaining_time = p.burst_time;

    process_table[process_count] = p;

    process_count++;

    printf(
        "Process Created: PID=%d NAME=%s PRIORITY=%d\n",
        p.pid,
        p.name,
        p.priority
    );
}

void display_processes() {

    printf("\n=========== PCB TABLE ===========\n");

    printf(
        "%-5s %-15s %-10s %-10s\n",
        "PID",
        "NAME",
        "STATE",
        "PRIORITY"
    );

    for (int i = 0; i < process_count; i++) {

        printf(
            "%-5d %-15s %-10d %-10d\n",
            process_table[i].pid,
            process_table[i].name,
            process_table[i].state,
            process_table[i].priority
        );
    }

    printf("=================================\n");
}