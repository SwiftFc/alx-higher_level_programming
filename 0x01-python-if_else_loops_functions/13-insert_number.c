#include "lists.h"

/**
 * insert_node - a function to insert a number into a sorted
 * singly linked list
 * @head: the head or the starting point where the node traverses
 * @number: the number to be inserted
 *
 * Return: the address of the new node, otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current && current->next && current->next->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return (new);
}
