#include "./../helpers/helpers.h"

int solve(const std::vector<std::string> &lines, int part)
{
    std::string input = lines[0];
    if(part == 1) {
        return std::count(input.begin(), input.end(), '(') 
                    - std::count(input.begin(), input.end(), ')');
    } else if(part == 2) {
        int floor = 0;
        for(int i = 0; i<input.length(); i++) {
            floor += input.at(i) == '(' ? 1 : -1;
            if(floor == -1) return i+1;
        }
        return -1;
    }
    return -1;
}

int main(int argc, char *argv[])
{
    auto lines = aoc::handle_argv(argc, argv);
    aoc::solve_wrapper(solve, lines, 1);
    aoc::solve_wrapper(solve, lines, 2);
}