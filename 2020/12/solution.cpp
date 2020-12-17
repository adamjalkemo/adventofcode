#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Instruction
{
    char action;
    unsigned value;
};

const vector<Instruction> sample0 = {{'F', 10},
                                     {'N', 3},
                                     {'F', 7},
                                     {'R', 90},
                                     {'F', 11}};

unsigned get_ships_travelled_distance_pt1(const vector<Instruction> &instructions)
{
    int x = 0;
    int y = 0;
    int dir = 0;
    for (const auto &instruction : instructions)
    {
        switch (instruction.action)
        {
        case 'N':
            y -= instruction.value;
            break;
        case 'S':
            y += instruction.value;
            break;
        case 'E':
            x += instruction.value;
            break;
        case 'W':
            x -= instruction.value;
            break;
        case 'L':
            dir += instruction.value;
            dir = (dir + 360) % 360;
            break;
        case 'R':
            dir -= instruction.value;
            dir = (dir + 360) % 360;
            break;
        case 'F':
            switch (dir)
            {
            case 0:
                x += instruction.value;
                break;
            case 90:
                y -= instruction.value;
                break;
            case 180:
                x -= instruction.value;
                break;
            case 270:
                y += instruction.value;
                break;
            default:
                throw runtime_error("Encountered faulty degree");
            }
            break;
        default:
            throw runtime_error("Didn't recognize action");
        }
    }
    return abs(x) + abs(y);
}

void part1(const vector<Instruction> &instructions)
{
    cout << "Part 1:" << endl;
    assert(get_ships_travelled_distance_pt1(sample0) == 25);
    auto distance = get_ships_travelled_distance_pt1(instructions);
    assert(distance == 845);
    cout << "Solution: The manhattan distance is " << distance << endl;
}

void rotate(int &x, int &y, const int deg)
{
    const double pi = std::acos(-1);
    const double rad = pi * deg / 180;
    int tmp = x;
    x = roundl(x * cos(rad) - y * sin(rad));
    y = roundl(tmp * sin(rad) + y * cos(rad));
}

unsigned get_ships_travelled_distance_pt2(const vector<Instruction> &instructions)
{
    int x = 0;
    int y = 0;
    int wx = 10;
    int wy = -1;
    for (const auto &instruction : instructions)
    {
        switch (instruction.action)
        {
        case 'N':
            wy -= instruction.value;
            break;
        case 'S':
            wy += instruction.value;
            break;
        case 'E':
            wx += instruction.value;
            break;
        case 'W':
            wx -= instruction.value;
            break;
        case 'L':
            rotate(wx, wy, -instruction.value);
            break;
        case 'R':
            rotate(wx, wy, instruction.value);
            break;
        case 'F':
            x += instruction.value * wx;
            y += instruction.value * wy;
            break;
        default:
            throw runtime_error("Didn't recognize action");
        }
    }
    return abs(x) + abs(y);
}

void part2(const vector<Instruction> &instructions)
{
    cout << "Part 1:" << endl;
    assert(get_ships_travelled_distance_pt2(sample0) == 286);
    auto distance = get_ships_travelled_distance_pt2(instructions);
    cout << "Solution: The manhattan distance is " << distance << endl;
    assert(distance == 27016);
}

int main()
{
    ifstream infile;
    infile.open("input.txt");
    vector<Instruction> instructions;
    char a;
    unsigned v;
    while (infile >> a >> v)
    {
        instructions.push_back({a, v});
    }

    part1(instructions);
    part2(instructions);
    return 0;
}
