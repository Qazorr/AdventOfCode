#include "./../helpers/helpers.h"

//todo: revisit part 2 (try to make the general grid)

int change(std::string option)
{
    if (option == "on")
    {
        return 1;
    }
    else if (option == "off")
    {
        return -1;
    }
    else if (option == "toggle")
    {
        return 2;
    }
    else
    {
        std::cerr << "bad option";
        return 0;
    }
}

int solve(const std::vector<std::string> &lines, int part)
{
    auto bg = aoc::BooleanGrid(1000, 1000);
    std::vector<std::vector<int>> matrix(1000, std::vector<int>(1000, 0));
    if (part == 1)
    {
        for (const auto &line : lines)
        {
            auto after_split = aoc::split(line, " ");
            std::string option = after_split[0] == "turn" ? after_split[1] : after_split[0];
            auto first_point = aoc::split(after_split[after_split.size() - 3], ",");
            auto second_point = aoc::split(after_split[after_split.size() - 1], ",");
            bg.change(bg.generate_points(first_point[0], first_point[1], second_point[0], second_point[1]), option);
        }
        return bg.count();
    }
    else if (part == 2)
    {
        for (const auto &line : lines)
        {
            auto after_split = aoc::split(line, " ");
            std::string option = after_split[0] == "turn" ? after_split[1] : after_split[0];
            auto first_point = aoc::split(after_split[after_split.size() - 3], ",");
            auto second_point = aoc::split(after_split[after_split.size() - 1], ",");
            auto points = bg.generate_points(first_point[0], first_point[1], second_point[0], second_point[1]);
            for (const auto &point : points)
            {
                matrix[point.real()][point.imag()] += change(option);
                if (matrix[point.real()][point.imag()] < 0)
                    matrix[point.real()][point.imag()] = 0;
            }
        }
        return std::accumulate(matrix.begin(), matrix.end(), 0,
                               [](int acc, const std::vector<int> &row)
                               {
                                   return acc + std::accumulate(row.begin(), row.end(), 0);
                               });
    }
    return -1;
}

int main(int argc, char *argv[])
{
    auto lines = aoc::handle_argv(argc, argv);
    aoc::solve_wrapper(solve, lines, 1);
    aoc::solve_wrapper(solve, lines, 2);
}