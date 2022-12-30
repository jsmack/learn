package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	// counts generate empty map  for integer
	counts := make(map[string]int)

	// Declaration
	// if file read use os.Open method
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		// equal...
		// line := input.Text()
		// counts[line] = counts[line] + 1
		counts[input.Text()]++
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}
