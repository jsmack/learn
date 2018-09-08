package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	echo1(os.Args)
	echo2(os.Args)
	echo3(os.Args)
	echo4(os.Args)
}

func echo1(Args []string) {
	fmt.Println("---- echo1 ----")
	// Declaration
	var s, sep string

	// Get length of array with len
	for i := 1; i < len(Args); i++ {
		s += sep + Args[i]
		sep = " "
	}
	fmt.Println(s)
}

func echo2(Args []string) {
	// Declaration and initialized
	s, sep := "", ""
	// _ is blank identifier
	// range two generate valus
	// index and index position
	fmt.Println("---- echo2 ----")
	for _, arg := range Args[1:] {
		s += sep + arg
		sep = " "
	}
	fmt.Println(s)
}

func echo3(Args []string) {
	fmt.Println("---- echo3 ----")
	// Merge the elements of the array
	fmt.Println(strings.Join(Args[1:], " "))
}

func echo4(Args []string) {
	fmt.Println("---- echo4----")
	// Output raw array valuess
	fmt.Println(Args[1:])
}
