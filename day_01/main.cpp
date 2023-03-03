#include "./../helpers/helpers.h"

int solve(std::string input, int part)
{
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
    auto line = aoc::handle_argv(argc, argv)[0];
    std::cout << solve(line, 1) << std::endl;
    std::cout << solve(line, 2) << std::endl;
}