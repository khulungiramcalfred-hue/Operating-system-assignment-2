#include "../include/eduos.h"

int main() {

    srand(time(NULL));

    print_banner();

    log_message("EduOS Simulator Started");

    create_process("init_process", 1);

    create_process("calculator.exe", 3);

    create_process("browser.exe", 2);

    display_processes();

    shared_memory_demo();

    pipe_demo();

    log_message("EduOS Simulator Finished");

    return 0;
}