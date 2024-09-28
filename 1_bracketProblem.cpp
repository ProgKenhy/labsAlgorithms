#include <iostream>
#include <string>

int main()
{
    std::string o_brt = "{[(";
    std::string c_brt = "}])";
    std::string s_brt;
    bool is_correct = true;
    std::cout << "Введите строку: ";
    std::cin >> s_brt;

    for (int i = 1; i < s_brt.length(); i++)
    {
        for (int q = 0; q < o_brt.length(); q++)
        {
            if (s_brt[i] == c_brt[q])
            {
                if (s_brt[i - 1] == o_brt[q])
                {
                    is_correct = true;
                    s_brt.erase(i, 1);
                    s_brt.erase(i - 1, 1);
                    i-=2;
                    break;
                }
                else is_correct = false;
            }
        }
        if (!is_correct)
            break;
    }

    if (s_brt.length() != 0)
    {
        std::cout << "Строка не существует, остались незакрытые(нераскрытые) скобки или посторонний символ: " << std::endl;
        std::cout << s_brt << std::endl;
    }
    else
        std::cout << "Строка cуществует" << std::endl;
}
