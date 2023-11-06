#include "lists.h"

/**
 * is_palindrome - A function to check if it is a palindrome
 * @head: the head of the node
 * Return: If it is a palindrome or not
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast;
	listint_t *slow;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL)
	{
		return (1);
	}

	fast = *head;
	slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
/**
 * newNode - insert a new node
 * @val: the value to be inserted
 * Return: the new node
 */

listint_t *newNode(int val)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	new_node->n = val;

	new_node->next = NULL;
	return (new_node);
}
