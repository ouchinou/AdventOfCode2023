#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#define NMAX     1000
#define N_STEP      7
#define NB_RANGE   50

bool isMapped = false;
unsigned int nb_seeds = 0;

typedef struct {
    long input[NMAX];
    long output[NMAX];
} data_set_t;

typedef struct {
    long dest_start[NB_RANGE];
    long src_start[NB_RANGE];
    long len[NB_RANGE];
} range_set_t;

static void process(data_set_t * data, range_set_t * range, const unsigned int * nb, int indx)
{
    for (int i = 0; i < N_STEP-1; i++)
    {
        for(int j = 0 ; j < nb[i]; j++)
        {
            if((range[i].src_start[j] <= data[i].input[indx]) && (data[i].input[indx] < range[i].src_start[j]+range[i].len[j]))
            {
                data[i+1].input[indx] = data[i].input[indx] + (range[i].dest_start[j]-range[i].src_start[j]);
                isMapped = true;
            }
        }

        if(!isMapped)
            data[i+1].input[indx] = data[i].input[indx];
        
        isMapped = false;
    }

    for(int j = 0 ; j < nb[6]; j++)
    {
        if((range[6].src_start[j] <= data[6].input[indx]) && (data[6].input[indx] < range[6].src_start[j]+range[6].len[j]))
        {
            data[6].output[indx] = data[6].input[indx] + (range[6].dest_start[j]-range[6].src_start[j]);
            isMapped = true;
        }
    }
    if(!isMapped)
        data[6].output[indx] = data[6].input[indx];
        
    isMapped = false;
}

int main()
{
    FILE *fptr;

    data_set_t data_set[N_STEP];
    range_set_t range_set[N_STEP];

    unsigned int nb_line[N_STEP];
    unsigned int line = 0;
    char * end_ptr;
    char * ptr;

    int index = 0;
    int k = 0;
    int n_step = -1;
    int i;
    long min = 1381149926;

    // Open a file in read mode
    fptr = fopen("../input.txt", "r");

    // Store the content of the file
    char myString[NMAX];

    // If the file exist
    if(fptr != NULL)
    {
        // Read the content and print it
        // "for line in text:" equivalent
        while(fgets(myString, NMAX, fptr))
        {
            unsigned int size = strlen(myString) - 2;
            // Parse the thing
            if(!line)
            {
                ptr = strtok(myString, ":");
                ptr = strtok(NULL, ":");

                // Recolte les seeds
                while(*ptr != '\n')
                {
                    data_set[0].input[nb_seeds++] = strtol(ptr, &end_ptr, 10);
                    assert(end_ptr != ptr);
                    ptr = end_ptr;
                }
            }
            else if(strstr(myString, "map:\n"))
            {
                if(n_step >= 0)
                    nb_line[n_step] = k;
                n_step++;
                k = 0;
            }
            else if(myString[0] != '\n')
            {
                ptr = myString;
                range_set[n_step].dest_start[k] = strtol(ptr, &end_ptr, 10); 
                assert(end_ptr != ptr);
                ptr = end_ptr;
                
                
                range_set[n_step].src_start[k] = strtol(ptr, &end_ptr, 10);
                assert(end_ptr != ptr);
                ptr = end_ptr;

                range_set[n_step].len[k] = strtol(ptr, &end_ptr, 10);
                k++;

                if(n_step == 6)
                    nb_line[6] = k;
            }
            line++;
        }
    }
    // If the file does not exist
    else
    {
        printf("Not able to open the file.");
    }
   
    // Close the file
    fclose(fptr);

    for (index = 0 ; index < nb_seeds; index++)
    {
        process(data_set, range_set, nb_line, index);

        if(data_set[6].output[index] < min)
            min = data_set[6].output[index];

        printf("%ld\n", data_set[6].output[index]);
    }

    printf("%ld\n", min);


	return 0;
}
