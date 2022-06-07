#include "lists.h"
/**
 *is_palindrome - check if singly linked list is a palindrome
 *@head: head of the list
 *Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
unsigned int len = 1;
listint_t *temp;
if(head == NULL || *head == NULL)
{
return (1);
}
temp = *head;
 while (temp)
{
temp = temp->next;
len++;
}
return (0);
}
