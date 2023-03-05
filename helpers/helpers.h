#ifndef HELPERS_H
#define HELPERS_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <complex>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>

namespace aoc
{
    //? general helper functions
    std::vector<std::string> get_input_vector(const std::string &filename);
    std::vector<std::string> handle_argv(int argc, char *argv[]);
    std::vector<std::string> split(std::string s, std::string delimiter);
    void display(const std::vector<std::string> &lines);

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

    class BooleanGrid
    {
    private:
        std::vector<std::vector<bool>> m;

    public:
        BooleanGrid(unsigned int x, unsigned int y);

        class grid_row
        {
        private:
            std::vector<bool> &row;

        public:
            grid_row(std::vector<bool> &r) : row(r) {}
            std::vector<bool>::reference operator[](unsigned int y) { return row.at(y); }
        };

        grid_row operator[](unsigned int x) { return grid_row(m.at(x)); }
        void change(unsigned int xpos, unsigned int ypos, std::string option);
        void change(std::vector<std::complex<double>> positions, std::string option);

        std::vector<std::complex<double>> generate_points(int x1, int y1, int x2, int y2);
        std::vector<std::complex<double>> generate_points(std::string x1, std::string y1, std::string x2, std::string y2);
        int count();
        void display();
    };
}

#endif