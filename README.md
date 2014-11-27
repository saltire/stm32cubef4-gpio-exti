To use:

Grab a copy of the STM32Cube code from here: http://www.st.com/web/en/catalog/tools/PF259243#

Note that the latest version will probably be different from the version number below
(so update your path accordingly).

Also, this is configured to work with the STM3240G_EVAL.
You can find a makefile for the STM32F4-Discovery here:
https://github.com/dhylands/stm32cubef4-gpio-exti

```
cd STM32Cube_FW_F4_V1.3.0/Projects/STM324xG_EVAL/Examples/GPIO/GPIO_EXTI
git clone https://github.com/saltire/stm32cubef4-gpio-exti gcc
cd gcc
make
```

Put the board in DFU mode and flash using dfu-util:
```
make dfu
```

Or, flash using https://github.com/texane/stlink:
```
make stlink
```

This can be adapted to work with example projects in STM32Cube other than GPIO_EXTI.
Included is a Python script that reads the provided config files
and patches the makefile with some build dependencies;
run `python deps.py` after cloning the repo.
You will likely still need to make some manual edits before running `make`,
but it's a good starting point.
