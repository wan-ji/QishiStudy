'''
http://poj.org/problem?id=1275


Cashier Employment


Description

A supermarket in Tehran is open 24 hours a day every day and needs a number of cashiers to fit its need. The supermarket manager has hired you to help him, solve his problem. The problem is that the supermarket needs different number of cashiers at different times of each day (for example, a few cashiers after midnight, and many in the afternoon) to provide good service to its customers, and he wants to hire the least number of cashiers for this job.

The manager has provided you with the least number of cashiers needed for every one-hour slot of the day. This data is given as R(0), R(1), ..., R(23): R(0) represents the least number of cashiers needed from midnight to 1:00 A.M., R(1) shows this number for duration of 1:00 A.M. to 2:00 A.M., and so on. Note that these numbers are the same every day. There are N qualified applicants for this job. Each applicant i works non-stop once each 24 hours in a shift of exactly 8 hours starting from a specified hour, say ti (0 <= ti <= 23), exactly from the start of the hour mentioned. That is, if the ith applicant is hired, he/she will work starting from ti o'clock sharp for 8 hours. Cashiers do not replace one another and work exactly as scheduled, and there are enough cash registers and counters for those who are hired.

You are to write a program to read the R(i) 's for i=0..23 and ti 's for i=1..N that are all, non-negative integer numbers and compute the least number of cashiers needed to be employed to meet the mentioned constraints. Note that there can be more cashiers than the least number needed for a specific slot.
Input

The first line of input is the number of test cases for this problem (at most 20). Each test case starts with 24 integer numbers representing the R(0), R(1), ..., R(23) in one line (R(i) can be at most 1000). Then there is N, number of applicants in another line (0 <= N <= 1000), after which come N lines each containing one ti (0 <= ti <= 23). There are no blank lines between test cases.
Output

For each test case, the output should be written in one line, which is the least number of cashiers needed.
If there is no solution for the test case, you should write No Solution for that case.
Sample Input

1
1 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
5
0
23
22
1
10
Sample Output

1
Source

Tehran 2000


'''


'''
x[i]: number of cashiers who start working at time i
s: prefix sum s[i] = x[0] + x[1] + ... + x[i-1]

Constraints:
s[i] - s[i-8] >= R[i-1], i = 8, 9, ..., 24
s[i] - s[i+16] + s[24] >= R[i-1], i = 1, 2, ..., 7
s[i] - s[i-1] >= 0, i = 1, 2, ..., 24
s[i-1] - s[i] >= - maxC[i-1], i = 1, 2, ..., 24
	maxC[i] is the maximum possible number of cashiers starting at time i

s[24] is the total number of cashiers needed, we can do
a binary search on s[24].
'''

import sys

def updateGraph(graph, R, total, cycleLen, shiftLen):
	for i in range(1, shiftLen):
		graph[i + cycleLen - shiftLen][i] = R[i-1] - total


def buildGraph(graph, R, N, maxC, cycleLen, shiftLen):
	for i in range(shiftLen, cycleLen+1):
		graph[i-shiftLen][i] = R[i-1]

	for i in range(cycleLen):
		graph[i][i+1] = 0

	for i in range(cycleLen):
		graph[i+1][i] = - maxC[i]

	updateGraph(graph, R, N, cycleLen, shiftLen)


def isFeasible(graph):
	d = [0] * (len(graph))

	for _ in range(len(graph)):
		for u in range(len(graph)):
			for v, w in graph[u].items():
				if (d[u] + w < d[v]):
					d[v] = d[u] + w

	for u in range(len(graph)):
		for v, w in graph[u].items():
			if (d[u] + w < d[v]):
				return False

	return True




def numCashier(R, N, T):

	cycleLen = 24
	shiftLen = 8
	maxC = [0] * cycleLen
	
	for t in T:
		maxC[t] += 1

	graph = [{} for _ in range(cycleLen+1)]
	buildGraph(graph, R, N, maxC, cycleLen, shiftLen)


	if not isFeasible(graph):
		return "No Solution"

	start, end = 0, N
	while start < end:
		mid = (start + end)//2
		updateGraph(graph, R, mid, cycleLen, shiftLen)
		if isFeasible(graph):
			end = mid
		else:
			start = mid + 1

	return start






def test():
	R = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
	N = 5
	T = [0, 23, 22, 1, 10]

	print(numCashier(R, N, T))


test()













