package main

import (
	"fmt"
	"os"
)

func main() {
	prac1(os.Args)
	prac2(os.Args)
}

func prac1(Args []string) {
	fmt.Println(Args[0])
}

func prac2(Args []string) {
	for _, args := range Args[1:] {
		fmt.Println(args)
	}
}
