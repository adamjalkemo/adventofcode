#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <istream>
#include <sstream>
#include <iostream>
#include <optional>
#include <string>
#include <vector>

using namespace std;

string sample0 =
    R"(939
    7,13,x,x,59,x,31,19)";

struct PuzzleData
{
    unsigned departure_time;
    vector<optional<unsigned>> busses;

    vector<unsigned> get_valid_busses() const
    {
        vector<unsigned> valid_busses;
        for (auto bus : busses)
        {
            if (bus.has_value())
            {
                valid_busses.push_back(bus.value());
            }
        }
        return valid_busses;
    }

    string to_string() const
    {
        stringstream ss;
        ss << departure_time << endl;
        for (auto &bus : busses)
        {
            if (bus.has_value())
            {
                ss << bus.value() << " ";
            }
            else
            {
                ss << "x"
                   << " ";
            }
        }
        ss << endl;
        return ss.str();
    }
};


PuzzleData create_puzzle_data(istream &puzzle_data)
{
    PuzzleData pd;
    assert(puzzle_data >> pd.departure_time);

    // String splitting is cheating..
    while (!puzzle_data.eof() and puzzle_data.good())
    {
        unsigned a;
        char b;
        if (puzzle_data.peek() == ',')
        {
            puzzle_data >> b;
        }
        else if (puzzle_data.peek() == 'x')
        {
            puzzle_data >> b;
            pd.busses.push_back({});
        }
        else
        {
            assert(puzzle_data >> a);
            pd.busses.push_back(a);
        }
    }
    return pd;
}


auto calculate_departure_time(auto bus, auto departure_time)
{
    return ceil(static_cast<double>(departure_time) / bus) * bus;
}


auto get_bus_with_closest_departure_time(auto busses, auto earliest_departure)
{
    const auto it = min_element(busses.begin(), busses.end(), [&earliest_departure](const auto bus0, const auto bus1) {
        const auto departure_time0 = calculate_departure_time(bus0, earliest_departure);
        const auto departure_time1 = calculate_departure_time(bus1, earliest_departure);
        return departure_time0 - earliest_departure < departure_time1 - earliest_departure;
    });
    assert(it != busses.end());
    return *it;
}


auto get_delay_multiplied_with_bus(istream &puzzle_data)
{
    const PuzzleData pd = create_puzzle_data(puzzle_data);

    const auto busses = pd.get_valid_busses();
    const auto earliest_departure = pd.departure_time;
    const auto bus = get_bus_with_closest_departure_time(busses, earliest_departure);

    const unsigned delay = calculate_departure_time(bus, earliest_departure) - earliest_departure;
    return delay * bus;
}


void part1()
{
    istringstream iss(sample0);
    assert(get_delay_multiplied_with_bus(iss) == 295);

    ifstream infile;
    infile.open("input.txt");
    assert(get_delay_multiplied_with_bus(infile) == 2092);
}


unsigned long long find_consecutive_departures(const auto &busses)
{
    struct BusAndOffset
    {
        unsigned offset;
        unsigned bus;
    };

    vector<BusAndOffset> as;
    for (auto i = 0u; i < busses.size(); ++i)
    {
        const auto &bus = busses[i];
        if (bus.has_value())
        {
            as.push_back({i, bus.value()});
        }
    }

    unsigned long factor = 1;
    unsigned long departure_time = 0;
    for (const auto &bus : as)
    {
        while ((departure_time + bus.offset) % bus.bus != 0)
        {
            departure_time += factor;
        }
        factor *= bus.bus;
    }
    return departure_time;
}


void part2()
{
    assert(find_consecutive_departures(vector<optional<unsigned>>{17, {}, 13, 19}) == 3417);
    assert(find_consecutive_departures(vector<optional<unsigned>>{67, 7, 59, 61}) == 754018);
    assert(find_consecutive_departures(vector<optional<unsigned>>{67, {}, 7, 59, 61}) == 779210);
    assert(find_consecutive_departures(vector<optional<unsigned>>{67, 7, {}, 59, 61}) == 1261476);
    assert(find_consecutive_departures(vector<optional<unsigned>>{1789, 37, 47, 1889}) == 1202161486);

    ifstream infile;
    infile.open("input.txt");
    assert(find_consecutive_departures(create_puzzle_data(infile).busses) == 702970661767766);
}


int main()
{
    part1();
    part2();
    return 0;
}
