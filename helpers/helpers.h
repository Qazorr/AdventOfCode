#ifndef HELPERS_H
#define HELPERS_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> get_input_vector(const std::string &filename);
std::vector<std::string> handle_argv(int argc, char *argv[]);
std::vector<std::string> split(std::string s, std::string delimiter);
void display(std::vector<std::string> lines);

#endif