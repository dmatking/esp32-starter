#pragma once
#include <stdbool.h>

void board_init(void);
const char *board_get_name(void);
bool board_has_lcd(void);
void board_lcd_sanity_test(void);
