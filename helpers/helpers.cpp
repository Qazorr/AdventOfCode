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

void aoc::display(const std::vector<std::string> &lines)
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
        std::cerr << "Invalid move (could be following: up/down/left/right)\n";
    }
}

std::size_t aoc::ImaginaryGrid::ComplexHash::operator()(const std::complex<double> &c) const
{
    std::size_t h1 = std::hash<double>{}(c.real());
    std::size_t h2 = std::hash<double>{}(c.imag());
    return h1 ^ (h2 << 1);
}

aoc::BooleanGrid::BooleanGrid(unsigned int x, unsigned int y) { m.resize(x, std::vector<bool>(y, false)); }

void aoc::BooleanGrid::change(unsigned int xpos, unsigned int ypos, std::string option)
{
    if (option == "on")
    {
        this->m[xpos][ypos] = true;
    }
    else if (option == "off")
    {
        this->m[xpos][ypos] = false;
    }
    else if (option == "toggle")
    {
        this->m[xpos][ypos] = !m[xpos][ypos];
    }
    else
    {
        std::cerr << "bad option";
    }
}

void aoc::BooleanGrid::change(std::vector<std::complex<double>> positions, std::string option)
{
    for (const auto &pos : positions)
    {
        change(pos.real(), pos.imag(), option);
    }
}

std::vector<std::complex<double>> aoc::BooleanGrid::generate_points(int x1, int y1, int x2, int y2)
{
    std::vector<std::complex<double>> points{};
    for (int x = x1; x <= x2; x++)
    {
        for (int y = y1; y <= y2; y++)
        {
            points.push_back(std::complex<double>(x, y));
        }
    }
    return points;
}

std::vector<std::complex<double>> aoc::BooleanGrid::generate_points(std::string x1, std::string y1, std::string x2, std::string y2)
{
    using std::stoi;
    return generate_points(stoi(x1), stoi(y1), stoi(x2), stoi(y2));
}

int aoc::BooleanGrid::count()
{
    int ctr = 0;
    for (const auto &row : this->m)
    {
        ctr += std::count(row.begin(), row.end(), true);
    }
    return ctr;
}

void aoc::BooleanGrid::display()
{
    std::cout << " " + std::string(2 * this->m.size() + 1, '-') + '\n';
    for (const auto &row : m)
    {
        std::cout << "| ";
        for (const auto &col : row)
        {
            std::cout << col << " ";
        }
        std::cout << "|" << std::endl;
    }
    std::cout << " " + std::string(2 * this->m.size() + 1, '-') + "\n\n";
}