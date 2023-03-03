#include "./../helpers/helpers.h"

#include <openssl/md5.h>
#include <string>
#include <iomanip>
#include <sstream>

std::string to_MD5_hash(const std::string &s)
{
    unsigned char hash[MD5_DIGEST_LENGTH];

    MD5((const unsigned char *)s.c_str(), s.length(), hash);

    std::ostringstream oss;
    oss << std::hex << std::setfill('0');
    for (size_t i = 0; i < MD5_DIGEST_LENGTH; i++)
    {
        oss << std::setw(2) << static_cast<unsigned int>(hash[i]);
    }
    return oss.str();
}

int solve(const std::string &line, int part)
{
    int number = 0;
    std::string hash, to_hash;
    std::string to_find = part == 1 ? "00000" : "000000";
    while (1)
    {
        to_hash = line + std::to_string(number);
        hash = to_MD5_hash(to_hash);
        std::cout << hash << " " << to_hash << "\r";
        if (hash.rfind(to_find, 0) == 0)
        {
            std::cout << std::endl;
            return number;
        }
        number++;
    }
}

int main(int argc, char *argv[])
{
    std::string str = aoc::handle_argv(argc, argv)[0];
    std::cout << solve(str, 1) << std::endl;
    std::cout << solve(str, 2) << std::endl;
}