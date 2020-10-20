SHELL := /bin/bash

BIN_NAME = kantan
K_FILES = src/ast/item.kan \
		  src/ast/lexer.kan \
		  src/ast/mod.kan \
		  src/ast/parser.kan \
		  src/ast/token.kan \
		  src/cli/config.kan \
		  src/cli/opt.kan \
		  src/cli/report.kan \
		  src/codegen/target.kan \
		  src/compiler.kan \
		  src/error.kan \
		  src/main.kan \
		  src/memory/arena.kan \
		  src/source/file.kan \
		  src/source/ident.kan \
		  src/source/modmap.kan \
		  src/source/position.kan \
		  src/source/span.kan \
		  src/std/cdeps.kan \
		  src/std/dbg.kan \
		  src/std/files/path.kan \
		  src/std/files/unix.kan \
		  src/std/libc.kan \
		  src/std/map.kan \
		  src/std/num.kan \
		  src/std/ptrvec.kan \
		  src/std/str.kan \
		  src/std/vec.kan \
		  src/std/vmap.kan \
		  src/types/data.kan \
		  src/types/primitive.kan \
		  src/types/subst.kan \
		  src/types/types.kan \
		  src/util.kan

C_FILES = lib.c
C_OBJ_FILES = $(C_FILES:.c=.c.o)
START_FOLDER = $(shell pwd)

LLVM_PATH = $(HOME)/Downloads/llvm/llvm-10.0.0.src/build
LLVM_CONFIG = $(LLVM_PATH)/bin/llvm-config

LLVM_LIB_NAMES = x86codegen webassemblycodegen passes

LLVM_C_FLAGS = $(shell $(LLVM_CONFIG) --cflags)
LLVM_LD_FLAGS = $(shell $(LLVM_CONFIG) --ldflags)
LLVM_LIBS = $(shell $(LLVM_CONFIG) --libs $(LLVM_LIB_NAMES))
LLVM_SYS_LIBS = $(shell $(LLVM_CONFIG) --system-libs)

LD_FLAGS = $(LLVM_LD_FLAGS) -fdata-sections -ffunction-sections
LIBS = $(LLVM_LIBS) $(LLVM_SYS_LIBS) -Wl,--gc-sections

KANTAN_STABLE = $(START_FOLDER)/../kantan -g
KANTAN_KANTAN_MEMCHECK = valgrind --leak-check=full --suppressions=$(START_FOLDER)/suppress-llvm-errors.supp $(START_FOLDER)/compiler
KANTAN_KANTAN_MASSIF = valgrind --tool=massif --massif-out-file=../massif.out $(START_FOLDER)/compiler
KANTAN_KANTAN = $(KANTAN_KANTAN_MEMCHECK) -g

$(BIN_NAME) : $(K_FILES) $(C_OBJ_FILES)
	if $(KANTAN_STABLE) $(K_FILES) -o out.o; then \
		g++ $(LD_FLAGS) -o $(BIN_NAME) out.o $(C_OBJ_FILES) $(LIBS); \
		rm out.o ; \
		rm $(C_OBJ_FILES) ; \
	fi

$(C_OBJ_FILES) : $(C_FILES)
	for file in $(C_FILES) ; do \
		gcc -O3 -Wall -c $$file -o $(addsuffix .o, $$file); \
	done

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
	pushd test && \
	python3 -m runner.main ../$(BIN_NAME) runner/cases --valgrind $(TEST_ARGS); \
	popd

.PHONY: clean
clean :
	rm $(BIN_NAME) ; \
	rm *.o
