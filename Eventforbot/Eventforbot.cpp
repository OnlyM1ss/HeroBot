#include <windows.h>
#include <iostream>

using namespace std;
class EventPress {
public:
	void Control(string command) {
		if (command == "right") rightEvent();
		else if (command == "left") leftEvent();
		else if (command == "up") upEvent();
		else if (command == "down") downEvent();
	}
private:
	void rightEvent() {
		Sleep(5000);
		keybd_event('d', 0, 0, 0);
	}
	void leftEvent() {
		Sleep(5000);
		keybd_event('a', 0, 0, 0);
	}
	void upEvent() {
		Sleep(5000);
		keybd_event('w', 0, 0, 0);
	}
	void downEvent() {
		Sleep(5000);
		keybd_event('s', 0, 0, 0);
	}
};

int main()
{
	string command;
	//нужно заинклюдить в питон и command будет сама команда;
	EventPress eventing;
	eventing.Control(command);
	
}

