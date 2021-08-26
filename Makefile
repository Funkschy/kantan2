K_FILES = $(shell find src -name '*.kan')

CC ?= gcc
BIN_NAME ?= kantan
STDLIB_DIR ?= src/std
KANTAN_STABLE ?= kantan

KANTAN_STABLE_FLAGS := -g
C_DEFINES := -DSTDLIB_DIR=\"$(STDLIB_DIR)\"
C_FILES := lib.c
C_FLAGS := -O3 -Wall -Wextra -pedantic -std=c99 -Werror

$(BIN_NAME) : Makefile $(K_FILES) $(C_FILES)
	$(KANTAN_STABLE) $(KANTAN_STABLE_FLAGS) $(K_FILES) -o $(BIN_NAME).o
	$(CC) $(C_FLAGS) $(C_FILES) $(BIN_NAME).o -o $(BIN_NAME)
	rm $(BIN_NAME).o

type-graph.png : $(BIN_NAME) test.kan
	( \
		. tools/venv/bin/activate ;\
		./$(BIN_NAME) test.kan --mi --dump-type-graph | tools/graphformat.py type-graph | dot -Tpng > type-graph.png \
	)

call-graph.png : $(BIN_NAME) test.kan
	( \
		. tools/venv/bin/activate ;\
		./$(BIN_NAME) test.kan --mi --dump-call-graph | tools/graphformat.py call-graph | dot -Tpng > call-graph.png \
	)


# This makes it possible to do stuff like `make test -- --show-skipped`
# see https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run
# If the first argument is "test"...
ifeq (test,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "test"
  TEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(TEST_ARGS):;@:)
endif

.PHONY: test
test : $(BIN_NAME)
	cd test && \
	python3 -m runner.main ../$(BIN_NAME) runner/cases $(TEST_ARGS)


ifeq (ir,$(firstword $(MAKECMDGOALS)))
  IR_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(IR_ARGS):;@:)
endif

.PHONY: ir
ir : $(BIN_NAME)
	./$(BIN_NAME) --mi --dump-ir $(IR_ARGS) | tools/irformat.py


.PHONY: clean
clean :
	rm $(BIN_NAME)
