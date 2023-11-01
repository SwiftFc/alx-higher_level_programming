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
	listint_t new_node;
	listint_t current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL)

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
