package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	// declaration
	counts := make(map[string]int)

	// get args
	files := os.Args[1:]

	// if args is nothing... input standard input
	if len(files) == 0 {
		//call countline method
		// f is file
		// counts is map
		countLines(os.Stdin, counts)
	} else {
		for _, arg := range files {
			// file opens
			f, err := os.Open(arg)

			// file opne error check
			if err != nil {
				fmt.Fprintf(os.Stderr, "1_3_1: %v\n", err)
				continue
			}
			//call countline method
			// f is file
			// counts is map
			countLines(f, counts)
			f.Close()
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d¥t%s\n", n, line)
		}
	}
}

func countLines(f *os.File, counts map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()]++
	}
}
