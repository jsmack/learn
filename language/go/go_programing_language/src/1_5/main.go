package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func main() {

	for _, url := range os.Args[1:] {
		if !strings.HasPrefix(url, "https://") {
			url = "https://" + url
		} else if !strings.HasPrefix(url, "http://") {
			url = "http://" + url
		}

		resp, err := http.Get(url)

		if err != nil {
			fmt.Fprintf(os.Stderr, "1_5: %v\n", err)
			os.Exit(1)
		}
		// if _, err := io.Copy(os.Stdout, resp.Body); err != nil {
		// 	fmt.Fprintf(os.Stderr, "1_5: %v\n", err)
		// }
		fmt.Println(resp.Status)

		// ReadAllでレスポンス全体を読み込み
		// 対象をbody
		b, err := ioutil.ReadAll(resp.Body)
		resp.Body.Close()
		if err != nil {
			// fmt.Fprintf(os.Stderr, "1_5: reading %s: %v\n", url, err)
			os.Exit(1)
		}
		fmt.Printf("%s", b)
	}
}
