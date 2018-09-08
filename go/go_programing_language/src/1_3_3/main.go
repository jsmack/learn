package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {

	// delclaration and generate map
	counts := make(map[string]int)

	// repetition args...
	for _, filename := range os.Args[1:] {
		// read file
		data, err := ioutil.ReadFile(filename)
		// check read error
		if err != nil {
			fmt.Fprintf(os.Stderr, "1_3_3: %v\n", err)
			continue
		}
		// read line of line of split line feeds
		for _, line := range strings.Split(string(data), "\n") {
			counts[line]++
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}

// go_programing_language/ go $
// go_programing_language/ go $ cat 3

// a
// b
// c
// go_programing_language/ go $ cat 4
// a
// b
// c
// d
// e

// go_programing_language/ go $ go run ./src/1_3_3/main.go  3  4
// 4
// 2       a
// 2       b
// 2       c
// go_programing_language/ go $
