#include "./../helpers/helpers.h"

#include <unordered_set>

std::string interpret_movement(char c)
{
    if (c == '^')
        return "up";
    else if (c == 'v')
        return "down";
    else if (c == '<')
        return "left";
    else if (c == '>')
        return "right";
    else
        return "bad";
}

int solve(const std::vector<std::string> &lines, int part) {
    aoc::ImaginaryGrid santa, robo_santa;
    std::string movement = lines[0];
    std::unordered_set<std::complex<double>, aoc::ImaginaryGrid::ComplexHash> houses{std::complex<double>(0.0, 0.0)};
    if(part == 1) {
        for(const char &c : movement) {
            santa.move(interpret_movement(c));
            houses.insert(santa.get_cur_pos());
        }
    } else if(part == 2) {
        bool santa_turn = true;
        for (const char &c : movement) {
            if(santa_turn) {
                santa.move(interpret_movement(c));
                houses.insert(santa.get_cur_pos());
            }
            else {
                robo_santa.move(interpret_movement(c));
                houses.insert(robo_santa.get_cur_pos());
            }
            santa_turn = !santa_turn;
        }
    }
    return houses.size();
}

int main(int argc, char *argv[])
{
    auto lines = aoc::handle_argv(argc, argv);
    aoc::solve_wrapper(solve, lines, 1);
    aoc::solve_wrapper(solve, lines, 2);
}