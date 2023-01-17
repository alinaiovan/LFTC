%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
int yyerror(char *s);

#define YYDEBUG 1
%}

%token STRING;
%token INT;
%token ARRAY;
%token IF;
%token READ;
%token WRITE;
%token ELSE;
%token WHILE;
%token FOR;
%token RETURN;

%token IDENTIFIER;
%token CONSTANT;

%token PLUS;
%token MINUS;
%token TIMES;
%token DIV;
%token FLOATDIV;
%token MOD;
%token EQ;
%token EQQ;
%token BIGGER;
%token SMALLER;
%token AND;
%token OR;

%token SEMICOLON;
%token COMMA;
%token CURLYOPEN;
%token CURLYCLOSE;
%token BRACKETOPEN;
%token BRACKETCLOSE;
%token RIGHTOPEN;
%token RIGHTCLOSE;
%token ARROWOPEN;
%token ARROWCLOSE;
%token TILDE;
%token PERCENT;

%start Program 

%%
Program: StmtList {printf("Program -> DeclList ; StmtList\n");}
	;
Declaration: Type IDENTIFIER {printf("Declaration -> Type IDENTIFIER\n");}
	| Type IDENTIFIER COMMA Declaration {printf("Declaration -> Type IDENTIFIER COMMA Declaration\n");}
	;
Type1 : STRING {printf("Type1 -> $\n");} 
	| INT {printf("Type1 -> #\n");} 
	| ARRAY {printf("Type1 -> @\n");}
	;
ArrayDecl: RIGHTOPEN Type1 RIGHTCLOSE {printf("ArrayDecl -> [ Type1 ]\n");}
	;
Type: Type1 {printf("Type -> Type1\n");} 
	| ArrayDecl {printf("Type -> ArrayDecl\n");}
	;
StmtList: Stmt {printf("StmtList -> Stmt\n");} 
	| Stmt SEMICOLON StmtList {printf(" StmtList -> Stmt ; StmtList\n");}
	;
Stmt: SimpleStmt {printf("Stmt -> SimpleStmt\n");} 
	| StructStmt {printf("Stmt -> StructStmt\n");}
	| Declaration {printf("Stmt -> Declaration\n");}
	;
SimpleStmt: AssignStmt {printf("SimpleStmt -> AssignStmt\n");} 
	| IosStmt {printf("SimpleStmt -> IosStmt\n");}
	;
AssignStmt: IDENTIFIER EQ Expression {printf("AssignStmt -> IDENTIFIER <= Expression\n");}
	;
Expression: Expression PLUS Term {printf("Expression -> Expression + Term\n");} 
	| Term {printf("Expression -> Term\n");}
	;
Term: Term TIMES Factor {printf("Term -> Term * Factor\n");} 
	| Term DIV Factor {printf("Term -> Term // Factor\n");} 
	| Term FLOATDIV Factor {printf("Term -> Term /. Factor\n");}
	| Factor {printf("Term -> Factor\n");}
	;
Factor: BRACKETOPEN Expression BRACKETCLOSE {printf("Factor -> ( Expression )\n");} 
	| IDENTIFIER {printf("Factor -> IDENTIFIER\n");} 
	| CONSTANT {printf("Factor -> CONSTANT\n");} 
	;
IosStmt: READ BRACKETOPEN IDENTIFIER BRACKETCLOSE {printf("IosStmt -> read ( IDENTIFIER )\n");} 
	| WRITE BRACKETOPEN IDENTIFIER BRACKETCLOSE {printf("IosStmt -> write ( IDENTIFIER )\n");}
	;
StructStmt: StmtList {printf("StructStmt -> StmtList\n");} 
	| IfStmt {printf("StructStmt -> IfList\n");} 
	| WhileStmt {printf("StructStmt -> WhileList\n");}
	;
IfStmt: IF BRACKETOPEN Condition BRACKETCLOSE CURLYOPEN Stmt CURLYCLOSE ELSE CURLYOPEN Stmt CURLYCLOSE {printf("if ( Condition ) { Stmt } else { Stmt }");}
	;
WhileStmt: WHILE BRACKETOPEN Condition BRACKETCLOSE CURLYOPEN Stmt CURLYCLOSE {printf("while ( Condition ) { Stmt }");}
	;
Condition: Expression BIGGER Expression {printf("Condition -> Expression bigger Expression\n");}  
	| Expression SMALLER Expression {printf("Condition -> Expression smaller Expression\n");} 
	| Expression EQQ Expression {printf("Condition -> Expression equal Expression\n");};

%%
int yyerror(char *s) {
    printf("Error: %s", s);
}

extern FILE *yyin;

int main(int argc, char** argv) {
    if (argc > 1) 
        yyin = fopen(argv[1], "r");
    if (!yyparse()) 
        fprintf(stderr, "\tOK\n");
}