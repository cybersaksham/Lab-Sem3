#include <bits/stdc++.h>
using namespace std;

class House;

class Room
{
  House *myHouse;
  string myName;

public:
  Room(House *house, string myName)
  {
    this->myHouse = house;

    if (NULL != this->myHouse)
      this->myName = myName;
    else
      cout << "House is not created yet...\n";
  };

  ~Room()
  {
    this->myHouse = NULL;
    this->myName = "";
  };

  void display()
  {
    cout << this->myName << endl;
  }
};

class House
{
  string myName;
  Room **roomList;
  int rooms;

public:
  House(string myName, int rooms)
  {
    this->myName = myName;
    this->roomList = new Room *[rooms];
    this->rooms = rooms;
    for (int i = 0; i < rooms; i++)
      this->roomList[i] = NULL;
  }

  ~House()
  {
    for (int i = 0; i < rooms; ++i)
    {
      if (this->roomList[i] != NULL)
        delete this->roomList[i];
    }
    delete[] this->roomList;
  }

  void addRoom(Room *&room)
  {
    int i = 0;
    while (i < this->rooms && this->roomList[i] != NULL)
      i++;

    if (i == this->rooms)
      cout << "House is full" << endl;
    else
      this->roomList[i] = room;
  }

  void display()
  {
    cout << endl;
    cout << "Name of the House : " << this->myName << endl;

    if (this->roomList != NULL)
    {
      cout << "Rooms inside house" << endl;
      for (int i = 0; i < rooms; ++i)
      {
        if (this->roomList[i] != NULL)
          this->roomList[i]->display();
      }
    }
  }
};

int main()
{
  House *h1 = new House("House1", 3);

  // Rooms
  Room *r1 = new Room(h1, "Room1");
  Room *r2 = new Room(h1, "Room2");
  Room *r3 = new Room(h1, "Room3");
  Room *r4 = new Room(h1, "Room4");
  r1->display();

  // Adding to house
  h1->addRoom(r1);
  h1->addRoom(r2);
  h1->addRoom(r3);
  h1->addRoom(r4);

  h1->display();

  delete h1;
  r1->display();

  return (0);
}
