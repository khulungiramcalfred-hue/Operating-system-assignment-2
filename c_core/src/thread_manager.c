#include "../include/eduos.h"

int counter = 0;

pthread_mutex_t lock;

void* increment_counter(void* arg) {

    for (int i = 0; i < 100000; i++) {

#ifdef RACE

        counter++;

#else

        pthread_mutex_lock(&lock);

        counter++;

        pthread_mutex_unlock(&lock);

#endif
    }

    return NULL;
}

int main() {

    pthread_t t1, t2, t3, t4;

#ifndef RACE
    pthread_mutex_init(&lock, NULL);
#endif

    pthread_create(&t1, NULL, increment_counter, NULL);
    pthread_create(&t2, NULL, increment_counter, NULL);
    pthread_create(&t3, NULL, increment_counter, NULL);
    pthread_create(&t4, NULL, increment_counter, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);
    pthread_join(t4, NULL);

    printf("Final Counter Value: %d\n", counter);

#ifndef RACE
    pthread_mutex_destroy(&lock);
#endif

    return 0;
}