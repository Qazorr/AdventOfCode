#include "./../helpers/helpers.h"

#include <unordered_set>

// todo: can be revisited with regex :)

// could be made into single for loop
bool vowel_valid(const std::string &s)
{
    return 3 <= std::count_if(s.begin(), s.end(), [](char ch)
                              { return ch == 'a' || ch == 'e' || ch == 'o' || ch == 'i' || ch == 'u'; });
}

bool double_letter_valid(const std::string &s)
{
    for (int i = 0; i < s.length() - 1; i++)
    {
        if (s.at(i) == s.at(i + 1))
            return true;
    }
    return false;
}

bool disallowed_string_valid(const std::string &s)
{
    const std::string disallowed[] = {"ab", "cd", "pq", "xy"};
    for (const auto &substr : disallowed)
    {
        if (std::search(s.begin(), s.end(), substr.begin(), substr.end()) != s.end())
            return false;
    }
    return true;
}

bool pair_valid(const std::string &s)
{
    std::unordered_set<std::string> pairs{};
    std::string next_pair;

    auto create_pair = [](char a, char b)
    { return std::string(1, a) + std::string(1, b); };

    for (int i = 0; i < s.length() - 1; i++)
    {
        next_pair = create_pair(s.at(i), s.at(i + 1));
        if (pairs.find(next_pair) != pairs.end())
            return true;
        if (i != s.length() - 2 && s.at(i) == s.at(i + 1) && s.at(i + 1) == s.at(i + 2))
            i++;
        pairs.insert(next_pair);
    }
    return false;
}

bool letter_between_valid(const std::string &s)
{
    for (int i = 0; i < s.length() - 2; i++)
    {
        if (s.at(i) == s.at(i + 2))
            return true;
    }
    return false;
}

int solve(const std::vector<std::string> &lines, int part)
{
    if (part == 1)
        return std::count_if(lines.begin(), lines.end(), [](std::string s)
                             { return vowel_valid(s) && double_letter_valid(s) && disallowed_string_valid(s); });
    else if (part == 2)
        return std::count_if(lines.begin(), lines.end(), [](std::string s)
                             { return pair_valid(s) && letter_between_valid(s); });
    return -1;
}

int main(int argc, char *argv[])
{
    auto lines = aoc::handle_argv(argc, argv);
    aoc::solve_wrapper(solve, lines, 1);
    aoc::solve_wrapper(solve, lines, 2);
}