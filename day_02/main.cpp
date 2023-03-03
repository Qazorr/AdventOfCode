#include "./../helpers/helpers.h"

#include <algorithm>

int solve(std::vector<std::string> lines, int part)
{
    long int surface = 0;
    if (part == 1)
    {
        for (auto &line : lines)
        {
            auto str_numbers = split(line, "x");
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
            auto str_numbers = split(line, "x");
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
    auto lines = handle_argv(argc, argv);
    std::cout << solve(lines, 1) << std::endl;
    std::cout << solve(lines, 2) << std::endl;
}