#include <iostream>
#include <fstream>
#include "Node.h"
#include "MyRandom.h"
#include "MyClock.h"
using namespace std;
#define N 1000000
#define M 3000000

void runProgram(long m, Node *head, Node *tail, MyRandom &randGen, MyClock &clockTime)
{
    ofstream runTime("Times_" + to_string(m) + ".txt");
    for(int i=1; i<=100; i++)
    {
        long **operations = randGen.generateOperations(m, "Runs/" + to_string(m) + "_" + to_string(i) + ".txt");
        clockTime.startClock();
        for (int j = 0; j < m; j++)
        {
            long op = operations[j][0];
            long num = operations[j][1];

            if (op == 0) Node::search(head, num);
            else if (op == 1) head = Node::insert(head, num);
            else if (op == 2) head = Node::remove(head, num);
        }
        clockTime.endClock();
        runTime << "Run - " << i << " = " << clockTime.consumedTimeInSecond() << "\n";
        clockTime.resetClock();
        randGen.deleteOperations(operations, m);
    }
    Node::destroy(tail->next);
    tail->next = NULL;
    runTime.close();
}

int main()
{
    // Initializations
    MyRandom randGen;
    MyClock clockTime;
    Node *head = new Node(-1);
    Node *tail = new Node(-1);

    // List of random nos
    ofstream randNos("randomNos.txt");
    for (long i = 0; i < N; i++)
    {
        long randNo = randGen.generateOneRandom(0, 10 * N);
        pair<Node *, Node *> newPair = Node::insertRandom(head, tail, randNo);
        head = newPair.first;
        tail = newPair.second;
        randNos << randNo << "\n";
    }
    randNos.close();

    // Operations
    long **operations = randGen.generateOperations(M, "randomOperations.txt");
    int ips[] = {1000, 10000, 50000, 100000, 1000000};
    for(int i=0; i<5; i++)
    {
        runProgram(ips[i], head, tail, randGen, clockTime);
    }

    // Destroying
    Node::destroy(head);
    randGen.deleteOperations(operations, M);

    return 0;
}