#include "./../helpers/helpers.h"

#include <regex>

int get_real_size(const std::string &s)
{
    std::regex pattern("\\\\x..|\\\\(\"|\\\\)");
    return std::regex_replace(s, pattern, "*").length() - 2;
}

int get_encoded_size(const std::string &s)
{
    std::regex pattern("\"|\\\\");
    return ("\"" + std::regex_replace(s, pattern, "**") + "\"").length();
}

int solve(const std::vector<std::string> &lines, int part)
{
    if (part == 1)
        return accumulate(lines.begin(), lines.end(), 0, [](int sum, const std::string &s)
                          { return sum + s.size() - get_real_size(s); });
    else if (part == 2)
    {
        return accumulate(lines.begin(), lines.end(), 0, [](int sum, const std::string &s)
                          { return sum + get_encoded_size(s) - s.size(); });
    }
    return -1;
}

int main(int argc, char *argv[])
{
    auto lines = aoc::handle_argv(argc, argv);
    std::cout << solve(lines, 1) << std::endl;
    std::cout << solve(lines, 2) << std::endl;
}