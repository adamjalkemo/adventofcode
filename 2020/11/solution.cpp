#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

const array<string, 6> sample0 = {
    "L.LL.LL.LL"
    "LLLLLLL.LL"
    "L.L.L..L.."
    "LLLL.LL.LL"
    "L.LL.LL.LL"
    "L.LLLLL.LL"
    "..L.L....."
    "LLLLLLLLLL"
    "L.LLLLLL.L"
    "L.LLLLL.LL",
    "#.##.##.##"
    "#######.##"
    "#.#.#..#.."
    "####.##.##"
    "#.##.##.##"
    "#.#####.##"
    "..#.#....."
    "##########"
    "#.######.#"
    "#.#####.##",
    "#.LL.L#.##"
    "#LLLLLL.L#"
    "L.L.L..L.."
    "#LLL.LL.L#"
    "#.LL.LL.LL"
    "#.LLLL#.##"
    "..L.L....."
    "#LLLLLLLL#"
    "#.LLLLLL.L"
    "#.#LLLL.##",
    "#.##.L#.##"
    "#L###LL.L#"
    "L.#.#..#.."
    "#L##.##.L#"
    "#.##.LL.LL"
    "#.###L#.##"
    "..#.#....."
    "#L######L#"
    "#.LL###L.L"
    "#.#L###.##",
    "#.#L.L#.##"
    "#LLL#LL.L#"
    "L.L.L..#.."
    "#LLL.##.L#"
    "#.LL.LL.LL"
    "#.LL#L#.##"
    "..L.L....."
    "#L#LLLL#L#"
    "#.LLLLLL.L"
    "#.#L#L#.##",
    "#.#L.L#.##"
    "#LLL#LL.L#"
    "L.#.L..#.."
    "#L##.##.L#"
    "#.#L.LL.LL"
    "#.#L#L#.##"
    "..L.L....."
    "#L#L##L#L#"
    "#.LLLLLL.L"
    "#.#L#L#.##"};

const array<string, 7> sample1 = {"L.LL.LL.LL"
                                  "LLLLLLL.LL"
                                  "L.L.L..L.."
                                  "LLLL.LL.LL"
                                  "L.LL.LL.LL"
                                  "L.LLLLL.LL"
                                  "..L.L....."
                                  "LLLLLLLLLL"
                                  "L.LLLLLL.L"
                                  "L.LLLLL.LL",
                                  "#.##.##.##"
                                  "#######.##"
                                  "#.#.#..#.."
                                  "####.##.##"
                                  "#.##.##.##"
                                  "#.#####.##"
                                  "..#.#....."
                                  "##########"
                                  "#.######.#"
                                  "#.#####.##",
                                  "#.LL.LL.L#"
                                  "#LLLLLL.LL"
                                  "L.L.L..L.."
                                  "LLLL.LL.LL"
                                  "L.LL.LL.LL"
                                  "L.LLLLL.LL"
                                  "..L.L....."
                                  "LLLLLLLLL#"
                                  "#.LLLLLL.L"
                                  "#.LLLLL.L#",
                                  "#.L#.##.L#"
                                  "#L#####.LL"
                                  "L.#.#..#.."
                                  "##L#.##.##"
                                  "#.##.#L.##"
                                  "#.#####.#L"
                                  "..#.#....."
                                  "LLL####LL#"
                                  "#.L#####.L"
                                  "#.L####.L#",
                                  "#.L#.L#.L#"
                                  "#LLLLLL.LL"
                                  "L.L.L..#.."
                                  "##LL.LL.L#"
                                  "L.LL.LL.L#"
                                  "#.LLLLL.LL"
                                  "..L.L....."
                                  "LLLLLLLLL#"
                                  "#.LLLLL#.L"
                                  "#.L#LL#.L#",
                                  "#.L#.L#.L#"
                                  "#LLLLLL.LL"
                                  "L.L.L..#.."
                                  "##L#.#L.L#"
                                  "L.L#.#L.L#"
                                  "#.L####.LL"
                                  "..#.#....."
                                  "LLL###LLL#"
                                  "#.LLLLL#.L"
                                  "#.L#LL#.L#",
                                  "#.L#.L#.L#"
                                  "#LLLLLL.LL"
                                  "L.L.L..#.."
                                  "##L#.#L.L#"
                                  "L.L#.LL.L#"
                                  "#.LLLL#.LL"
                                  "..#.L....."
                                  "LLL###LLL#"
                                  "#.LLLLL#.L"
                                  "#.L#LL#.L#"};

template <unsigned len>
using Seats = array<array<char, len>, len>;

template <unsigned len>
class SeatingPreference
{
public:
    SeatingPreference() = default;
    virtual ~SeatingPreference() = default;
    SeatingPreference(SeatingPreference &) = delete;
    SeatingPreference &operator=(SeatingPreference &) = delete;

    virtual bool wants_to_leave(const Seats<len> &seats, unsigned i, unsigned j) const = 0;
    virtual bool wants_to_sit(const Seats<len> &seats, unsigned i, unsigned j) const = 0;
};

template <unsigned len>
class AdjacentSeatingPreference : public SeatingPreference<len>
{
public:
    bool wants_to_leave(const Seats<len> &seats, unsigned i, unsigned j) const override
    {
        return number_of_adjacent_occupied_seats(seats, i, j) >= 4;
    }

    bool wants_to_sit(const Seats<len> &seats, unsigned i, unsigned j) const override
    {
        return number_of_adjacent_occupied_seats(seats, i, j) == 0;
    }

