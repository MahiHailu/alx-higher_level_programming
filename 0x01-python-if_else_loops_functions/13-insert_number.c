#include "lists.h"
/**
 * insert_node - Function that inserts a num into a sorted singly linked list
 * @head: pointer to the linked list
 * @number: The value to be inserted
 * Return: An:wq address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *current;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	
	node->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n <= number)
			current = current->next;
		node->next = current->next;
		current->next = node;
	}

	return (node);
}
