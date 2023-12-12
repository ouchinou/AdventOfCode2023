include ./makefile.conf

NAME=main
STARTUP_DEFS=-D__STARTUP_CLEAR_BSS -D__START=main

LDSCRIPTS=-L. -L$(BASE)/ldscripts -T nokeep.ld
LFLAGS=-lc -lm -lgcc
ARM_LFLAGS=$(LCOV) $(STD_LIB) $(USE_NOHOST) $(LDSCRIPTS) $(GC) $(MAP)

$(NAME)-$(CORE).elf: $(SRC)/$(NAME).c $(STARTUP)
	$(ARM_CC) $^ $(ARM_CFLAGS) $(ARM_LFLAGS) -o $(OUT)/$@
	$(ARM_DIS) -dSs $(OUT)/$@ > $(OUT)/$(NAME)-$(CORE).dis

$(NAME): $(SRC)/$(NAME).c
	$(CC) $^ $(CFLAGS) $(LFLAGS) -o $(OUT)/$@
	$(DIS) -dSs $(OUT)/$@ > $(OUT)/$(NAME).dis

clean: 
	rm -f $(OUT)/*
	rm -f coverage.* *.gcov

# Target built with arm non eabi toolchain
.PHONY: arm
arm: $(NAME)-$(CORE).elf
	@echo '___________________________'
	@echo '_____ BUILD FOR ARM $(CORE) ____ '
	@echo '___________________________'

# Target built with native GCC
.PHONY: native
native: $(NAME)
	@echo '___________________________'
	@echo '_____ BUILD FOR x86_64 ____ '
	@echo '___________________________'
