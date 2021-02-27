K_FILES = src/ast/generics.kan \
		  src/ast/expr.kan \
		  src/ast/item.kan \
		  src/ast/lexer.kan \
		  src/ast/mod.kan \
		  src/ast/parser.kan \
		  src/ast/signature.kan \
		  src/ast/stmt.kan \
		  src/ast/token.kan \
		  src/ast/tyid.kan \
		  src/cdeps.kan \
		  src/cli/config.kan \
		  src/cli/opt.kan \
		  src/cli/parse.kan \
		  src/cli/report.kan \
		  src/compiler.kan \
		  src/error.kan \
		  src/ir/compile/ctx.kan \
		  src/ir/compile/expr.kan \
		  src/ir/compile/item.kan \
		  src/ir/compile/locals.kan \
		  src/ir/compile/stmt.kan \
		  src/ir/ir.kan \
		  src/ir/memory.kan \
		  src/ir/rvalue.kan \
		  src/main.kan \
		  src/memory/arena.kan \
		  src/source/file.kan \
		  src/source/ident.kan \
		  src/source/modmap.kan \
		  src/source/position.kan \
		  src/source/span.kan \
		  src/std/alloc.kan \
		  src/std/dbg.kan \
		  src/std/files/path.kan \
		  src/std/files/unix.kan \
		  src/std/io.kan \
		  src/std/libc.kan \
		  src/std/map.kan \
		  src/std/num.kan \
		  src/std/ptrvec.kan \
		  src/std/str.kan \
		  src/std/vec.kan \
		  src/std/vmap.kan \
		  src/target/parse.kan \
		  src/target/target.kan \
		  src/types/check/binary.kan \
		  src/types/check/call.kan \
		  src/types/check/expr.kan \
		  src/types/check/item.kan \
		  src/types/check/literal.kan \
		  src/types/check/stmt.kan \
		  src/types/check/unary.kan \
		  src/types/ctx.kan \
		  src/types/data.kan \
		  src/types/finalize/expr.kan \
		  src/types/finalize/item.kan \
		  src/types/finalize/stmt.kan \
		  src/types/finalize/types.kan \
		  src/types/function.kan \
		  src/types/graph.kan \
		  src/types/info.kan \
		  src/types/instances.kan \
		  src/types/primitive.kan \
		  src/types/resolve/functions.kan \
		  src/types/scope.kan \
		  src/types/template.kan \
		  src/types/types.kan \
		  src/types/util.kan \
		  src/util.kan

CC ?= gcc
BIN_NAME ?= kantan
STDLIB_DIR ?= src/std
KANTAN_STABLE ?= /usr/local/bin/kantan

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
		./$(BIN_NAME) test.kan --mi --dump-type-graph | tools/graphformat.py | dot -Tpng > type-graph.png \
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
