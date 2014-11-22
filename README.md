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

Put board in DFU mode using dfu-util:

`make pgm`

Or, convert the ELF file to binary format,
then flash the binary using https://github.com/texane/stlink:

```
arm-none-eabi-objcopy -O binary flash.elf flash.bin
st-flash write flash.bin 0x8000000
```
