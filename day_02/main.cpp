#include "./../helpers/helpers.h"

int solve(const std::vector<std::string> &lines, int part)
{
    long int surface = 0;
    if (part == 1)
    {
        for (auto &line : lines)
        {
            auto str_numbers = aoc::split(line, "x");
            std::vector<int> numbers;
            std::transform(str_numbers.begin(), str_numbers.end(), std::back_inserter(numbers), [&](std::string s)
                           { return std::stoi(s); });
            surface += 2 * (numbers[0] * numbers[1] + numbers[1] * numbers[2] + numbers[0] * numbers[2]);
            std::sort(numbers.begin(), numbers.end());
            surface += numbers[0] * numbers[1];
        }
    }
    else if (part == 2)
    {
        for (auto &line : lines)
        {
            auto str_numbers = aoc::split(line, "x");
            std::vector<int> numbers;
            std::transform(str_numbers.begin(), str_numbers.end(), std::back_inserter(numbers), [&](std::string s)
                           { return std::stoi(s); });
            std::sort(numbers.begin(), numbers.end());
            surface += 2 * (numbers[0] + numbers[1]) + numbers[0] * numbers[1] * numbers[2];
        }
    }
    return surface;
}

int main(int argc, char *argv[])
{
    auto lines = aoc::handle_argv(argc, argv);
    aoc::solve_wrapper(solve, lines, 1);
    aoc::solve_wrapper(solve, lines, 2);
}