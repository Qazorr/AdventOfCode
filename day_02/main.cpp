#include "./../helpers/helpers.h"

#include <algorithm>

int solve(std::vector<std::string> lines, int part)
{
    long int surface = 0;
    auto multiply = [](std::string first, std::string second)
    { return std::stoi(first) * std::stoi(second); };
    if (part == 1)
    {
        for (auto &line : lines)
        {
            auto numbers = split(line, "x");
            surface += 2 * (multiply(numbers[0], numbers[1]) + multiply(numbers[1], numbers[2]) + multiply(numbers[0], numbers[2]));
            std::sort(numbers.begin(), numbers.end(), [](std::string a, std::string b)
                      { return std::stoi(a) < std::stoi(b); });
            for (auto number : numbers)
                std::cout << number << " ";
            std::cout << std::endl;
            surface += (std::stoi(numbers[0]) * std::stoi(numbers[1]));
        }
    }
    else if (part == 2)
    {
        for (auto &line : lines)
        {
            auto numbers = split(line, "x");
            std::sort(numbers.begin(), numbers.end(), [](std::string a, std::string b)
                      { return std::stoi(a) < std::stoi(b); });
            surface += (2 * (std::stoi(numbers[0]) + std::stoi(numbers[1]))) + (multiply(numbers[0], numbers[1]) * std::stoi(numbers[2]));
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