#include "./../helpers/helpers.h"

#include <regex>

uint16_t operation(uint16_t x, std::string op, uint16_t y)
{
    if (op == "AND")
    {
        return x & y;
    }
    else if (op == "OR")
    {
        return x | y;
    }
    else if (op == "LSHIFT")
    {
        return x << y;
    }
    else if (op == "RSHIFT")
    {
        return x >> y;
    }
    else if (op == "NOT")
    {
        return ~x;
    }
    return -1;
}

// todo: try to erase/skip elements used
int solve(const std::vector<std::string> &lines, int part)
{
    if (part == 1)
    {
        std::map<std::string, uint16_t> circuit;
        std::vector<std::vector<std::string>> commands;
        std::regex number("[0-9]+");

        for (int i = 0; i < lines.size(); i++)
            commands.push_back(aoc::split(lines.at(i), " "));

        for (int i = 0; i < commands.size(); i++)
        {
            if (std::regex_match(commands[i][0], number))
                circuit[commands[i][2]] = std::stoi(commands[i][0]);
        }

        auto find = [&circuit](std::string s)
        { return circuit.find(s) != circuit.end(); };

        int max_iter = lines.size(), j = 0;
        while (!commands.empty() && j != max_iter)
        {
            for (int i = 0; i < commands.size(); i++)
            {
                if (commands[i][0] == "NOT")
                {
                    uint16_t argument;
                    if (std::regex_match(commands[i][1], number))
                        argument = std::stoi(commands[i][1]);
                    else
                    {
                        if (find(commands[i][1]))
                            argument = circuit[commands[i][1]];
                        else
                            continue;
                    }
                    circuit[commands[i][3]] = operation(argument, commands[i][0], 0);
                }
                else if (commands[i][1] == "AND" || commands[i][1] == "OR" || commands[i][1] == "LSHIFT" || commands[i][1] == "RSHIFT")
                {
                    uint16_t first_argument, second_argument;
                    if (std::regex_match(commands[i][0], number))
                        first_argument = std::stoi(commands[i][0]);
                    else
                    {
                        if (find(commands[i][0]))
                            first_argument = circuit[commands[i][0]];
                        else
                            continue;
                    }
                    if (std::regex_match(commands[i][2], number))
                        second_argument = std::stoi(commands[i][2]);
                    else
                    {
                        if (find(commands[i][2]))
                            second_argument = circuit[commands[i][2]];
                        else
                            continue;
                    }
                    circuit[commands[i][4]] = operation(first_argument, commands[i][1], second_argument);
                }
                else if (commands[i].size() == 3)
                {
                    if (find(commands[i][0]))
                        circuit[commands[i][2]] = circuit[commands[i][0]];
                }
            }
            j++;
        }
        return circuit["a"];
    }
    else if (part == 2)
    {
        uint16_t a = solve(lines, 1);

        std::vector<std::string> line_copy(lines);

        std::regex find_b_regex("[0-9]+ -> b");
        for (int i = 0; i < line_copy.size(); i++)
        {
            if (std::regex_match(line_copy[i], find_b_regex))
                line_copy[i] = std::to_string(a) + " -> b";
        }
        return solve(line_copy, 1);
    }
    return -1;
}

int main(int argc, char *argv[])
{
    auto lines = aoc::handle_argv(argc, argv);
    aoc::solve_wrapper(solve, lines, 1);
    aoc::solve_wrapper(solve, lines, 2);
}