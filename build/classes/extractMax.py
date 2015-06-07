# Script for visualizing extractMax on a maxHeap, step-by-step.
# The initial heap is stored in the myHeap variable (in the bottom of the script)
# Created by Brian Pedersen

def max_heapify(heap, i):
	left = i * 2 + 1
	right = i * 2 + 2
		
	if left < len(heap) and heap[left] > heap[i]:
		largest = left
	else:
		largest = i
	
	if right < len(heap) and heap[right] > heap[largest]:
		largest = right

	if largest != i:
		heap[i], heap[largest] = heap[largest], heap[i]
		print(str(heap) + " exchanged " + str(heap[i]) + " with " + str(heap[largest]))
		max_heapify(heap, largest)
		
def heap_extract_max(heap):
	if len(heap) < 0:
		print("Heap underflow")
	print(str(heap) + " original heap")
	max_node = heap[0]
	heap[0] = heap[len(heap) - 1]
	heap.pop(len(heap)-1)
	print(str(heap) + " extracted (root) " + str(max_node))
	max_heapify(heap, 0)	
	
# Edit here
myheap = [10, 7, 6, 5, 4, 2, 3, 1, 2, 3, 1, 1]
heap_extract_max(myheap)
