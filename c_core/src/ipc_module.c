#include "../include/eduos.h"
#include <sys/mman.h>
#include <fcntl.h>

void shared_memory_demo() {

    int *shared_mem = mmap(
        NULL,
        sizeof(int),
        PROT_READ | PROT_WRITE,
        MAP_SHARED | MAP_ANONYMOUS,
        -1,
        0
    );

    if (shared_mem == MAP_FAILED) {
        perror("mmap failed");
        return;
    }

    *shared_mem = 100;

    printf("Shared Memory Value: %d\n", *shared_mem);

    munmap(shared_mem, sizeof(int));
}

void pipe_demo() {

    int fd[2];

    if (pipe(fd) == -1) {
        perror("Pipe failed");
        return;
    }

    char message[] = "Pipe communication successful";

    write(fd[1], message, sizeof(message));

    char buffer[100];

    read(fd[0], buffer, sizeof(buffer));

    printf("Received From Pipe: %s\n", buffer);

    close(fd[0]);
    close(fd[1]);
}