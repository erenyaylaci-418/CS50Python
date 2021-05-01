// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 10000

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

unsigned int count = 0;
// Hashes word to a number between 0 and 25, inclusive, based on its first letter

unsigned int hash(const char *word)
{
    unsigned int hash_new = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash_new = (hash_new << 2) ^ word[i];
    }
    return hash_new % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)//dosya sonu olana kadar
    {

        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return false;

        }
        strcpy(new_node->word,word);
        new_node->next = NULL;

        int index = hash(new_node->word);

        node *head = hashtable[index]
        if(head == NULL)
        {
            hashtable[index] = new_node;
            count++;
        }
        else
        {
            new_node->next = hashtable[index];
            hashtable[index] = new_node;
            count++;
        }


        
        // TODO

    }

    // Close dictionary
    fclose(file);
    free(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    unsigned int  a = count;
    return a ;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = strlen(word);
    char word_copy[LENGTH + 1];
    for(int i = 0; i<index; i++)
    {
        word_copy[i] = tolower(word[i]);
    }
    word_copy[index] = '\0'
    int h = hash(word_copy);

    node *cursor = hashtable[h];
    while(cursor != NULL)
    {
        int i;
        i = strcasecmp(cursor->word,word_copy);
        if(i == 0)
        {
            return true;         
        }
        else
        {
            cursor = cursor->next;
        }
    }

    
    // TODO
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for(int i=0; i<N; i++)
    {
         // tmp1 is like a cursor that points to each node while tmp2 is the pointer that frees the prior node
        node *conteiner=hashtable[i]; // initially tmp1 points to 1st node

        while(conteiner != NULL)
        {

            node *tmp = conteiner;
            conteiner = conteiner -> next;
            free(tmp);
        }
    }
    // TODO
    return false;
}
