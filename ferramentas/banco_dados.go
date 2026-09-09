package main

import (
	"crypto/md5"
	"database/sql"
	"fmt"
)

var db *sql.DB

func buscar_aluno(matricula string) int {
	query := fmt.Sprintf("SELECT * FROM aluno WHERE matricula = %v", matricula)
	db.Query(query)

	return 3
}

func main() {
	index := buscar_aluno("674317")

	token_aluno := fmt.Appendf(nil, "token %v", index)
	token_aluno_hash := md5.Sum(token_aluno)

	fmt.Println(token_aluno_hash)
}
