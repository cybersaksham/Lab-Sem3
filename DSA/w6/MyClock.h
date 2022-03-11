#include <sys/time.h>
#include <ctime>

class MyClock
{
    long startTime, endTime;

    long getTime()
    {
        struct timeval start;
        gettimeofday(&start, NULL);
        return start.tv_sec * 1000000 + start.tv_usec;
    }

public:
    MyClock() : startTime(0), endTime(0) {}

    void startClock() { this->startTime = this->getTime(); }
    void endClock() { this->endTime = this->getTime(); }
    double consumedTimeInSecond() const { return (this->endTime - this->startTime) / (1000000.0); }
    void resetClock() { this->startTime = this->endTime = 0; }
};
