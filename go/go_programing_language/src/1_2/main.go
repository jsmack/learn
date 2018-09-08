package main

import (
	"fmt"
	"os"
)

func main() {
	var s, sep string
	// for i := 1; i < len(os.Args); i++ {
	for i := len(os.Args) - 1; i >= ; i-- {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Println(s)
}
