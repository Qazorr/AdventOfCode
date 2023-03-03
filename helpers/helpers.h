#ifndef HELPERS_H
#define HELPERS_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <complex>
#include <map>
#include <algorithm>

namespace aoc
{
    //? general helper functions
    std::vector<std::string> get_input_vector(const std::string &filename);
    std::vector<std::string> handle_argv(int argc, char *argv[]);
    std::vector<std::string> split(std::string s, std::string delimiter);
    void display(std::vector<std::string> lines);

    //? class with imaginary grid that helps with problems in which movement in 2d plane occurs
    class ImaginaryGrid
    {
    private:
        std::complex<double> cur_position{};
        std::map<std::string, std::complex<double>> moves{
            {"up", (std::complex<double>(0, 1))},
            {"down", (std::complex<double>(0, -1))},
            {"left", (std::complex<double>(-1, 0))},
            {"right", (std::complex<double>(1, 0))}};

    public:
        struct ComplexHash
        {
            std::size_t operator()(const std::complex<double> &c) const;
        };
        std::complex<double> get_cur_pos();
        void move(std::string where);
    };
}

#endif