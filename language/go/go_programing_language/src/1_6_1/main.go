package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"time"
)

func main() {
	// 現在の時刻を取得
	file, err := os.OpenFile("/Users/kim/work/git/learn/go/go_programing_language/result/1_6_1.txt", os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0666)

	start := time.Now()

	// chanという文字列のチャネルを生成
	ch := make(chan string)
	for _, url := range os.Args[1:] {
		// goは引数に対し新しいゴルーチンを生成
		go fetch(url, ch) // start ゴルーチン
		go fetch(url, ch) // start ゴルーチン
	}
	for range os.Args[1:] {
		fmt.Fprintln(file, <-ch) // send ch channel
	}

	if err != nil {
		log.Printf("%s\n", err)
	}
	fmt.Fprintf(file, "%.2fs elapsed\n", time.Since(start).Seconds())

}

func fetch(url string, ch chan<- string) {
	// 現在の時刻を取得
	start := time.Now()
	// getで引数のurlのhttpを取得
	resp, err := http.Get(url)

	// エラーの場合、errがnilでなくなるため、ここでエラーを処理
	if err != nil {
		ch <- fmt.Sprint(err)
		return
	}

	// copyでresponseの内容を読み込み
	//discardで出力ストリームへ書き込みし内容を破棄
	// copyはバイト数とエラーを返すので変数名をnbytes,errとしている
	nbytes, err := io.Copy(ioutil.Discard, resp.Body)
	resp.Body.Close() // 資源のリーク防止
	if err != nil {
		ch <- fmt.Sprintf("while reading %s: %v", url, err)
		return
	}
	//startの変数から
	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs %7d %s", secs, nbytes, url)
}
