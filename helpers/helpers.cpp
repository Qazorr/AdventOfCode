#include "helpers.h"

std::vector<std::string> aoc::get_input_vector(const std::string &filename)
{
    std::vector<std::string> lines;
    std::ifstream file(filename);
    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
            lines.push_back(line);
        file.close();
    }
    return lines;
}

std::vector<std::string> aoc::handle_argv(int argc, char *argv[])
{
    if (argc != 2)
    {
        std::cerr << "Usage: " << argv[0] << " file_name" << std::endl;
        exit(1);
    }
    return aoc::get_input_vector(argv[1]);
}

std::vector<std::string> aoc::split(std::string s, std::string delimiter)
{
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> result;

    while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos)
    {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        result.push_back(token);
    }

    result.push_back(s.substr(pos_start));
    return result;
}

void aoc::display(std::vector<std::string> lines)
{
    for (std::size_t i = 0; i < lines.size(); ++i)
        std::cout << i << ": " << lines[i] << std::endl;
}

std::complex<double> aoc::ImaginaryGrid::get_cur_pos() { return this->cur_position; }

void aoc::ImaginaryGrid::move(std::string where)
{
    std::vector<std::string> possible_moves{"up", "down", "left", "right"};
    if (std::find(std::begin(possible_moves), std::end(possible_moves), where) != std::end(possible_moves))
    {
        this->cur_position += this->moves[where];
    }
    else
    {
        std::cout << "Invalid move (could be following: up/down/left/right)\n";
    }
}

std::size_t aoc::ImaginaryGrid::ComplexHash::operator()(const std::complex<double> &c) const
{
    std::size_t h1 = std::hash<double>{}(c.real());
    std::size_t h2 = std::hash<double>{}(c.imag());
    return h1 ^ (h2 << 1);
}