    unsigned number_of_adjacent_occupied_seats(const auto &seats, unsigned i, unsigned j) const
    {
        auto occupied_seats = 0u;
        auto i_start = max(1u, i) - 1;
        auto i_end = min(len - 1, i + 1);
        auto j_start = max(1u, j) - 1;
        auto j_end = min(len - 1, j + 1);

        for (auto ii = i_start; ii <= i_end; ++ii)
        {
            for (auto jj = j_start; jj <= j_end; ++jj)
            {
                if (ii == i && jj == j)
                {
                    continue;
                }

                occupied_seats += seats[ii][jj] == '#' ? 1 : 0;
            }
        }

        return occupied_seats;
    }
};

template <unsigned len>
class LineOfSightSeatingPreference : public SeatingPreference<len>
{
public:
    bool wants_to_leave(const Seats<len> &seats, unsigned i, unsigned j) const override
    {
        return number_of_occupied_seats(seats, i, j) >= 5;
    }

    bool wants_to_sit(const Seats<len> &seats, unsigned i, unsigned j) const override
    {
        return number_of_occupied_seats(seats, i, j) == 0;
    }

    unsigned number_of_occupied_seats(const auto &seats, unsigned i, unsigned j) const
    {
        struct Direction
        {
            int y;
            int x;
        };

        auto occupied_seats = 0u;
        std::array<Direction, 8> directions = {{{0, 1},
                                                {1, 1},
                                                {1, 0},
                                                {1, -1},
                                                {0, -1},
                                                {-1, -1},
                                                {-1, 0},
                                                {-1, 1}}};
        for (auto direction : directions)
        {
            int ii = i;
            int jj = j;
            while (true)
            {
                ii += direction.y;
                jj += direction.x;
                if (ii >= 0 and ii < static_cast<int>(len) and jj >= 0 and jj < static_cast<int>(len))
                {
                    if (seats[ii][jj] == '#')
                    {
                        occupied_seats += 1;
                        break;
                    }
                    else if (seats[ii][jj] == 'L')
                    {
                        break;
                    }
                }
                else
                {
                    break;
                }
            }
        }
        return occupied_seats;
    }
};

template <unsigned len>
class WaitingArea
{
private:
    Seats<len> seats;
    const SeatingPreference<len> &preference;

public:
    WaitingArea(const string representation, const SeatingPreference<len> &preference) : preference(preference)
    {
        assert(representation.size() == len * len);
        auto idx = 0u;
        for (auto i = 0u; i < len; ++i)
        {
            for (auto j = 0u; j < len; ++j)
            {
                seats[i][j] = representation[idx];
                ++idx;
            }
        }
    }

    template <class Iter>
    void evolve_and_assert(Iter first, Iter last)
    {
        Iter current = first;
        while (current != last)
        {
            evolve();
            assert(to_string() == WaitingArea<len>(*current, preference).to_string());
            ++current;
        }
    }

    unsigned
    count_occupied_seats() const
    {
        auto occupied_seats = 0;
        for (auto i = 0u; i < len; ++i)
        {
            for (auto j = 0u; j < len; ++j)
            {
                if (seats[i][j] == '#')
                {
                    occupied_seats += 1;
                }
            }
        }
        return occupied_seats;
    }

    void evolve_until_convergence(unsigned max_iter = 1000u)
    {
        string old_repr;
        for (auto i = 0u; i < max_iter; ++i)
        {
            evolve();
            if (to_string() == old_repr)
            {
                break;
            }
            old_repr = to_string();
        }
    }

    string to_string() const
    {
        stringstream ss;
        for (auto i = 0u; i < len; ++i)
        {
            for (auto j = 0u; j < len; ++j)
            {
                ss << seats[i][j];
            }
            ss << endl;
        }
        return ss.str();
    }

private:
    void evolve()
    {
        auto new_seats = seats;
        for (auto i = 0u; i < len; ++i)
        {
            for (auto j = 0u; j < len; ++j)
            {
                auto &seat = seats[i][j];
                auto &new_seat = new_seats[i][j];
                switch (seat)
                {
                case 'L':
                    if (preference.wants_to_sit(seats, i, j))
                    {
                        new_seat = '#';
                    }
                    break;
                case '#':
                    if (preference.wants_to_leave(seats, i, j))
                    {
                        new_seat = 'L';
                    }
                    break;
                case '.':
                    break;
                default:
                    throw runtime_error("Unexpected char encountered");
                }
            }
        }
        seats = new_seats;
    }
};

void part1(const string lines)
{
    {
        const AdjacentSeatingPreference<10> p;
        WaitingArea<10>
            wa(sample0[0], p);
        wa.evolve_and_assert(sample0.begin() + 1, sample0.end());
        wa.evolve_until_convergence();
        assert(wa.count_occupied_seats() == 37);
    }

    {
        const AdjacentSeatingPreference<98> p;
        WaitingArea<98> wa(lines, p);
        wa.evolve_until_convergence();
        cout << "Part 1:" << endl;
        cout << "Solution: There will be " << wa.count_occupied_seats() << " occupied seats." << endl;
        assert(wa.count_occupied_seats() == 2476);
    }
}

void part2(const string lines)
{
    {
        const LineOfSightSeatingPreference<10> p;
        WaitingArea<10> wa(sample1[0], p);
        wa.evolve_and_assert(sample1.begin() + 1, sample1.end());
        wa.evolve_until_convergence();
        assert(wa.count_occupied_seats() == 26);
    }

    {
        const LineOfSightSeatingPreference<98> p;
        WaitingArea<98> wa(lines, p);
        wa.evolve_until_convergence();
        cout << "Part 2:" << endl;
        cout << "Solution: There will be " << wa.count_occupied_seats() << " occupied seats." << endl;
        assert(wa.count_occupied_seats() == 2257);
    }
}

int main()
{
    ifstream infile;
    infile.open("input.txt");
    string lines, line;
    while (getline(infile, line))
    {
        lines += line;
    }
    part1(lines);
    part2(lines);
    return 0;
}
